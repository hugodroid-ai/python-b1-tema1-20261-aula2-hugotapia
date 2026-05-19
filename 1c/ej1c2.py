"""
Enunciado:
Escribe una función llamada 'invert_list(lst)' que reciba como parámetro
una lista 'lst' y la invierta utilizando recursión. La función debe
devolver la lista invertida.

Parámetros:
    lst (list): una lista de elementos.

Ejemplo
    Entrada:
    lst = [1, 2, 3, 4, 5]
    print(invert_list(lst))

    Salida:
    [5, 4, 3, 2, 1]


"""

def invert_list(lst):
    # validacion
    if not isinstance(lst,list):
        raise ValueError(" El parametro lst debe ser una lista ")
#Caso base : cuando la lista este vacia o contiene 1 elemento ya esta invertida->detiene la recursion
    if len(lst)<=1:
        return lst
#Recursividad ->empieza cuando hay >2 elementos y luego concatenamos 1er elemento(se convirete en ultimo)
    return invert_list(lst[1: ])+ [lst[0]]
#metodo alternativo 
   # if len(lst)<=1:
    #    return lst
    #return [lst[-1]]+ invert_list(lst[ :-1]) # ultimo elemento lo ponemos al principio'''

    
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script:
lst = [1, 2, 3, 4, 5]
print(invert_list(lst))
