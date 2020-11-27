#Sexto
import plotly.graph_objects as go
from numpy import *
from filter_lib_711 import *
from palitos2 import stem_plot
import scipy.signal.windows as ssw

#freq de paso
wp = 0.05*pi 
#freq rechazo
ws = 0.07*pi
#atenuacion deseada
a = 70

#banda de transicion normalizada
delta_w = ws - wp
delta_f = delta_w/2*pi

#orden del filtro
M = ceil(11*pi/delta_w)+1
n = arange(M)

B = 0.5842*((a-21)**0.4) + 0.07886*(a-21)

#freq de corte (filtro pasa bajas ideal)
wc = (ws+wp)/2
#coeficientes del sin cardinal
hd = fpb_ideal(wc,M)
#coeficientes de la ventana chebyshev
#w_black = blackman(M)
w_kai = kaiser(M,B)
#aplicamos la ventana
hw = hd*w_kai
#desplazamiento de espectro
delta = 0.4999
s = sin(2*pi*n*delta)
#aplicamos el desplazamiento
h = hw*s

#store = png,svg,pdf,html
#all_plots(hn=hw,wn=w_black, color='steelblue',store='html')

#fig = go.Figure()
#fig.add_traces(stem_plot(x=n,y=s,color='royalblue'))
#fig.update_layout(title='Coeficientes de la senal de desplazamiento', xaxis=dict(range=[0,M]))
#fig.update_xaxes(title_text='n')
#fig.update_yaxes(title_text='sin(wn/d)')

all_plots(hn=h,wn=w_kai, fs=100000000,store='eps')
