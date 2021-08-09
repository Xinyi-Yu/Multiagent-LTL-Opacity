# -*- coding: utf-8 -*-

from wTS import MotionFts
from buchi import buchi_from_ltl
from GTS import GTS
from labelingGTS import labelingGTS
from MulLabelingGTS import MulLabelingGTS
from ProductSystem import ProductSystem
from Init import *
import time


time_start = time.time()

# Construct wTS for each robot T_i
T_1 = MotionFts(regions_1, init_1, 'T_1')
T_1.add_edges(edges)
T_2 = MotionFts(regions_2, init_2, 'T_2')
T_2.add_edges(edges)

# construct GTS T_g
GTS = GTS(T_1, T_2)
GTS = GTS.product()
print "the number of nodes in GTS is", len(GTS.nodes)
print "the number of edges in GTS is", len(GTS.edges)

# construct labeling-GTS \tilde{T}_g
labelingGTS = labelingGTS(GTS)
labelingGTS = labelingGTS.labeling(Secret_region)
print "the number of nodes in labelingGTS is", len(labelingGTS.nodes)
print "the number of edges in labelingGTS is", len(labelingGTS.edges)

# construct multiple-labeling-GTS V
MulLabelingGTS = MulLabelingGTS(labelingGTS)
MulLabelingGTS = MulLabelingGTS.Mul_3(H)
# To reduce computation complexity, we construct 3-labeling-GTS here instead of 5-labeling-GTS
# since we have already known there is only one robot visiting secret state
# and it is easy to change it to 5-labeling-GTS by changing "Mul_3" function in "MulLabelingGTS.py"
print "the number of nodes in MulLabelingGTS is", len(MulLabelingGTS.nodes)
print "the number of edges in MulLabelingGTS is", len(MulLabelingGTS.edges)

# convert LTL to automata
task = Task_exper
A = buchi_from_ltl(task, 'robot')
print "the number of nodes in automata A is", len(A.nodes)
print "the number of edges in automata A is", len(A.edges)

# Construct product system
ProductSystem = ProductSystem(MulLabelingGTS, A)
ProductSystem = ProductSystem.Product()
print "the number of nodes in Product System is", len(ProductSystem.nodes)
print "the number of edges in Product System is", len(ProductSystem.edges)
print "the initial state in Product System is", ProductSystem.graph['initial']
print "the number of the accepting nodes in product system is ", len(ProductSystem.graph['accept'])

# Find the optimal path
ProductSystem.optimal()

time_end = time.time()
print "Total time cost:", time_end - time_start


