from pyvis.network import Network
import csv
import os

CSV_PATH = 'device.csv'

class Device:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        self.neighbor = []

    def add_neighbor(self, neighbor_description):
        self.neighbor.append(neighbor_description)

# Check that the CSV file exists
if not os.path.isfile(CSV_PATH):
    print(f"Error: {CSV_PATH} does not exist")
    exit()

# Read CSV file
with open(CSV_PATH, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]

# Create devices and their neighbors
devices = {}
for d in data:
    source = d['source']
    target = d['target']
    weight = d['weight']
    neighbor_description = f"{d['int']} -> {target}\n"
    if source not in devices:
        devices[source] = Device(source, target, weight)
    else:
        devices[source].add_neighbor(neighbor_description)

# Create network
net = Network(height='1000px', width='100%', bgcolor='#222222', font_color='white')

# Add nodes and edges to the network
for source, device in devices.items():
    net.add_node(device.source, device.source, title=device.source)
    net.add_node(device.target, device.target, title=device.target)
    net.add_edge(device.source, device.target, value=device.weight)

# Add neighbor descriptions to node titles
for node in net.nodes:
    if node['id'] in devices:
        node['title'] = ''.join(devices[node['id']].neighbor)

# Show network in browser
net.show("index.html")
