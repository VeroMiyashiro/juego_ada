from random import choice
palabras = ['celular', 'camello', 'python','bote','pizarron']
letras_incorrectas =[]
letras_correctas = []
intentos = 5
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):

    palabra_elegida = choice(lista_palabras)
    letras_unicas =len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

palabra = elegir_palabra(palabras)

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta =[]
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(1)
        else:
            lista_oculta.append('__')
    print(lista_oculta)


def pedir_letra():
    abecedario ='abcdfghikalmnñopqrstuvwxyz'
    letra=input("Ingrease una letra al juego:").lower()
    if len(letra) !=1 or letra not in abbecedario: 
        print("Ingresa solo letras.")
        return pedir_letra()
    return letra 
#no te olvides de gurdar los cambios, sino no carga
