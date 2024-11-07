import subprocess
import re
import pytest

from student_code import SpanningTreeGraph

def test_spanning_tree_disconnected():
    st = SpanningTreeGraph()
    st.add_node("a")
    st.add_node("b")
    st.add_node("c")
    st.add_edge("a", "b", edge_weight=1)
    P = st.spanning_tree("a")
    assert "c" not in P
