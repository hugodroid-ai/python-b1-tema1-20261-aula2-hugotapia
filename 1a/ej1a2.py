'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30



'''

def sum_odd_numbers(list_numbers):
    
    #1 Validamos el parametro lista
    if not isinstance(list_numbers,list):
        raise ValueError("El parametro debe ser una lista")
    #2 Recorremos  la lista para validar cada elemento
    for numero in list_numbers:
        if not isinstance(numero,int) or isinstance(numero,bool):
            raise ValueError("Todos los numeros deber ser enteros")
        if numero<0:
            raise ValueError("Todos los numeros deben ser mayores que 0")
    # 3 Obtenemos la suma de los numeros impares de la lista
    suma=0
    for numero in list_numbers:
         if numero%2!=0:
            suma+=numero
    return suma

    
    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
