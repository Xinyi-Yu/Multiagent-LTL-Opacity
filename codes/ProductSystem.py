# -*- coding: utf-8 -*-

from networkx.classes.digraph import DiGraph
from discrete_plan import dijkstra_plan_networkX


class ProductSystem(DiGraph):
	def __init__(self, MulLabelingGTS, A):
		DiGraph.__init__(self, MulLabelingGTS=MulLabelingGTS, A=A, initial=set(), label=set(), accept=set())

	def Product(self):
		# Construct nodes and transitions
		for mul_labeling_node in self.graph['MulLabelingGTS']:
			for node_A in self.graph['A']:
				node_prod = self.Composition_Prod(mul_labeling_node, node_A)
				for mul_labeling_node_t in self.graph['MulLabelingGTS'].successors(mul_labeling_node):
					for node_A_t in self.graph['A'].successors(node_A):
						label = self.graph['MulLabelingGTS'].node[mul_labeling_node_t]['label']
						truth = self.graph['A'].edges[node_A, node_A_t]['guard'].check(label[0] | label[1])     # check_transition_label_for_A_1
						cost = self.graph['MulLabelingGTS'][mul_labeling_node][mul_labeling_node_t]['weight']
						if truth:
							node_prod_t = self.Composition_Prod(mul_labeling_node_t, node_A_t)
							self.add_edge(node_prod, node_prod_t, weight=cost)
		return self

	def Composition_Prod(self, mul_labeling_node, node_A):
		node_prod = (mul_labeling_node, node_A)
		if not self.has_node(node_prod):
			self.add_node(node_prod, MulLabelingGTS=mul_labeling_node, A=node_A)
			if (mul_labeling_node in self.graph['MulLabelingGTS'].graph['initial']) and (node_A in self.graph['A'].graph['initial']):
				self.graph['initial'].add(node_prod)
			if node_A in self.graph['A'].graph['accept']:
				if (mul_labeling_node[0][1] == 1) and (mul_labeling_node[0][2] == 0) and (mul_labeling_node[1][1] == 0) and (mul_labeling_node[2][2] == 1):
					self.graph['accept'].add(node_prod)
		return node_prod

	def optimal(self):
		self.run = dijkstra_plan_networkX(self)
		if self.run == None:
			print '---No valid has been found!---'
			return

		print '------------------------------'
		print 'the prefix of plan **states**:'
		print [n for n in self.run[0]]
		print 'the suffix of plan **states**:'
		print [n for n in self.run[2]]
		print '------------------------------'

		print "=================The final plan is:"
		print "Prefix:"
		for node in self.run[0]:
			print node[0][0]
		print "Suffix:"
		for node in self.run[2]:
			print node[0][0]







