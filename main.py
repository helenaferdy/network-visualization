from pyvis.network import Network
import pandas as pd
import csv
from device import Device

CSV_PATH = 'device.csv'

net = Network(height='1000px', width='100%', bgcolor='#222222', font_color='white')
# net.show_buttons(filter_=['nodes'])

#open csv
with open(CSV_PATH, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]

#initialize object
devices = []
for d in data:
    new_d = Device(
        d['source'],
        d['target'],
        d['weight']
    )
    devices.append(new_d)

#initialize object's neighbor
for d in data:
    for dd in devices:
        if d['source'] == dd.source:
            new_neigh = []
            new_neigh.append(d['int']+' -> ')
            new_neigh.append(d['target']+'\n')
            dd.add_neighbor(new_neigh)

#create node
for dd in devices:
    net.add_node(dd.source, dd.source, title=dd.source)
    net.add_node(dd.target, dd.target, title=dd.target)
    net.add_edge(dd.source, dd.target, value=dd.weight)

#add neighbor description
for node in net.nodes:
    for dd in devices:
        if node['id'] == dd.source and node['title'] == dd.source:
            node['title'] = ""
            for n in dd.neighbor:
                for nn in n:
                    node['title'] += nn



net.show("index.html")
