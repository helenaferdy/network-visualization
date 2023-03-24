from pyvis.network import Network

s
net = Network()

# add nodes
net.add_node(1, label="Node 1")
net.add_node(2, label="Node 2")
net.add_node(3, label="Node 3")
net.add_node(4, label="Node 4")
net.add_edges([(1,2)])
net.add_edges([(1,3)])
net.add_edges([(1,4)])
net.add_edges([(2,1)])
net.add_edges([(2,3)])
net.add_edges([(1,4)])

# show the network
net.show("index.html")

from IPython.core.display import display, HTML
display(HTML("index.html"))