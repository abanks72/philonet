from flask import Blueprint, render_template, request, jsonify
from app.services.philosopher import (create_philosopher_graph, calculate_edge_weights,
                                      calculate_node_weights, perform_community_detection, 
                                      json_format_dict, create_philosopher_graph_test)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/get_graph_json')
def get_graph_json():
    selected_era = request.args.get('era', 'All')
    graph = create_philosopher_graph_test(selected_era)
    graph = calculate_edge_weights(graph)
    weights = calculate_node_weights()
    partition = perform_community_detection(graph)
    graph_data = json_format_dict(graph, weights, partition)
    return jsonify(graph_data)
