#Segundo
import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot

#frecuencia de paso
wp = 0.3*pi
#frecuencia de rechazo
ws = 0.4*pi
delta_w = ws-wp

#orden del filtro, numero de taps
M = ceil(11*pi/delta_w) + 1
n = arange(M)

#frecuencia de corte (filtro pasa bajas ideal)
wc = (ws-wp)/2 #w = 2*pi*f
hd = fpb_ideal(wc,M)
w_bl = blackman(M)
h = hd*w_bl

all_plots(hn=h,wn=w_bl, fs=100000000, store='eps')

