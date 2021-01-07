import matplotlib.pyplot as plt
import networkx as nx

from networkx.drawing.nx_agraph import graphviz_layout
from collections import Counter


def construct_graph(error_messages):
    """ This function constructs a networkx graph from error messages tokens
    """
    graph = nx.DiGraph()
    messages_list = []
    edges_list = []

    graph = nx.DiGraph()
    messages_list = []
    edges_list = []
    nodes_list = []

    for message in error_messages:
        message = message.split()
        # add the messages as nodes in the graph
        nodes_list += message

        # Preprocessing the tokens list to egde tuples (a, b, c) -> (a,b), (b,c)
        edges = []
        for i in range(0, len(message), 2):
          if i < len(message)-1:
            edges.append((message[i], message[i+1]))
          if i < len(message)-2:
            edges.append((message[i+1], message[i+2]))
        messages_list.append(message)
        edges_list += edges

    # Adding edges to the graph with their respective weights
    graph.add_edges_from(edges_list)
    # Adding nodes to the graph with their respective weights
    graph.add_nodes_from(nodes_list)

    # Count number of occurences for edges
    edges_weights = dict(Counter(edges_list))
    # Count number of occurences for nodes
    nodes_weights = dict(Counter(nodes_list))

    # Adding weight information to the graph
    nx.set_edge_attributes(graph, values = edges_weights, name = 'weight')
    nx.set_node_attributes(graph, values = nodes_weights, name = 'weight')
    return graph

