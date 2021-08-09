# -*- coding: utf-8 -*-

from networkx.classes.digraph import DiGraph

class MulLabelingGTS(DiGraph):
	def __init__(self, labelingGTS):
		DiGraph.__init__(self, labelingGTS=labelingGTS, initial=set(), label=set())

	def Mul_2(self, H):
		# construct initial state
		for labeling_node_1 in self.graph['labelingGTS'].graph['initial']:
			for labeling_node_2 in self.graph['labelingGTS'].graph['initial']:
				if self.H(labeling_node_1, H) == self.H(labeling_node_2, H):
					mul_labeling_node = self.composition_2(labeling_node_1, labeling_node_2)
					self.graph['initial'].add(mul_labeling_node)

		# Construct nodes and transitions
		for labeling_node_1 in self.graph['labelingGTS'].nodes:
			for labeling_node_2 in self.graph['labelingGTS'].nodes:
				if self.H(labeling_node_1, H) == self.H(labeling_node_2, H):
					mul_labeling_node = self.composition_2(labeling_node_1, labeling_node_2)
					for labeling_node_1_t in self.graph['labelingGTS'].successors(labeling_node_1):
						for labeling_node_2_t in self.graph['labelingGTS'].successors(labeling_node_2):
							if self.H(labeling_node_1_t, H) == self.H(labeling_node_2_t, H):
								mul_labeling_node_t = self.composition_2(labeling_node_1_t, labeling_node_2_t)
								cost = self.graph['labelingGTS'][labeling_node_1][labeling_node_1_t]['weight']
								self.add_edge(mul_labeling_node, mul_labeling_node_t, weight=cost)
		return self

	def composition_2(self, labeling_node_1, labeling_node_2):
		mul_labeling_node = (labeling_node_1, labeling_node_2)
		if not self.has_node(mul_labeling_node):
			label = self.graph['labelingGTS'].node[labeling_node_1]['label']
			self.add_node(mul_labeling_node, label=label)
		return mul_labeling_node


	def Mul_3(self, H):
		# construct initial state
		for labeling_node_1 in self.graph['labelingGTS'].graph['initial']:
			for labeling_node_2 in self.graph['labelingGTS'].graph['initial']:
				for labeling_node_3 in self.graph['labelingGTS'].graph['initial']:
					if self.H(labeling_node_1, H) == self.H(labeling_node_2, H) == self.H(labeling_node_3, H):
						mul_labeling_node = self.composition_3(labeling_node_1, labeling_node_2, labeling_node_3)
						self.graph['initial'].add(mul_labeling_node)

		# Construct nodes and transitions
		for labeling_node_1 in self.graph['labelingGTS'].nodes:
			for labeling_node_2 in self.graph['labelingGTS'].nodes:
				for labeling_node_3 in self.graph['labelingGTS'].nodes:
					if self.H(labeling_node_1, H) == self.H(labeling_node_2, H) == self.H(labeling_node_3, H):
						mul_labeling_node = self.composition_3(labeling_node_1, labeling_node_2, labeling_node_3)
						for labeling_node_1_t in self.graph['labelingGTS'].successors(labeling_node_1):
							for labeling_node_2_t in self.graph['labelingGTS'].successors(labeling_node_2):
								for labeling_node_3_t in self.graph['labelingGTS'].successors(labeling_node_3):
									if self.H(labeling_node_1_t, H) == self.H(labeling_node_2_t, H) == self.H(labeling_node_3_t, H):
										mul_labeling_node_t = self.composition_3(labeling_node_1_t, labeling_node_2_t, labeling_node_3_t)
										cost = self.graph['labelingGTS'][labeling_node_1][labeling_node_1_t]['weight']
										self.add_edge(mul_labeling_node, mul_labeling_node_t, weight=cost)
		return self

	def composition_3(self, labeling_node_1, labeling_node_2, labeling_node_3):
		mul_labeling_node = (labeling_node_1, labeling_node_2, labeling_node_3)
		if not self.has_node(mul_labeling_node):
			label = self.graph['labelingGTS'].node[labeling_node_1]['label']
			self.add_node(mul_labeling_node, label=label)
		return mul_labeling_node

	def H(self, labeling_node, H):
		H_1 = H[ labeling_node[0][0] ]
		H_2 = H[ labeling_node[0][1] ]
		node_g_labeling_H = (H_1, H_2)
		return node_g_labeling_H

