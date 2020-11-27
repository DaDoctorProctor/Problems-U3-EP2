#Problema 7
import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot
import scipy.signal.windows as ssw

ws1 = 0.25*pi #freq de rechazo inferior.
wp1 = 0.35*pi #freq de paso inferior.
wp2 = 0.65*pi #freq de rechazo sup.
ws2 = 0.75*pi #freq de paso superior.
a = 60

delta_w = min((wp1-ws1), (ws2-wp2))
M = ceil(11*pi/delta_w) + 1
n = arange(M)

wc1 = (ws1+wp1)/2
wc2 = (wp2+ws2)/2

h = fpb_ideal(wc2,M) - fpb_ideal(wc1,M)
w = blackman(M)
hn = h*n

all_plots(hn=hn,wn=w,fs=100000000,store='eps')



