# -*- coding: utf-8 -*-


# map information
regions_1 = {'A': set(['a1']), 'F': set(['f1']),
             'E': set(['e1']), 'H': set(['h1']),
             'B': set(['b1']), 'G': set(['g1']),
             'C': set(['c1']), 'D': set(['d1']),
             }
regions_2 = {'A': set(['a2']), 'F': set(['f2']),
             'E': set(['e2']), 'H': set(['h2']),
             'B': set(['b2']), 'G': set(['g2']),
             'C': set(['c2']), 'D': set(['d2']),
             }
edges = [('A', 'F', 1), ('A', 'B', 2), ('B', 'F', 2), ('B', 'C', 2), ('C', 'D', 1), ('D', 'H', 2), ('D', 'G', 2),
         ('E', 'F', 2), ('F', 'G', 2)]

# Output function   (To avoid confusion, we use double letters to denote the output result)
H = {'A': 'GG', 'F': 'GG',
     'E': 'PP', 'H': 'PP',
     'B': 'RR', 'G': 'RR',
     'C': 'BB', 'D': 'BB',
     }

# initial position
init_1 = ['A']
init_2 = ['E']

# secret region
Secret_region = ['B']

# LTL task
Task_exper = '(!c1 U b1)  && ([]<>c1) && ([]<>d2)'
