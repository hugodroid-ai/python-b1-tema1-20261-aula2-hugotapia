"""
Enunciado:
Mediante la librería 'matplotlib', implementa una función llamada 
'line_graph(x,y)', se debe realizar únicamente la configuración 
para la gráfica (sin mostrar nada en pantalla).
De esta forma, deberás configurar el título, que será 'Graph';
los labels de los ejes, que serán 'Axis X' y 'Axis Y' y activar
el grid.

Puedes encontrar la documentación de la librería 'matplotlib' en el
siguiente enlace: https://matplotlib.org/stable/users/index

En concreto, te recomendamos que consultes:
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html


Los valores de los parámetros que recibe esta función son:
    
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]


"""

import matplotlib.pyplot as plt


# Esta función deberá configurar la gráfica en la variable plt
def line_graph(x, y):
   #1Dibujar la linea con los datos de x e y 
    plt.plot(x,y)

    # 2 poner el titulo
    plt.title("Graph")

    # 3 etiquetas 
    plt.xlabel("Axis X")
    plt.ylabel("Axis Y")
    
    #4 activar el grid
    plt.grid(True)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
line_graph([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
