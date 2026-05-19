"""
Enunciado
Implementa la función `mult_recursive(value, times)` que debe devolver el
resultado de sumar `value` `times` veces. Como puedes ver, su comportamiento
real es como si fuera una multiplicación. La función ha de ser implementada
usando recursividad. La función recibe dos parámetros:
 - value: un número entero, que representa el número a sumar
 - times: un número entero, que representa el número de veces que ha de sumarse `value` al resultado
Por ejemplo, si `value` vale 2 y `times` vale 3, la función ha de devolver 6, resultado sumar 2 + 2 + 2
Como puedes ver, su comportamiento real es como si fuera una multiplicación

Parámetros:
    value: número entero que se desea sumar
    times: número de veces que se desea sumar 'value'

Ejemplo:
    Entrada:
    value = 2
    times = 3

    Salida:
    6

"""
def mult_recursive(value, times):
    # Validaciones 
    if not isinstance(value,int):
        raise ValueError("Value debe ser numero entero")
    if not isinstance(times,int):
        raise ValueError("times debe ser numero entero")
    #Funcion recursiva 
    value,times=times ,value*times
    return times



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
if __name__ == "__main__":
    print("Must print 6: ", mult_recursive(2, 3))
