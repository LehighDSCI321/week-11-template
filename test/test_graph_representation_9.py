import subprocess
import re
import pytest

from student_code import SpanningTreeGraph,VersatileDigraph

def test_class_structure():
    st = SpanningTreeGraph()
    
    # Check inheritance
    assert isinstance(st, VersatileDigraph)
    
    # Check overridden methods
    overridden_methods = [method for method in dir(SpanningTreeGraph) 
                          if callable(getattr(SpanningTreeGraph, method)) 
                          and method in ['__init__', 'add_edge']]
    assert set(overridden_methods) == {'__init__', 'add_edge'}
    
    # Check for additional methods
    additional_methods = [method for method in dir(SpanningTreeGraph) 
                          if callable(getattr(SpanningTreeGraph, method)) 
                          and not method.startswith('__') 
                          and method not in dir(VersatileDigraph)]
    assert 'dfs' in additional_methods 
    assert 'bfs' in additional_methods 