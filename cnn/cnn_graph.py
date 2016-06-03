import pygraphviz as pgv


g = pgv.AGraph(directed = True, strict='true', rankdir="LR", ordering="out", splines="line", compound='true')

layer_nodenum = [4, 3, 3, 2]

g.node_attr["style"] = "solid"
g.node_attr["shape"] = "circle"
g.node_attr['fixedsize']='true'

for n in range(len(layer_nodenum) - 1):

	layer_nodes = ["{}_b".format(n)]

	for j in range(layer_nodenum[n + 1]):
		for i in range(layer_nodenum[n]):
			g.add_edge("{}_{}".format(n, i), "{}_{}".format(n + 1, j))
			layer_nodes.append("{}_{}".format(n, i))
		g.add_edge("{}_b".format(n), "{}_{}".format(n + 1, j))

	g.add_subgraph(layer_nodes, name="layer_{}".format(n))

layer_nodes = []


for i in range(layer_nodenum[-1]):
	layer_nodes.append("{}_{}".format(len(layer_nodenum) - 1, i))

g.add_subgraph(layer_nodes, name="output")

g.node_attr["label"] = ""

g.layout("dot")
g.draw('multi_perceptron.png')

g.clear()






nodes = [["1", "2", "3", "4", "5"], ["6", "7", "8"]]

g.node_attr["style"] = "solid"
g.node_attr["shape"] = "circle"



for node_from in nodes[0]:
	for node_to in nodes[1]:
		g.add_edge(node_from, node_to)

g.add_subgraph(nodes[0], name="s1")
g.add_subgraph(nodes[1], name="s2")


g.draw('simple_neural.png', prog="dot")


g.clear()

g.node_attr["style"] = "solid"
g.node_attr["shape"] = "circle"
g.add_subgraph(nodes[0], name="s1")
g.add_subgraph(nodes[1], name="s2")


for node in nodes[0][0:3]:
	g.add_edge(node, "6")

for node in nodes[0][1:4]:
	g.add_edge(node, "7")

for node in nodes[0][2:5]:
	g.add_edge(node, "8")

g.draw('simple_cnn.png', prog="dot")
