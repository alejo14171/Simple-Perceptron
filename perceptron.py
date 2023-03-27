import numpy as np
import matplotlib.pyplot as plt

from muestras import generar_muestras, graficar_muestras

# Inicialización
alpha = 0.3
m = 1
b = 0
w = np.array([-0.5, 0.5])

def etiqueta_esperada(x):
    return x[1]

def actualizar(parametro, x_i, error):
    parametro = parametro + (alpha*error*x_i)
    return parametro

def check_error_clasificacion(array_errores):
    for item in array_errores:
        if item != 0:
            return False
    
    return True


# Condiciones iniciales de w y b
b = 1
X, y = generar_muestras(6, m, b)
graficar_muestras(X, y, m, b, 'not done')
condicion_salida = False

x_muestras = []

for i in range(len(y)):
    x_muestras.append([X[i], y[i]])

m1 = -w[0]/w[1]
b1 = -b/w[1]
graficar_muestras(X, y, m1, b1, 'not done')
i = 0

while condicion_salida == False:
    error_clasificacion = []
    print('iteración:', i)
    i+=1
    for x_i in x_muestras:
        output_neurona = 1 if (np.dot(w, x_i[0]) + b)>0 else -1
        error = etiqueta_esperada(x_i) - output_neurona
        w = actualizar(w, x_i[0], error)
        b = b - error
        error_clasificacion.append(error)
    
    m1 = -w[0]/w[1]
    b1 = -b/w[1]
    graficar_muestras(X, y, m1, b1, 'not done')
    condicion_salida = True if check_error_clasificacion(error_clasificacion) else False
graficar_muestras(X, y, m1, b1, 'done')