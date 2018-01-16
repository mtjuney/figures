from matplotlib import rc
import daft

rc("font", family="Ricty")
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

	pgm = daft.PGM(shape=[3, 2])

	plot_params = {'alpha': 0.}
	pgm.add_node(daft.Node('p', '', 1.5, 1))
	pgm.add_node(daft.Node('p_m', r'$f(\sum w_i x_i)$', 1.7, 1.4, plot_params=plot_params))

	pgm.add_node(daft.Node('x1', r'$x_1$', 0.5, 1.5))
	pgm.add_node(daft.Node('x2', r'$x_2$', 0.5, 0.5))
	pgm.add_node(daft.Node('z', '', 2.8, 1.0, plot_params=plot_params))

	pgm.add_edge('x1', 'p')
	pgm.add_edge('x2', 'p')
	pgm.add_edge('p', 'z')

	pgm.add_node(daft.Node('w1', r'$w_1$', 0.8, 1.2, plot_params=plot_params))
	pgm.add_node(daft.Node('w2', r'$w_2$', 0.8, 0.8, plot_params=plot_params))

	pgm.render()
	pgm.figure.savefig('cnn_perceptron.pdf')


def math1():

	pgm = daft.PGM(shape=[2.4, 0.5])

	pgm.add_node(daft.Node('p', r'$E(x) = (f(\sum w_i x_i) - t)^2$', 1.2, 0.25, plot_params={'alpha': 0.}))

	pgm.render()
	pgm.figure.savefig('error_math.pdf')


def graph5():
	layer_nodenum = [5, 3]
	height = max(layer_nodenum)
	pgm = daft.PGM(shape=[len(layer_nodenum) * 3 + 1, height])

	# ひとつめ
	for i in range(layer_nodenum[0]):
		pgm.add_node(daft.Node('1_{}_{}'.format(0, i), '', 1, (i + 1) * height / (layer_nodenum[0] + 1)))
	for i in range(layer_nodenum[1]):
		pgm.add_node(daft.Node('1_{}_{}'.format(1, i), '', 2, (i + 2) * height / (layer_nodenum[0] + 1)))
	for j in range(layer_nodenum[1]):
		for i in range(j, j + 3):
			params = {}
			if j!=0:
				params['alpha'] = 0.1
			elif i == j:
				params['ec'] = 'r'
			elif i == j + 1:
				params['ec'] = 'b'
			else:
				params['ec'] = 'g'
			pgm.add_edge('1_{}_{}'.format(0, i), '1_{}_{}'.format(1, j), **params)

	# ふたつめ
	for i in range(layer_nodenum[0]):
		pgm.add_node(daft.Node('2_{}_{}'.format(0, i), '', 3, (i + 1) * height / (layer_nodenum[0] + 1)))
	for i in range(layer_nodenum[1]):
		pgm.add_node(daft.Node('2_{}_{}'.format(1, i), '', 4, (i + 2) * height / (layer_nodenum[0] + 1)))
	for j in range(layer_nodenum[1]):
		for i in range(j, j + 3):
			params = {}
			if j!=1:
				params['alpha'] = 0.1
			elif i == j:
				params['ec'] = 'r'
			elif i == j + 1:
				params['ec'] = 'b'
			else:
				params['ec'] = 'g'
			pgm.add_edge('2_{}_{}'.format(0, i), '2_{}_{}'.format(1, j), **params)

	# みっつめ
	for i in range(layer_nodenum[0]):
		pgm.add_node(daft.Node('3_{}_{}'.format(0, i), '', 5, (i + 1) * height / (layer_nodenum[0] + 1)))
	for i in range(layer_nodenum[1]):
		pgm.add_node(daft.Node('3_{}_{}'.format(1, i), '', 6, (i + 2) * height / (layer_nodenum[0] + 1)))
	for j in range(layer_nodenum[1]):
		for i in range(j, j + 3):
			params = {}
			if j!=2:
				params['alpha'] = 0.1
			elif i == j:
				params['ec'] = 'r'
			elif i == j + 1:
				params['ec'] = 'b'
			else:
				params['ec'] = 'g'
			pgm.add_edge('3_{}_{}'.format(0, i), '3_{}_{}'.format(1, j), **params)

	pgm.render()
	pgm.figure.savefig('cnn_weight.pdf')

graph1()
graph2()
graph3()
graph4()
math1()
graph5()
