import networkx as nx
import numpy as np
import random

class WarehouseGraph:
    def __init__(self, num_zones=10):
        self.G = nx.DiGraph()
        self.build_graph(num_zones)
    
    def build_graph(self, num_zones):
        # Nodes: Zones for pallet (P1-P3), case (C1-C4), eaches (E1-E3)
        zones = [f'P{i}' for i in range(1, 4)] + [f'C{i}' for i in range(1, 5)] + [f'E{i}' for i in range(1, 4)]
        self.G.add_nodes_from(zones)
        
        # Edges: Modular paths with weights (travel time in mins)
        paths = [
            ('P1', 'C1', {'weight': 2, 'capacity': 50}),  # Pallet to case
            ('P1', 'C2', {'weight': 3, 'capacity': 40}),
            ('C1', 'E1', {'weight': 1, 'capacity': 30}),
            ('C2', 'E2', {'weight': 1.5, 'capacity': 25}),
            # Add more for full pallet-case-eaches coverage...
            ('P3', 'C4', {'weight': 4, 'capacity': 60}),
            ('C4', 'E3', {'weight': 2, 'capacity': 35})
        ]
        self.G.add_edges_from([(u, v, attr) for u, v, attr in paths])
    
    def simulate_failure(self, failure_rate=0.05):
        """Risk assessment: Randomly fail edges (e.g., AGV downtime)"""
        for edge in list(self.G.edges):
            if random.random() < failure_rate:
                self.G[edge[0]][edge[1]]['failed'] = True
                self.G[edge[0]][edge[1]]['weight'] *= 2  # Slower on failure
    
    def shortest_paths(self, source='P1', target='E3'):
        return dict(nx.all_shortest_paths(self.G, source, target, weight='weight'))
