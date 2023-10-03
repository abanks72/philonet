import networkx as nx
import community, json, sqlite3
import plotly.graph_objs as go
import plotly.offline as pyo
import plotly.express as px
from philosopher_data import philosophers_data

def create_philosopher_graph():
    G = nx.DiGraph()

    # Connect to the database
    db_connection = sqlite3.connect('philosophers.db')
    db_cursor = db_connection.cursor()

    # Query the 'philosophers' table to get philosopher data
    db_cursor.execute('SELECT name, influences FROM philosophers')

    # Fetch all rows as a list of tuples
    rows = db_cursor.fetchall()

    # Iterate through the rows and add nodes and edges to the graph
    for name, influences in rows:

        G.add_node(name)

        # Parse the 'influences' column and add edges if there are influences
        influence_list = influences.split(', ')
        for influence in influence_list:
            if influence.strip():  # Check if the influence is not empty or whitespace
                G.add_edge(influence, name)

    # Close the database connection
    db_connection.close()

    return G

def calculate_edge_weights(G):

    # Connect to the database
    db_connection = sqlite3.connect('philosophers.db')
    db_cursor = db_connection.cursor()

    # Iterate through the edges in the graph
    for u, v in G.edges():
        # Query the database to get attributes for both philosophers
        db_cursor.execute('SELECT attributes FROM philosophers WHERE name = ? OR name = ?', (u, v))
        rows = db_cursor.fetchall()

        if len(rows) == 2:
            attributes_u, attributes_v = rows
            attributes_u, attributes_v = attributes_u[0], attributes_v[0]
        elif len(rows) == 1:
            attributes_u = attributes_v = rows[0][0]
        else:
            attributes_u = attributes_v = ""

        if attributes_u and attributes_v:
            # Parse and compare attributes to calculate edge weight
            philosopher_attributes = set(attributes_u.split(', '))
            influencer_attributes = set(attributes_v.split(', '))
            shared_attributes = philosopher_attributes.intersection(influencer_attributes)
            edge_weight = len(shared_attributes) / max(len(philosopher_attributes), len(influencer_attributes))
            G[u][v]["weight"] = edge_weight

    # Close the database connection
    db_connection.close()

    return G

def calculate_node_weights():
    node_weights = {}

    # Connect to the database
    db_connection = sqlite3.connect('philosophers.db')
    db_cursor = db_connection.cursor()

    # Query the 'philosophers' table to get philosopher names and influences
    db_cursor.execute('SELECT name, influences FROM philosophers')

    # Fetch all rows as a list of tuples
    rows = db_cursor.fetchall()

    # Create a dictionary to store the philosopher's influences
    philosopher_influences = {name: influences.split(', ') for name, influences in rows}

    # Iterate through the philosophers and calculate node weights
    for philosopher in philosopher_influences:
        node_weight = sum(1 for influences in philosopher_influences.values() if philosopher in influences)
        node_weights[philosopher] = node_weight

    # Close the database connection
    db_connection.close()

    return node_weights

def perform_community_detection(G):
    G = G.to_undirected()
    partition = community.best_partition(G)
    return partition

def visualize_network(G, node_weights, partition):
    pos = nx.spring_layout(G, seed=42)
    fig = go.Figure()
    colors = px.colors.qualitative.Set1
    size_scaling_factor = 2

    for node, (x, y) in pos.items():
        community_id = partition[node]
        node_color = colors[community_id % len(colors)]

        node_size = node_weights[node] * size_scaling_factor

        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode="markers",
            text=node,
            marker=dict(
                size=node_size,
                color=node_color,
                opacity=1,
            ),
            name=node,
        ))

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        fig.add_trace(go.Scatter(
            x=[x0, x1],
            y=[y0, y1],
            mode="lines",
            line=dict(width=.2, color="gray"),
        ))

    fig.update_layout(
        showlegend=True,
        hovermode="closest",
        title="Philosopher Influences with Weighted Edges Based on Shared Attributes and Community Detection",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
    )
    
    pyo.plot(fig, filename='plotly_visualization.html')

def json_format_dict(G, node_weights, partition):
    
    pos = nx.spring_layout(G, seed=42)  # Calculate the spring layout
    colors = px.colors.qualitative.Set1
    size_scaling_factor = 3

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

def json_dict_to_json(graph_data):
    json_data = json.dumps(graph_data, indent=4)

    # Save the JSON data to a file
    with open("philosopher_data_4.json", "w") as json_file:
        json_file.write(json_data)

def filter_data_by_era(data, era):

    filtered_data = {}
    for philosopher, details in data.items():
        philosopher_era = details.get("Era")
        if era == "All" or philosopher_era == era:
            filtered_details = details.copy()  # Create a copy of the philosopher's details
            filtered_influences = [influence for influence in filtered_details.get("Influences", []) if data.get(influence, {}).get("Era") == era]
            filtered_details["Influences"] = filtered_influences  # Update the influences based on the selected era
            filtered_data[philosopher] = filtered_details

    return filtered_data

def filter_data_by_year_range(data, start_year, end_year):
    filtered_data = {}

    for philosopher, details in data.items():
        philosopher_year = details.get("Year")
        if start_year <= philosopher_year <= end_year:
            filtered_details = details.copy()
            filtered_influences = [influence for influence in filtered_details.get("Influences", []) if start_year <= data.get(influence, {}).get("Year") <= end_year]
            filtered_details["Influences"] = filtered_influences
            filtered_data[philosopher] = filtered_details

    return filtered_data

def process_philosopher_data(data):
    graph = create_philosopher_graph(data)
    graph = calculate_edge_weights(graph, data)
    node_weights = calculate_node_weights(data)
    partition = perform_community_detection(graph)

    print_communities(partition)

    visualize_network(graph, node_weights, partition)

def print_communities(partition):
        # Create a dictionary to group nodes by community
    communities = {}
    for node, community_id in partition.items():
        if community_id not in communities:
            communities[community_id] = []
        communities[community_id].append(node)
    
    # Print the communities
    for community_id, nodes in communities.items():
        print(f"Community {community_id + 1}: {', '.join(nodes)}")

def database_populate(data):
        # Create an SQLite database file (if it doesn't exist)
    db_connection = sqlite3.connect('my_database.db')
    db_cursor = db_connection.cursor()

    # Create a table for nodes
    db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY,
            node_id TEXT,
            x REAL,
            y REAL,
            color TEXT,
            size REAL
        )
    ''')

    # Create a table for edges
    db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS edges (
            id INTEGER PRIMARY KEY,
            source_node_id TEXT,
            target_node_id TEXT,
            FOREIGN KEY (source_node_id) REFERENCES nodes (node_id),
            FOREIGN KEY (target_node_id) REFERENCES nodes (node_id)
        )
    ''')

    # Insert data into the nodes table
    for node in data["nodes"]:
        db_cursor.execute('''
            INSERT INTO nodes (node_id, x, y, color, size)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            node["id"],
            node["x"],
            node["y"],
            node["color"],
            node["size"]
        ))

    # Insert data into the edges table
    for edge in data["links"]:
        db_cursor.execute('''
            INSERT INTO edges (source_node_id, target_node_id)
            VALUES (?, ?)
        ''', (
            edge["source"],
            edge["target"]
        ))

    # Commit the changes and close the database connection
    db_connection.commit()
    db_connection.close()

def main():

    graph = create_philosopher_graph()
    graph = calculate_edge_weights(graph)
    weights = calculate_node_weights()
    partition = perform_community_detection(graph)

    visualize_network(graph, weights, partition)
        
if __name__ == "__main__":
    main()