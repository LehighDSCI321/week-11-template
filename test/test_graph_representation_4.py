import subprocess
import re
import pytest

from student_code import SpanningTreeGraph

def test_edge_weights():
    st = SpanningTreeGraph()
    st.add_node("a")
    st.add_node("b")
    st.add_edge("a", "b", edge_weight=1)
    assert st.get_edge_weight("a", "b") == 1
    assert st.get_edge_weight("b", "a") == 1
