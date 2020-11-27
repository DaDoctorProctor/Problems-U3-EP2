#Filtro 5

import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot
import scipy.signal.windows as ssw

wp = 0.05*pi

ws = 0.07*pi

a = 70

delta_w = ws - wp
delta_f = delta_w/2*pi

#orden del filtro
M = ceil(11*pi/delta_w)+1
n = arange(M)

#frecuencia de corte (filtro pasa bajas ideal)
wc = (ws+wp)/2
#coeficientes del sin cardinal
hd = fpb_ideal(wc,M)
#coeficientes de la ventana chebyshev
w_black = blackman(M)
#aplicamos la ventana
hw = hd*w_black
#desplazamiento del espectro
delta = 1/4
s = sin(2*pi*n*delta) #0.25 = delta %
#aplicamos el desplazamiento
h = hw*s

#all_plots(hn=hw,wn=w_black, color='steelblue',store='html')

#fig = go.Figure()
##fig.add_traces(stem_plot(x=n,y=s,color='royalblue'))
#fig.update_layout(title='Coeficientes de la senal de desplazamiento', xaxis=dict(range=[0,M]))
#fig.update_xaxes(title_text='n')
#fig.update_yaxes(title_text='sin(wn/d)')

all_plots(hn=h, wn=w_black, fs=100000000,store='eps')
