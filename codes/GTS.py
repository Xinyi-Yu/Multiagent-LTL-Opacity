# -*- coding: utf-8 -*-

from networkx.classes.digraph import DiGraph

class GTS(DiGraph):
	def __init__(self, T_1, T_2):
		DiGraph.__init__(self, ts1=T_1, ts2=T_2, initial=set(), label=set())

	def product(self):
		for node_ts1 in self.graph['ts1'].nodes():
			for node_ts2 in self.graph['ts2'].nodes():
				node_g = self.composition_node(node_ts1, node_ts2)
				for node_ts1_t in self.graph['ts1'].successors(node_ts1):
					for node_ts2_t in self.graph['ts2'].successors(node_ts2):
						node_g_t = self.composition_node(node_ts1_t, node_ts2_t)
						cost = self.graph['ts1'][node_ts1][node_ts1_t]['weight'] + self.graph['ts2'][node_ts2][node_ts2_t]['weight']
						self.add_edge(node_g, node_g_t, weight=cost)
		return self

	def composition_node(self, node_ts1, node_ts2):
		node_g = (node_ts1, node_ts2)
		if not self.has_node(node_g):
			label = (self.graph['ts1'].node[node_ts1]['label'], self.graph['ts2'].node[node_ts2]['label'])
			self.add_node(node_g, ts1=node_ts1, ts2=node_ts2, label=label)
			if ((node_ts1 in self.graph['ts1'].graph['initial']) and (node_ts2 in self.graph['ts2'].graph['initial'])):
				self.graph['initial'].add(node_g)
		return node_g




