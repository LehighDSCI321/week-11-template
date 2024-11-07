import subprocess
import re
import pytest

from student_code import SpanningTreeGraph

def test_spanning_tree_output():
    st = SpanningTreeGraph()
    nodes = ["a", "b", "c", "d"]
    for nd in nodes:
        st.add_node(nd)
    st.add_edge("a", "b", edge_weight=1)
    st.add_edge("b", "c", edge_weight=2)
    st.add_edge("c", "d", edge_weight=3)
    st.add_edge("a", "d", edge_weight=4)
    P = st.spanning_tree("a")
    assert P == {"a": None, "b": "a", "c": "b", "d": "c"}
