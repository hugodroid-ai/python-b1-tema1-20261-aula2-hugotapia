""" 
Enunciado:
Escribe una función llamada is_palindrome(word) que reciba como parámetro
una cadena word y verifique si es un palíndromo utilizando recursión.
La función debe devolver True si la cadena es un palíndromo y False en
caso contrario.

Parámetros:
    word (str): una cadena de caracteres.

Ejemplo:
    Entrada:
    word = "racecar"
    print(is_palindrome(word))

    Salida:
    True
"""
def is_palindrome(word):
    # validaciones
    if not isinstance(word,str):
        raise ValueError("El paparametro debe ser un string")
   
    #Caso base : 
    # 1 si la cadena es vacia o con un solo elemento es un palindrome  
    if len(word)<=1:
        return True
    # 2 Si la primera letra y la ultima letra no coinciden no es palindrome 
    if word[0]!=word[-1]:
        return False
    # 3 Caso recursivo: Si la primera y la ultima coinciden ,
    #Comparamos el interior de la cadena sin esos extremos
    return is_palindrome(word[1:-1])
    
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
word = "level"
print(f"Is '{word}' word palindrome?", is_palindrome(word))
#
word = "juan"
print(f"Is '{word}' word palindrome?", is_palindrome(word))
