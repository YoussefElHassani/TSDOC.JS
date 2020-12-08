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

  for message in error_messages:
      message = message.split()
      # add the messages as nodes in the graph
      graph.add_nodes_from(message)
      
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

  # Count number of occurences for edges
  edges_weights = dict(Counter(edges_list))

  # Adding weight information to the graph
  nx.set_edge_attributes(graph, values = edges_weights, name = 'weight')

  return graph

def draw_graph(graph, title):
      # Specifying graph layout
  pos = graphviz_layout(graph, prog='dot')
  # Setting figure size
  fig = plt.figure(figsize=(20,20))
  ax = plt.subplot(111)
  # Set title
  ax.set_title(title, fontsize=10)

  # extracting weights information
  edges = graph.edges()
  weights = [graph[u][v]['weight']/10 for u,v in edges]

  nx.draw(graph,
          pos=pos,
          with_labels=True,
          node_color='lightgreen',
          ax=ax)
  plt.savefig(title+".png", format="PNG")
  plt.show()
    
  #edge_labels = nx.get_edge_attributes(graph,'weight')
  # nx.draw_networkx_edge_labels(graph, pos, edge_labels)





