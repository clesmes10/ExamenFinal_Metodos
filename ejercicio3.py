#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])
#grafica

plt.plot(t, u, "m")
plt.plot(t, v, "c")
plt.savefig("serie.png")

#covarianza

meanu = np.mean(u)
meanv = np.mean(v)
ene = len(t)

for i in range(len(t)):
    covarianza = ((u[i]-meanu)*(v[i]-meanv))/ene
    
print (covarianza)
