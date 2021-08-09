# -*- coding: utf-8 -*-


from networkx import dijkstra_predecessor_and_distance, single_source_dijkstra
import time


def dijkstra_plan_networkX(product):
	start = time.time()
	runs = {}
	loop = {}
	# minimal circles
	for prod_target in product.graph['accept']:
		if prod_target in product.predecessors(prod_target):
			loop[prod_target] = (product.edges[prod_target,prod_target]["weight"], [prod_target, prod_target])
			continue
		else:
			cycle = {}
			loop_pre, loop_dist = dijkstra_predecessor_and_distance(product, prod_target)
			for target_pred in product.predecessors(prod_target):
				if target_pred in loop_dist:
					sufcost_target_pred, suffix_target_pred = single_source_dijkstra(product, prod_target, target_pred)
					cycle[target_pred] = (product.edges[target_pred, prod_target]["weight"] + sufcost_target_pred, suffix_target_pred)
				if cycle:
					opti_pred = min(cycle, key=cycle.get)
					sufcost = cycle[opti_pred][0]
					suffix = cycle[opti_pred][1]
					loop[prod_target] = (sufcost, suffix)

	# shortest line
	for prod_init in product.graph['initial']:
		line_pre, line_dist = dijkstra_predecessor_and_distance(product, prod_init)
		for target in loop.iterkeys():   # check whether the system can start from prod_init to the loop
			if target in line_dist:
				precost, prefix = single_source_dijkstra(product, prod_init, target)
				suffix = loop[target][1]
				sufcost = loop[target][0]
				runs[(prod_init, target)] = (prefix, precost, suffix, sufcost)

	# best combination
	if runs:
		prefix, precost, suffix, sufcost = min(runs.values(), key=lambda p: 0.5*p[1] + 0.5*p[3])
		run_prefix_g_twin = [product.node[node]['MulLabelingGTS'] for node in prefix]
		run_suffix_g_twin = [product.node[node]['MulLabelingGTS'] for node in suffix]
		run = (run_prefix_g_twin, precost, run_suffix_g_twin, sufcost)
		print '=================='
		print 'Dijkstra_plan_networkX done within %.2fs: precost %.2f, sufcost %.2f' %(time.time()-start, precost, sufcost)
		return run
	print '=================='        
	print 'No accepting run found in optimal planning!'
	return None


