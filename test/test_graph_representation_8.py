import subprocess
import re
import pytest
from student_code import SpanningTreeGraph

def test_initialization():
    st = SpanningTreeGraph()
    assert isinstance(st, SpanningTreeGraph)
