from matplotlib import rc
import daft

rc("font", family="Ricty", size=15)
rc("text", usetex=True)

def graph1():
	layer_nodenum = [5, 3, 3, 2]
	height = max(layer_nodenum)
	pgm = daft.PGM(shape=[len(layer_nodenum) + 1, height])

	for n in range(len(layer_nodenum)):

		for i in range(layer_nodenum[n]):
			pgm.add_node(daft.Node('{}_{}'.format(n, i), '', n + 1, (i + 1) * height / (layer_nodenum[n] + 1)))


	for n in range(len(layer_nodenum) - 1):

		for j in range(layer_nodenum[n + 1]):
			for i in range(layer_nodenum[n]):
				pgm.add_edge('{}_{}'.format(n, i), '{}_{}'.format(n + 1, j))

	plot_params = {}
	plot_params['alpha'] = 0.
	pgm.add_node(daft.Node('input_label', 'Input Layer', 1, 4.7, plot_params=plot_params))
	pgm.add_node(daft.Node('output_label', 'Output Layer', 4, 4., plot_params=plot_params))

	pgm.render()
	pgm.figure.savefig('nn.pdf')

def graph2():

	layer_nodenum = [5, 3]
	height = max(layer_nodenum)
	pgm = daft.PGM(shape=[len(layer_nodenum) + 1, height])

	for i in range(layer_nodenum[0]):
		pgm.add_node(daft.Node('{}_{}'.format(0, i), '', 1, (i + 1) * height / (layer_nodenum[0] + 1)))

	for i in range(layer_nodenum[1]):
		pgm.add_node(daft.Node('{}_{}'.format(1, i), '', 2, (i + 2) * height / (layer_nodenum[0] + 1)))


	for n in range(len(layer_nodenum) - 1):

		for j in range(layer_nodenum[n + 1]):
			for i in range(layer_nodenum[n]):
				pgm.add_edge('{}_{}'.format(n, i), '{}_{}'.format(n + 1, j))

	pgm.render()
	pgm.figure.savefig('nn_simple.pdf')


def graph3():
	layer_nodenum = [5, 3]
	height = max(layer_nodenum)
	pgm = daft.PGM(shape=[len(layer_nodenum) + 1, height])

	for i in range(layer_nodenum[0]):
		pgm.add_node(daft.Node('{}_{}'.format(0, i), '', 1, (i + 1) * height / (layer_nodenum[0] + 1)))

	for i in range(layer_nodenum[1]):
		pgm.add_node(daft.Node('{}_{}'.format(1, i), '', 2, (i + 2) * height / (layer_nodenum[0] + 1)))

	for j in range(layer_nodenum[1]):
		for i in range(j, j + 3):
			pgm.add_edge('{}_{}'.format(0, i), '{}_{}'.format(1, j))

	pgm.render()
	pgm.figure.savefig('cnn_simple.pdf')


def graph4():

	pgm = daft.PGM(shape=[2, 2])

	pgm.add_node(daft.Node('p', '', 1, 1))

	pgm.add_node(daft.Node('x1', r'$x_1$', 0.5, 1.5, plot_params=plot_params))
	pgm.add_node(daft.Node('x2', r'$y_2$', 0.5, 0.5, plot_params=plot_params))
	pgm.add_node(daft.Node('z', r'$f(\sum x_i)$', 1.5, 1.5, plot_params=plot_params))

	pgm.add_edge('x1', 'p')
	pgm.add_edge('x2', 'p')
	pgm.add_edge('p', 'z')

	pgm.render()
	pgm.figure.savefig('cnn_perceptron.pdf')

graph1()
graph2()
graph3()
