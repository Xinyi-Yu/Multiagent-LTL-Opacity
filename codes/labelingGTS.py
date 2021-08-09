# -*- coding: utf-8 -*-

from networkx.classes.digraph import DiGraph

class labelingGTS(DiGraph):
	def __init__(self, GTS):
		DiGraph.__init__(self, GTS=GTS, initial=set(), label=set())

	def labeling(self, secret):
		# construct initial nodes in labelingGTS
		labeling_init_node = self.label_init_node(secret)
		# construct nodes and transitions
		self.composition_label(secret, labeling_init_node)
		return self

	def composition_label(self, secret, initial_node):
		set_itera_old = [initial_node]
		flag_while = 0
		while flag_while < 5:
			# If five consecutive iterations do not produce a new transition, we consider the construction is finished
			set_itera_new = []
			for (node_g, a_1, a_2) in set_itera_old:
				labeling_node = (node_g, a_1, a_2)
				for node_g_t in self.graph['GTS'].successors(node_g):
					if node_g_t[0] in secret:
						a_1_t = 1
					else:
						a_1_t = a_1
					if node_g_t[1] in secret:
						a_2_t = 1
					else:
						a_2_t = a_2
					labeling_node_t = (node_g_t, a_1_t, a_2_t)
					if labeling_node_t not in self.nodes:
						label = self.graph['GTS'].node[node_g_t]['label']
						self.add_node(labeling_node_t, label=label)
						set_itera_new.append(labeling_node_t)
					if (labeling_node, labeling_node_t) not in self.edges:
						cost = self.graph['GTS'][node_g][node_g_t]['weight']
						self.add_edge(labeling_node, labeling_node_t, weight=cost)
			if set_itera_new == []:
				flag_while = flag_while + 1
			set_itera_old = set_itera_new



	def label_init_node(self, secret):
		for node_g in self.graph['GTS'].graph['initial']:
			a_1 = 0
			a_2 = 0
			if node_g[0] in secret:
				a_1 = 1
			if node_g[1] in secret:
				a_2 = 1
			labeling_node = (node_g, a_1, a_2)
			label = self.graph['GTS'].node[node_g]['label']
			self.add_node(labeling_node, label=label)
			self.graph['initial'].add(labeling_node)
		return labeling_node



