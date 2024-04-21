import networkx as nx
import community, json, sqlite3
import plotly.express as px
from app.data.philosopher_data import philosophers_data

DB_PATH ='app/database/philosophers.db'

def create_philosopher_graph_test(era='All'):
    G = nx.DiGraph()

    # Connect to the database
    db_connection = sqlite3.connect('app/database/philosophers.db')
    db_cursor = db_connection.cursor()

    # Define the SQL query based on the specified era
    if era == 'All':
        # If 'All' is specified, retrieve all philosophers
        db_cursor.execute('SELECT name, influences FROM philosophers')
    else:
        # If a specific era is specified, retrieve philosophers from that era
        db_cursor.execute('SELECT name, influences FROM philosophers WHERE era = ?', (era,))

    # Fetch all rows as a list of tuples
    rows = db_cursor.fetchall()

    # Create a set to store BC philosophers
    bc_philosophers = set()

    # If era is "AD," identify BC philosophers and exclude them from influences
    if era == "AD":
        bc_philosophers_query = 'SELECT name FROM philosophers WHERE era = "BC"'
        bc_philosophers_result = db_cursor.execute(bc_philosophers_query)
        bc_philosophers = {row[0] for row in bc_philosophers_result}

    # Iterate through the rows and add nodes and edges to the graph
    for name, influences in rows:
        G.add_node(name)
        
        # Parse the 'influences' column and add edges if there are influences
        influence_list = influences.split(', ')
        for influence in influence_list:
            if influence.strip() and influence not in bc_philosophers:
                G.add_edge(influence, name)

    # Close the database connection
    db_connection.close()

    return G


def calculate_edge_weights(G):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        for u, v in G.edges():
            cursor.execute('SELECT attributes FROM philosophers WHERE name = ? OR name = ?', (u, v))
            rows = cursor.fetchall()

            if len(rows) == 2:
                attributes_u, attributes_v = rows
                attributes_u, attributes_v = attributes_u[0], attributes_v[0]
            elif len(rows) == 1:
                attributes_u = attributes_v = rows[0][0]
            else:
                attributes_u = attributes_v = ""

            if attributes_u and attributes_v:
                philosopher_attributes = set(attributes_u.split(', '))
                influencer_attributes = set(attributes_v.split(', '))
                shared_attributes = philosopher_attributes.intersection(influencer_attributes)
                edge_weight = len(shared_attributes) / max(len(philosopher_attributes), len(influencer_attributes))
                G[u][v]["weight"] = edge_weight

    return G


def calculate_node_weights():
    node_weights = {}
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT name, influences FROM philosophers')
        rows = cursor.fetchall()
        philosopher_influences = {name: influences.split(', ') for name, influences in rows}

        for philosopher in philosopher_influences:
            node_weight = sum(1 for influences in philosopher_influences.values() if philosopher in influences)
            node_weights[philosopher] = node_weight

    return node_weights


def json_format_dict(G, node_weights, partition):
    
    pos = nx.spring_layout(G, seed=42)  # Calculate the spring layout
    colors = px.colors.qualitative.Set1
    size_scaling_factor = 2

    # Create a dictionary for nodes with x, y coordinates, color, and size
    nodes = [
        {
            "id": node,
            "x": pos[node][0],
            "y": pos[node][1],
            "color": colors[partition[node] % len(colors)],
            "size": node_weights.get(node, 1) * size_scaling_factor if node_weights.get(node, 1) > 0 else size_scaling_factor
        }
        for node in G.nodes()
    ]

    # Create a list of links
    links = [{"source": edge[0], "target": edge[1]} for edge in G.edges()]

    graph_data = {
        "nodes": nodes,
        "links": links
    }

    return graph_data


def perform_community_detection(G):
    G = G.to_undirected()
    partition = community.best_partition(G)
    return partition