"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7
"""
def find_max(lst):
    # validaciones 
    if not isinstance(lst,list):
        raise ValueError(" lst debe ser una lista")
    if len(lst)==0:
        raise ValueError(" La lista  lst no debe ser vacia")
    for n in lst:
        if not isinstance (n,(int,float)) or  isinstance(n,bool):
            raise ValueError("El elemento de la lista  lst debe ser entero o flotante")
        
    # El caso base, rompe la recursion seria cuando la lista tiene 1 solo elemento
    if len(lst) ==1:
        return lst[0]
    #Caso recursivo
    # Calculamos el maximo  del resto de la lista sin el 1r elemento 
    max_resto=find_max(lst[1:])
    #comparamos el maximo numero del resto con el 1er elemento y retornamoa el myor de los dos
    if max_resto>lst[0]:
        return max_resto
    else:
        return lst[0]
     
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script

numbers_list = [1, 5, 2, 7, 3]
print(find_max(numbers_list))

