from flask import Flask, render_template, request, jsonify
from philosopher import create_philosopher_graph, calculate_edge_weights, calculate_node_weights, perform_community_detection, json_format_dict, create_philosopher_graph_test
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Create a new route to return JSON data
@app.route('/get_graph_json')
def get_graph_json():
    selected_era = request.args.get('era', 'All')  # Get the selected era from the query parameter

    # Create the philosopher graph based on the selected era and calculate weights
    graph = create_philosopher_graph_test(selected_era)
    graph = calculate_edge_weights(graph)
    weights = calculate_node_weights()
    partition = perform_community_detection(graph)
    
    # Convert the graph data into JSON format
    graph_data = json_format_dict(graph, weights, partition)
    
    # Use jsonify to return the JSON response
    return jsonify(graph_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)










