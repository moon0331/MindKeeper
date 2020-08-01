# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

# create graph
# load graph
# print graph
# get name of node
# get value of edge TODO

def get_edge_pair(lst):
	return ((lst[i], lst[i+1]) for i in range(len(lst)-1))

class MindGraph:
	def __init__(self, path=''): #input path
		if path:
			self.graph = self.get_graph(path)
		else:
			self.graph = nx.DiGraph() #https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_directed.html

	def add_edge(self, edge, weight_value=1, verbose=False):
		if verbose:
			print(edge)
		if self.graph.has_edge(*edge):
			self.graph[edge[0]][edge[1]]['weight']+=weight_value
		else:
			self.graph.add_edge(*edge, weight=weight_value) # weight=val로 weight 추가 가능

	def add_edge_from_file(self, fname):
		# 파일의 모든 라인을 읽어 연결 상태 추가
		with open(fname, 'r') as f:
			flist = (line.strip() for line in f.readlines())
		
		for edge in get_edge_pair(flist):
			self.add_edge(edge)

	def add_edge_from_line(self, line):
		# string 한줄 읽어서
		lst = line.split()
		for edge in get_edge_pair(lst):
			self.add_edge(edge)

	def draw(self, show=False, time=0):
		nx.draw_networkx(self.graph)
		if show:
			self.show_graph(time)

	def save(self, fmt, fname):
		if fmt.lower() is 'image':
			plt.savefig(fname)
		elif fmt.lower() is 'graphml':
			self.save_graph(fname)

	def show_graph(self, time=1):
		plt.show()
		plt.pause(time)
		plt.close('all')

	def show_weight_info(self):
		return self.graph.edges(data=True)

	def get_shortest_path(self, *args, **kwargs):
		return nx.shortest_path(self.graph, *args, **kwargs)

	def get_graph(self, path):
		return nx.read_graphml(path)

	def save_graph(self, path):
		nx.write_graphml(self.graph, path)