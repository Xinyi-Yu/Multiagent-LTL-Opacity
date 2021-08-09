# -*- coding: utf-8 -*-

from ltl2ba import run_ltl2ba
from promela import parse as parse_ltl, find_states, find_symbols
from parser import parse as parse_guard
from networkx.classes.digraph import DiGraph


def buchi_from_ltl(formula, Type):
    promela_string = run_ltl2ba(formula)
    symbols = find_symbols(formula)
    edges = parse_ltl(promela_string)   # It is a dict
    (states, initials, accepts) = find_states(edges)
    buchi = DiGraph(type=Type, initial=initials, accept=accepts, symbols=symbols)
    for state in states:
        buchi.add_node(state)
    for (ef, et) in edges.keys():
        guard_formula = edges[(ef, et)]
        guard_expr = parse_guard(guard_formula)
        buchi.add_edge(ef, et, guard=guard_expr, guard_formula=guard_formula)      # guard_formula is a word which can induce ef to et
    return buchi


