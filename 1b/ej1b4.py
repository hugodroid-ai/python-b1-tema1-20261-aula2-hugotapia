'''
Enunciado:
Implementar la función 'results(list_numbers)' que reciba como parámetro una
lista que contiene números enteros y decimales llamada 'list_numbers', se pide
calcular el promedio y la desviación estándar mediante la
librería "Numpy" de todos los números dentro de la lista.

Cada resultado se debe imprimir en pantalla con su respectivo nombre 
'Average: {value}' y 'Standard deviation: {value}', dichos resultados deben
estar redondeados a 2 decimales. 

Los resultados también han de ser devueltos por la función.

Puedes consultar la referencia de la librería 'Numpy' en el siguiente enlace:
https://numpy.org/doc/stable/reference/index.html#reference

En concreto, te recomendamos que consultes:
* https://numpy.org/doc/stable/reference/generated/numpy.mean.html
* https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std

Parámetro:
- list_numbers: Lista de números enteros y decimales.

Ejemplo:
    Entrada:
    [1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42]
    
    Salida:
    Average: 19.74
    Standard deviation: 26.03

Enunciat:


'''


import numpy as np

def results(list_numbers):


    #1 convertir la lista en un array de numpy
    array= np.array(list_numbers)
    
    #2 Calcular el promedio redndear a decimales 
    average=round(np.mean(array),2)

    #3 Calcular la desviacion standard
    standard_deviation=round(np.std(array),2)
     
     #4 Imprimir resulatdos 
    print(f"Average: {average}")
    print(f"Standard deviation: {standard_deviation}")
    
    return average, standard_deviation
   

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
results([1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42])
