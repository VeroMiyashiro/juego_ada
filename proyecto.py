from random import choice

palabras = ['celular', 'camello', 'python', 'bote', 'pizarron']
letras_incorrectas = []
letras_correctas = []
intentos = 5
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

palabra_elegida, letras_unicas = elegir_palabra(palabras)

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('__')
    print(lista_oculta)

def pedir_letra():
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    letra = input("Ingresa una letra al juego: ").lower()
    if len(letra) != 1 or letra not in abecedario:
        print("Ingresa solo letras.")
        return pedir_letra()
    return letra

def verificar_letra(letra):
    if letra in palabra_elegida:
        letras_correctas.append(letra)
        return True
    else:
        letras_incorrectas.append(letra)
        return False

while not juego_terminado:
    mostrar_nuevo_tablero(palabra_elegida)
    print("Letras incorrectas:", letras_incorrectas)
    print("Intentos restantes:", intentos)

    letra = pedir_letra()

    if verificar_letra(letra):
        aciertos += 1
        if aciertos == letras_unicas:
            print("¡Felicitaciones! Has adivinado la palabra:", palabra_elegida)
            juego_terminado = True
            break
    else:
        intentos -= 1
        if intentos == 0:
            print("¡Uy! Te quedaste sin intentos. La palabra era:", palabra_elegida)
            juego_terminado = True
            break



if juego_terminado:
    print("¡Fin del juego!")
