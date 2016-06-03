import pygraphviz as pgv


g = pgv.AGraph(directed = True)

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
