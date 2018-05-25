# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 
xin = 0.0
yin = 0.0
zin = 0.0
tin = 0.0
tfin = 5.0
sigma = 10.0
beta = 2.67
rho = 28.0

def dxdt(sigma, y,x):
    return sigma*(y-x)
dxi = dxdt(sigma, yin, xin)

def dydt(rho, x,y,z):
    return rho*x-y-x*z
dyi = dydt(rho, xin, yin , zin)

def dzdt(beta, x,y,z):
    return -beta*z+x*y
dzi = dzdt(beta, xin, yin, zin)

for i in tfin:
    k1x = dxi
    k1y = dyi
    k1z = dzi
    k2x = dxi





