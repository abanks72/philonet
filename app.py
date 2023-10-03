from flask import Flask, render_template, request, jsonify
from philosopher import create_philosopher_graph, calculate_edge_weights, calculate_node_weights, perform_community_detection, json_format_dict
import networkx as nx
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

# Create a new route to return JSON data
@app.route('/get_graph_json')
def get_graph_json():
    # Create the philosopher graph and calculate weights
    graph = create_philosopher_graph()
    graph = calculate_edge_weights(graph)
    weights = calculate_node_weights()
    partition = perform_community_detection(graph)
    
    # Convert the graph data into JSON format
    graph_data = json_format_dict(graph, weights, partition)
    
    # Use jsonify to return the JSON response
    return jsonify(graph_data)

@app.route('/test', methods=['GET'])
def test():
    return render_template('index.html')

@app.route('/process_dropdown', methods=['POST'])
def process_dropdown():
    selection = request.form.get('selection')  # Get the selected value from the form
    print(selection)  # Print the selected value to the command line
    # Process the selected value as needed

    if selection == "yes":
        return "Congratulations!"
    else:
        return "Awww"

if __name__ == '__main__':
    app.run(debug=True)






