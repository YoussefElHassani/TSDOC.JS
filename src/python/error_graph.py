import networkx as nx

path = 'test.txt'

# Initializing error messages list
error_messages = []

with open(path) as error_log:
    for line in error_log:
        # Removing the end of line character
        line = line.replace('\n', '')
        error_messages.append(line)

# Initialize graph
error_graph = nx.Graph()

"""
# tokenize error messages
for message in error_messages:
    message = message.split()
    
    # adding tokens to the graph
    
"""
print(len(error_messages))
print(error_messages[:5])

G=nx.Graph()

print(G.nodes())
print(G.edges())

print(type(G.nodes()))
print(type(G.edges()))


# adding just one node:
G.add_node("a")
G.add_node("a")

if "a" in G.nodes():
    G.add_node("mate")
# a list of nodes:
G.add_nodes_from(["b","c"])
G.add_node("a")


print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())
