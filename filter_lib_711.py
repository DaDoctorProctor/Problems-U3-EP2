def my_sinc(X):
	from numpy import sin, array
	S = []
	for x in X:
		if x == 0:
			s = 1
		else:
			s = sin(x)/x 
		S.append(s)
	return array(S)

def fpb_ideal(w, M):
	from numpy import arange, pi
	pm = (M-1)/2
	n = arange(M)
	m = n - pm 
	rpb = my_sinc(w*m)*(w/pi) #2f * sinc(2*pi*f*m)
	return rpb

#Esta función determina la respuesta en frecuencia de diferentes filtros
def resp_frec(h):
	from numpy import sqrt, arctan2, pi, log10, arange, fft, max
	N = 2**14 
	hN = int(N/2)
	hm = fft.fft(h, N) #fast Fourier transform
	mag = abs(hm)
	ang = arctan2(hm.imag, hm.real)*(180/pi)
	magh = mag[0:hN]
	angh = ang[0:hN]
	dB = 20*log10(magh/max(magh))
	m = arange(hN)
	w = m*pi/(hN-1)
	return magh, angh, dB, w 

def all_plots(**kwargs):
	from numpy import arange, pi
	import plotly.graph_objects as go 
	from palitos2 import stem_plot
	import datetime
	nargs = len(kwargs)
	hn = kwargs.get('hn', [0])
	wn = kwargs.get('wn', [0])
	fs = kwargs.get('fs', None)
	fformat = kwargs.get('store', None)
	color = kwargs.get('color', None)

	if color == None:
		color1 = 'firebrick'
		color2 = 'royalblue'
		color3 = 'blueviolet'
		color4 = 'darkcyan'
		color5 = 'forestgreen'
		color6 = 'lightcoral'
	else:
		color1 = color
		color2 = color
		color3 = color
		color4 = color
		color5 = color
		color6 = color

	m,a,dB,w = resp_frec(hn) 

	if fformat == None:
		if len(wn) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(wn)), y=wn, color=color1))
			fig.update_layout(title='Coeficientes de la ventana', xaxis=dict(range=[0, len(wn)]))
			fig.update_xaxes(title_text='n')
			fig.update_yaxes(title_text='w(n)')
			fig.show()

		fig = go.Figure()
		fig.add_traces(stem_plot(x=arange(len(hn)), y=hn, color=color2))
		fig.update_layout(title='Coeficientes del filtro', xaxis=dict(range=[0, len(hn)]))
		fig.update_xaxes(title_text='n')
		fig.update_yaxes(title_text='h(n)')
		fig.show()

		fig = go.Figure()
		fig.add_trace(go.Scatter(x=w/pi, y=m, line=dict(color=color3)))
		fig.update_layout(title='Magnitud de la respuesta')
		fig.update_xaxes(title_text='w (rad/s)')
		fig.update_yaxes(title_text='|H(m)|')
		fig.show()

		fig = go.Figure()
		fig.add_trace(go.Scatter(x=w/pi, y=dB, line=dict(color=color4)))
		fig.update_layout(title='Magnitud de la respuesta (dB)')
		fig.update_xaxes(title_text='w (rad/s)')
		fig.update_yaxes(title_text='dB')
		fig.show()

		if fs != None:
			fs = fs/2
			fig = go.Figure()
			fig.add_trace(go.Scatter(x=w/pi*fs, y=m, line=dict(color=color5)))
			fig.update_layout(title='Magnitud de la respuesta')
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='|H(m)|')
			fig.show()

			fig = go.Figure()
			fig.add_trace(go.Scatter(x=w/pi*fs, y=dB, line=dict(color=color6)))
			fig.update_layout(title='Magnitud de la respuesta (dB)')
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='dB')
			fig.show()
	else:
		folder = 'all_plots/'
		dt= datetime.datetime.now()
		timestamp = str(dt.year)+str(dt.month)+str(dt.day)+'_'+str(dt.hour)+str(dt.minute)+str(dt.second)
		i = 1
		if len(wn) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(wn)), y=wn, color=color1))
			fig.update_layout(title='Coeficientes de la ventana', xaxis=dict(range=[0, len(wn)]))
			fig.update_xaxes(title_text='n')
			fig.update_yaxes(title_text='w(n)')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_window_coefficients.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_window_coefficients.'+fformat)
			i = i+1

		fig = go.Figure()
		fig.add_traces(stem_plot(x=arange(len(hn)), y=hn, color=color2))
		fig.update_layout(title='Coeficientes del filtro', xaxis=dict(range=[0, len(hn)]))
		fig.update_xaxes(title_text='n')
		fig.update_yaxes(title_text='h(n)')
		if fformat == 'html':
			fig.write_html(folder+timestamp+'_'+str(i)+'_filter_coefficients.'+fformat)
		else:
			fig.write_image(folder+timestamp+'_'+str(i)+'_filter_coefficients.'+fformat)
		i = i+1

		fig = go.Figure()
		fig.add_trace(go.Scatter(x=w/pi, y=m, line=dict(color=color3)))
		fig.update_layout(title='Magnitud de la respuesta')
		fig.update_xaxes(title_text='w (rad/s)')
		fig.update_yaxes(title_text='|H(m)|')
		if fformat == 'html':
			fig.write_html(folder+timestamp+'_'+str(i)+'_filter_mag_lineal.'+fformat)
		else:
			fig.write_image(folder+timestamp+'_'+str(i)+'_filter_mag_lineal.'+fformat)
		i = i+1

		fig = go.Figure()
		fig.add_trace(go.Scatter(x=w/pi, y=dB, line=dict(color=color4)))
		fig.update_layout(title='Magnitud de la respuesta (dB)')
		fig.update_xaxes(title_text='w (rad/s)')
		fig.update_yaxes(title_text='dB')
		if fformat == 'html':
			fig.write_html(folder+timestamp+'_'+str(i)+'_filter_mag_dB.'+fformat)
		else:
			fig.write_image(folder+timestamp+'_'+str(i)+'_filter_mag_dB.'+fformat)
		i = i+1

		if fs != None:
			fs = fs/2
			fig = go.Figure()
			fig.add_trace(go.Scatter(x=w/pi*fs, y=m, line=dict(color=color5)))
			fig.update_layout(title='Magnitud de la respuesta')
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='|H(m)|')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_filter_mag_Hz_lineal.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_filter_mag_Hz_lineal.'+fformat)
			i = i+1

			fig = go.Figure()
			fig.add_trace(go.Scatter(x=w/pi*fs, y=dB, line=dict(color=color6)))
			fig.update_layout(title='Magnitud de la respuesta (dB)')
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='dB')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_filter_mag_Hz_dB.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_filter_mag_Hz_dB.'+fformat)