def draw_graph(graph, title):
    # Specifying graph layout
    pos = graphviz_layout(graph, prog='dot')
    # Setting figure size
    fig = plt.figure(figsize=(50,20))
    ax = plt.subplot(111)
    # Set title
    ax.set_title(title, fontsize=18)

    # extracting weights information
    edges = graph.edges()

    nx.draw(graph,
          pos=pos,
          with_labels=True,
          node_color='lightgreen',
          ax=ax)
    edge_labels = nx.get_edge_attributes(graph,'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels, font_size=14)
    plt.savefig("fig/" + title + ".png", format="PNG")
    plt.show()


def allocate_variable_layout(before, after, dictionary):
    variable_node = None
    # Find next available variable
    for key,value in dictionary.items():
        # Once found, change its availability flag
        if value['available'] == True:
            variable_node = key
            value['before'] = before
            value['after'] = after
            value['occurence'] = 1 
            value['available'] = False
            break
    # Return the dictionary
    return key, dictionary

def delete_empty_layouts(dictionary):
    keys = []
    # Find unalocated nodes
    for key,value in dictionary.items():
        if value['available'] == True:
            keys.append(key)
            continue
    # Proceed to delete those
    for key in keys:
        dictionary.pop(key, None)
    # Return the dictionary
    return dictionary

def search_layouts(before, after, dictionary):
    for key,value in dictionary.items():
        if value['before'] == before and value['after'] == after:
            return key
    return 'LAYOUT NOT FOUND'
        
def replace_node_by_var_list(node, variable, nodes_list):
    new_list = []
    for element in nodes_list:
        if element == node:
            new_list.append(variable)
        else:
            new_list.append(element)
    return new_list

def replace_node_by_var_tuples(node, variable, tuples_list):
    new_list = []
    for node1, node2 in tuples_list:
        if node == node1:
            new_list.append(variable, node2)
        elif node == node2:
            new_list.append(node1, variable)
        else:
            new_list.append(node1, node2)
    return new_list

def update_dictionary(node, variable, dictionary):
    for key, value in dictionary.items():
        value['before'] = replace_node_by_var_list(node, variable, value['before'])
        value['after'] = replace_node_by_var_list(node, variable, value['after'])
    return dictionary


def preprocess_graph(G, threshold):
    # identify variable nodes in graph
    variable_nodes = set()
    for node, data in G.nodes(data=True):
        if data['weight'] <= threshold:
            variable_nodes.add(node)

    # identify variable edges in graph
    variable_edges = set()
    for node1, node2 in G.edges:
        if node1 in variable_nodes or node2 in variable_nodes:
            variable_edges.add((node1, node2))

    # add dictionary edge tracker where the before and after nodes are stored
    edges_layout = {}

    # create a variable node
    variable_count = 0
    # variable tracker
    var_tracker = {}
    # Initialise variable nodes layout tracker# variable tracker
    for count in range(0,len(variable_nodes)):
        # Declare variable node
        variable_node = 'var_' + str(variable_count)
        # adding the variable_node to the dictionary edges_layout
        if variable_node not in edges_layout:
            keys = ['before', 'after']
            edges_layout[variable_node] = {key: [] for key in keys}
            edges_layout[variable_node]['available'] = True
            var_tracker[variable_node] = []
        variable_count += 1
    # Once layouts are captured, it is time to create the new edge list that needs to be modified
    edges_to_remove = variable_edges
    nodes_to_remove = []
    edges_to_add = []
    nodes_to_add = []

    for node in variable_nodes:
        before = []
        after = []
        # Finding tuples where the variable node is defined
        tuple_result = filter(lambda x: x[0] == node or x[1] == node, G.edges)

        for tuple_node_1, tuple_node_2 in tuple_result:
            if node == tuple_node_1:
                after.append(tuple_node_2)
            elif node == tuple_node_2:
                before.append(tuple_node_1)
        # Search for the layout
        variable = search_layouts(before, after, edges_layout)
        # If the layout does not exist, return
        if variable == 'LAYOUT NOT FOUND':
            variable, edges_layout = allocate_variable_layout(before, after, edges_layout)

        var_tracker[variable].append(node)
        nodes_to_remove.append(node)
        # Creating the edges to be added
        for node_after in after:
            edges_to_add.append((variable, node_after))
        for node_before in before:
            edges_to_add.append((node_before, variable))

        # Updating the dictionary layout
        edges_layout = update_dictionary(node, variable, edges_layout)
    # Removing unnecessary keys
    edges_layout = delete_empty_layouts(edges_layout)
    # Assigning the nodes to be added list
    nodes_to_add = list(edges_layout.keys())

    # Aggregating node weights
    nodes_to_remove = var_tracker
    var_counter = {}
    for key, value in var_tracker.items():
        var_counter[key] = 0
        for node in value:
            var_counter[key] += G.nodes[node]['weight']

    # Remove variable nodes
    G.remove_edges_from(edges_to_remove)
    G.remove_nodes_from(nodes_to_remove)

    # Adding weights to nodes
    nodes_to_add_meta = []
    for node in nodes_to_add:
        weight = var_counter[node]
        nodes_to_add_meta.append((node,dict({'weight': weight})))
    # Add new nodes
    G.add_nodes_from(nodes_to_add_meta)

    leaf_nodes = [x for x in G.nodes() if G.out_degree(x)==0 and G.in_degree(x)> 0]
    root_nodes = [x for x in G.nodes() if G.out_degree(x) > 0 and G.in_degree(x)==0]
    
    # Adding weights to the edges
    for before, after in edges_to_add:
        if before in root_nodes:
            G.add_edge(before, after, weight = G.nodes[after]["weight"])
            continue
        if after in leaf_nodes:
            G.add_edge(before, after, weight = G.nodes[after]["weight"])
            continue
        if G.out_degree(before) < G.in_degree(after):
            G.add_edge(before, after, weight = G.nodes[before]["weight"])
            continue
        if G.out_degree(before) > G.in_degree(after):
            G.add_edge(before, after, weight = G.nodes[after]["weight"])
            continue
        if G.out_degree(before) == G.in_degree(after):
            minimum_weight = min([G.nodes[before]["weight"], G.nodes[after]["weight"]])
            G.add_edge(before, after, weight = minimum_weight)
            continue
        G.add_edge(before, after, weight = 999999)
    
    # Removing nodes with 0 degress
    remove = [node for node,degree in dict(G.degree()).items() if degree == 0]
    G.remove_nodes_from(remove)

    return G


