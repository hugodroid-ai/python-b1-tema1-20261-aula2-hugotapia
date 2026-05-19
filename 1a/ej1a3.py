'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH



'''

def invert_text(text_chain:str):
    # validamos el parametro para que sea str
    if not isinstance(text_chain,str):
        raise ValueError("El parametro debe ser una cadena (string)")
   #Invertimos la cadena 
    texto_invertido=text_chain[ :  :-1]
    return texto_invertido

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(invert_text("Hello world!"))