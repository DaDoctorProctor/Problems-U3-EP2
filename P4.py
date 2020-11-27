#Cuarto
import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot
import plotly.express as px
import scipy.signal.windows as ssw
from psutil import *
#from pandas import *

#step frequencies
wp = 0.4*pi
#frequencia de rechazo
ws = 0.5*pi
#atenucion deseada
a = 60

#banda de transicion normalizada
delta_f = (ws-wp)*(2*pi)

#orden del filtro
M = int(ceil(a/(22*delta_f)))
n = arange(M)

#frecuencia de corte (filtro pasa bajas ideal)
wc = (ws+wp)/2
hd = fpb_ideal(wc,M)
w_cheb = ssw.chebwin(M,a)
h = hd*w_cheb

all_plots(hn=h,wn=w_cheb,fs=100000000,store='eps')