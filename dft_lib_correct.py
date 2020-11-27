def mi_dft(x):
	from numpy import pi, sqrt, arctan2, array, arange, e
	N = len(x)
	n = arange(N)
	X = []
	for m in range(N):
		xne = sum(x*(e**(-1j*2*pi*m*n/N)))
		#X.append(round(xne, 10) + 0)
		X.append(xne)
	X = array(X)
	X_r = X.real
	X_i = X.imag
	X_m = sqrt(X.real**2+X.imag**2)
	X_a = arctan2(X.imag, X.real)*(180/pi)
	return X_r, X_i, X_m.real, X_a.real

def mi_idft(X):
	from numpy import pi, array, arange, e
	N = len(X)
	m = arange(N)
	xn = []
	for n in range(N):
		Xme = sum(X*(e**(1j*2*pi*m*n/N)))
		#xn.append(round(Xme, 10) + 0)
		xn.append(Xme)
	xn = array(xn)/N
	xn_r = xn.real
	xn_i = xn.imag
	return xn_r, xn_i
