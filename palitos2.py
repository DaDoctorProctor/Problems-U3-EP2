import plotly.graph_objects as go 

def stemize(n, xn):
	import numpy as np
	samples = len(n)
	ns = np.linspace(0, 0, 0)
	xns = np.linspace(0, 0, 0)
	for i in range(samples):
		ns = np.append(ns, [n[i], n[i], n[i]*1.5])
		xns = np.append(xns, [0, xn[i], np.newaxis])
	return ns, xns

def stem_plot(**kwargs):
	nargs = len(kwargs)
	x = kwargs.get('x', None)
	y = kwargs.get('y', None)
	color = kwargs.get('color', 'royalblue')
	label = kwargs.get('label', None)
	xs, ys = stemize(x, y)
	a = go.Scatter(x=x, y=y, mode='markers', showlegend=(label != None), marker=dict(color=color), name=label)
	b = go.Scatter(x=xs, y=ys, showlegend=False, line=dict(color=color))
	return a,b