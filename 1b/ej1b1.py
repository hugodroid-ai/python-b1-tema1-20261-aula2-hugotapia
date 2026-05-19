"""
Enunciado:
Implementar la función 'obtain_max(list_numbers)' que recibe 
como parámetro una lista no vacía de números enteros y devuelve
el número mayor de la lista.

Recuerda que en Python existe la función llamada 'max'

Parámetros:
- list_numbers: Lista de números enteros

Ejemplo:
    Entrada:
    obtain_max([1, 45, 87, 21, 0, 23, 28])

    Salida:
    87


"""

def obtain_max(list_numbers):
    #validaciones 
    if not isinstance(list_numbers,list):
        raise ValueError("El parametro debe ser una lista")
    if len(list_numbers)==0:
        raise ValueError("La lista no debe estar vacia")
    for n in list_numbers:
        if not isinstance(n,int):
            raise ValueError("La lista debe contener numeros enteros")
    #Obtenemos el numero mayor de la lista 
    numero_maximo= max(list_numbers)
    return numero_maximo

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(obtain_max([1, 45, 87, 21, 0, 23, 28]))