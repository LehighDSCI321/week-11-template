import subprocess
import re
import pytest

from student_code import SpanningTreeGraph

def test_spanning_tree_complex_graph():
    st = SpanningTreeGraph()
    nodes = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    for nd in nodes:
        st.add_node(nd)
    
    edges = [
        ("a", "b", 4), ("a", "h", 8), ("b", "h", 11), ("b", "c", 8),
        ("c", "d", 7), ("c", "f", 4), ("c", "i", 2), ("d", "e", 9),
        ("d", "f", 14), ("e", "f", 10), ("f", "g", 2), ("g", "h", 1),
        ("g", "i", 6), ("h", "i", 7)
    ]
    
    for start, end, weight in edges:
        st.add_edge(start, end, edge_weight=weight)
    
    P = st.spanning_tree("a")
    
    # Check that all nodes are in the spanning tree
    assert set(P.keys()) == set(nodes)
    
    # Check that the total weight of the spanning tree is minimal
    total_weight = sum(st.get_edge_weight(node, parent) for node, parent in P.items() if parent is not None)
    assert total_weight == 37  # The minimal total weight for this graph
    
    # Check that there are no cycles
    def has_cycle(parents):
        visited = set()
        for node in parents:
            current = node
            while current is not None:
                if current in visited:
                    return True
                visited.add(current)
                current = parents[current]
            visited.clear()
        return False
    
    assert not has_cycle(P)