def all_plots_X(**kwargs):
	from numpy import arange, pi
	import plotly.graph_objects as go 
	from palitos2 import stem_plot
	import datetime
	nargs = len(kwargs)
	xt = kwargs.get('xt', [0])
	t = kwargs.get('t', [0])
	xn = kwargs.get('xn', [0])
	Xm = kwargs.get('Xm', [0])
	Ym = kwargs.get('Ym', [0])
	yn = kwargs.get('yn', [0])
	fs = kwargs.get('fs', 1)
	fformat = kwargs.get('store', None)
	color = kwargs.get('color', None)

	if color == None:
		color1 = 'firebrick'
		color2 = 'royalblue'
		color3 = 'blueviolet'
		color4 = 'darkcyan'
		color5 = 'forestgreen'
		color6 = 'lightcoral'
	else:
		color1 = color
		color2 = color
		color3 = color
		color4 = color
		color5 = color
		color6 = color

	N = len(Xm)

	if fformat == None:
		if len(xt) > 1:
			fig = go.Figure()
			fig.add_trace(go.Scatter(x=t, y=xt, line=dict(color=color1)))
			fig.update_layout(title='Señal continua')
			fig.update_xaxes(title_text='t')
			fig.update_yaxes(title_text='x(t)')
			fig.show()

		if len(xn) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(xn))/fs, y=xn, color=color2))
			fig.update_layout(title='Señal discreta', xaxis=dict(range=[0, len(xn)/fs]))
			fig.update_xaxes(title_text='n')
			fig.update_yaxes(title_text='x(n)')
			fig.show()

		if len(Xm) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(Xm))*(fs/N), y=abs(Xm), color=color3))
			fig.update_layout(title='Espectro de la señal', xaxis=dict(range=[0, fs/2]))
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='X(m)')
			fig.show()

		if len(Ym) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(Ym))*(fs/N), y=abs(Ym), color=color4))
			fig.update_layout(title='Espectro de la señal filtrada', xaxis=dict(range=[0, fs/2]))
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='Y(m)')
			fig.show()

		if len(yn) > 1:
			fig = go.Figure()
			fig.add_trace(go.Scatter(x=arange(len(yn)), y=yn, line=dict(color=color5)))
			fig.update_layout(title='Señal filtrada')
			fig.update_xaxes(title_text='n')
			fig.update_yaxes(title_text='y(n)')
			fig.show()
	else:
		folder = 'all_plots/'
		dt = datetime.datetime.now()
		timestamp = str(dt.year)+str(dt.month)+str(dt.day)+'_'+str(dt.hour)+str(dt.minute)+str(dt.second)
		i = 1
		if len(xt) > 1:
			fig = go.Figure()
			fig.add_trace(go.Scatter(x=t, y=xt, line=dict(color=color1)))
			fig.update_layout(title='Señal continua')
			fig.update_xaxes(title_text='t')
			fig.update_yaxes(title_text='x(t)')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_xt.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_xt.'+fformat)
			i = i+1

		if len(xn) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(xn))/fs, y=xn, color=color2))
			fig.update_layout(title='Señal discreta', xaxis=dict(range=[0, len(xn)/fs]))
			fig.update_xaxes(title_text='n')
			fig.update_yaxes(title_text='x(n)')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_xn.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_xn.'+fformat)
			i = i+1

		if len(Xm) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(Xm))*(fs/N), y=abs(Xm), color=color3))
			fig.update_layout(title='Espectro de la señal', xaxis=dict(range=[0, fs/2]))
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='X(m)')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_Xm.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_Xm.'+fformat)
			i = i+1

		if len(Ym) > 1:
			fig = go.Figure()
			fig.add_traces(stem_plot(x=arange(len(Ym))*(fs/N), y=abs(Ym), color=color4))
			fig.update_layout(title='Espectro de la señal filtrada', xaxis=dict(range=[0, fs/2]))
			fig.update_xaxes(title_text='f (Hz)')
			fig.update_yaxes(title_text='Y(m)')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_Ym.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_Ym.'+fformat)
			i = i+1

		if len(yn) > 1:
			fig = go.Figure()
			fig.add_trace(go.Scatter(x=arange(len(yn)), y=yn, line=dict(color=color5)))
			fig.update_layout(title='Señal filtrada')
			fig.update_xaxes(title_text='n')
			fig.update_yaxes(title_text='y(n)')
			if fformat == 'html':
				fig.write_html(folder+timestamp+'_'+str(i)+'_yn.'+fformat)
			else:
				fig.write_image(folder+timestamp+'_'+str(i)+'_yn.'+fformat)