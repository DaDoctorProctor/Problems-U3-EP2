#Primero
import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *
from filter_lib_711 import *

#Frecuencia de paso
wp = 0.2*pi
#Frecuencia de rechazo
ws = 0.3*pi
delta_w = ws-wp

#orden del filtro
M = ceil(6.6*pi/delta_w)+1
n = arange(M)

#Frecuencia de corte
wc = (ws+wp)/2
hd = fpb_ideal(wc,M)
w_ham = hamming(M)
h = hd*w_ham

m,a,dB,w = resp_frec(h)

#fig = go.Figure()
#fig.add_traces(stem_plot(x=n,y=hd,color='lightcoral'))
#fig.update_layout(title='Coficientes del filtro (respuesta al impulso ideal'))

all_plots(hn=h,wn=w_ham,fs=100000000,store='eps')


