#Tercero
import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot
import scipy.signal.windows as ssw

#freq de paso
wp = 0.2*pi
#freq de rechazo
ws = 0.3*pi
#atenuacion deseada
a = 60

#banda de transicion normalizada
delta_w = ws-wp
delta_f = (ws-wp)/(2*pi)

#orden del filtro
M = int(ceil(a/(22*delta_f)))
#M = ceil(7.8*pi/delta_f) + 1
n = arange(M)

B = 0.5842*((a-21)**0.4) + 0.07886*(a-21)

#freq de corte (filtro pasa bajas ideal)
wc = (ws+wp)/2
#coeficientes del sin cardinal
hd = fpb_ideal(wc,M)
w_kai = kaiser(M,B)
#coeficientes de la ventana chebyshev
#w_cheb = ssw.chebwin(M,a)
#aplicamos la ventana
hw = hd*w_kai

all_plots(hn=hw,wn=w_kai, fs=100000000, store='eps')

