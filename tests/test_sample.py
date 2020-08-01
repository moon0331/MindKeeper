import sys
sys.path.append('..')
import matplotlib.pyplot as plt
from IPython.core.display import Image
from networkx.drawing.nx_pydot import to_pydot

from src.package.graph import MindGraph

if __name__ =='__main__':
    g = MindGraph()
    g.addEdgeWithLine(input())
    d = to_pydot(g)
    d.set_dpi(600)
    Image(d.create_png(), width=600)

    print("hello")