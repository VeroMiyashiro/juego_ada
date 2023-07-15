from random import choice
palabras = ['celular', 'camello', 'python','bote','pizarron']
letras_incorrectas =[]
letras_correctas = []
intentos = 5
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra = lista_palabras(lista_palabras):
    palabra ekegida = choice(lista_palabras):
    letras unicas =len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

palabra = elegir_palabr(palabras)

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta =[]
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(1)
        else:
            lista_oculta.append('__')
print(lista_oculta)
