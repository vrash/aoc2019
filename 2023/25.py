#!/usr/bin/python
# -*- coding: utf-8 -*-
import networkx as nx
filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 

graph = nx.Graph()

for line in open(filename):
    left, right = line.split(":")
    for node in right.strip().split():
        graph.add_edge(left,node)
#print(graph)

#print(nx.minimum_edge_cut(graph))
graph.remove_edges_from(nx.minimum_edge_cut(graph))
a,b = nx.connected_components(graph)
print(len(a)*len(b))