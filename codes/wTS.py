# -*- coding: utf-8 -*-


from networkx.classes.digraph import DiGraph

class MotionFts(DiGraph):
    def __init__(self, node_dict, init_node, ts_type):
        DiGraph.__init__(self, type=ts_type, initial=set())
        for (n, label) in node_dict.iteritems():
            self.add_node(n, label=label)
            if n in init_node:
                self.graph['initial'].add(n)
            
    def add_edges(self, edge_list):   # it is different from self.add_edge
        for edge in edge_list:
            node_1 = edge[0]
            node_2 = edge[1]
            cost = edge[2]
            self.add_edge(node_1, node_2, weight=cost)
            self.add_edge(node_2, node_1, weight=cost)
        for node in self.nodes():
            self.add_edge(node, node, weight=0.01)






