#Problema 8
import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot
import scipy.signal.windows as ssw

ws = 0.6*pi #freq de rechazo sup.
wp = 0.7*pi #freq de paso sup.
a = 60 #atenuacion deseada

delta_w = abs(wp-ws) #banda de transicion.
delta_f = delta_w/(2*pi) #banda de transicion normalizada

#Orden del filtro
M = int(ceil(a/(22*delta_f)))
n = arange(M)

wc = (ws+wp)/2 #freq de corte superior.

h = fpb_ideal(pi,M) -fpb_ideal(wc,M) #dif de sin cardinales
#h = -fpb_ideal(wc,M) #diferencia de sin cardinal
w = ssw.chebwin(M,a) #ventana chebyshev
hn = h*w

all_plots(hn=hn,wn=w,fs=100000000, store='eps')








