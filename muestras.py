import matplotlib.pyplot as plt
import numpy as np

def generar_muestras(n, m, b):
    """
    Genera n muestras aleatorias con etiquetas de clasificación 1 y -1, separadas por una línea recta
    con la ecuación y = mx + b.
    
    Args:
    - n: número de muestras a generar
    - m: pendiente de la línea recta
    - b: término independiente de la línea recta
    
    Returns:
    - X: matriz de características de las muestras generadas, de dimensiones (n, 2)
    - y: vector de etiquetas de clasificación de las muestras generadas, de dimensiones (n,)
    """
    
    # Generar valores aleatorios para las características x de las muestras
    X = np.random.uniform(0, 10, size=(n, 2))
    
    # Calcular los valores de y correspondientes a la línea recta
    y_linea = m*X[:,0] + b
    
    # Asignar etiquetas de clasificación 1 o -1 a cada muestra según si está por encima o por debajo de la línea recta
    y = np.where(X[:,1] > y_linea, 1, -1)
    
    return X, y


def graficar_muestras(X, y, m, b, flag):
    """
    Grafica las muestras generadas por la función generar_muestras, separadas por una línea recta con la
    ecuación y = mx + b. Las muestras con etiqueta 1 se muestran en azul y las muestras con etiqueta -1
    se muestran en rojo.
    
    Args:
    - X: matriz de características de las muestras generadas, de dimensiones (n, 2)
    - y: vector de etiquetas de clasificación de las muestras generadas, de dimensiones (n,)
    - m: pendiente de la línea recta
    - b: término independiente de la línea recta
    """

    plt.clf()
    
    # Separar las muestras por etiquetas de clasificación
    X_1 = X[y == 1]
    X_menos_1 = X[y == -1]

    plt.xlim = [-10, 10]
    plt.ylim = [-10, 10]
    plt.title('Muestras separadas por una línea recta')
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    
    # Graficar las muestras con etiqueta 1 en azul y las muestras con etiqueta -1 en rojo
    plt.scatter(X_1[:,0], X_1[:,1], color='blue', label='Etiqueta 1')
    plt.scatter(X_menos_1[:,0], X_menos_1[:,1], color='red', label='Etiqueta -1')
    
    # Graficar la línea recta que separa las muestras
    # [x_min, x_max] = plt.xlim()
    # Configurar el título y las etiquetas de los ejes

    x_linea = np.array([-10, 10])
    y_linea = m*x_linea + b
    plt.plot(x_linea, y_linea, color='green', label='Línea recta separadora')
    
    
    # Mostrar la leyenda
    plt.legend()
    
    # Mostrar la gráfica
    if flag != 'done': plt.pause(0.5)
    else: plt.show()

# X, y = generar_muestras(100, 2, 1)
# graficar_muestras(X, y, 2, 1)

