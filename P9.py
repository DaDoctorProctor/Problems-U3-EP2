#problema 9
import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot
import scipy.signal.windows as ssw

wp1 = 0.2*pi
ws1 = 0.3*pi
ws2 = 0.7*pi
wp2 = 0.8*pi
a = 60

delta_w = min(abs(ws1-wp1),abs(wp2-ws2)) #seleccion de la banda de trans.
delta_f = delta_w/(2*pi)# banda de transicion normalizada

#orden del filtro
M = int(ceil(a/(22*delta_f)))
n = arange(M)

wc1 = (wp1*ws1)/2
wc2 = (ws2*wp2)/2

h = fpb_ideal(pi,M) - fpb_ideal(wc2,M) + fpb_ideal(wc1,M)
w = ssw.chebwin(M,a)
hn = h*w

all_plots(hn=hn,wn=w,fs = 100000000, store='eps')