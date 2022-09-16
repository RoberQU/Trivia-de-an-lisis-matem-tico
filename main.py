import random
import time

random.randint(0, 101)
time.sleep(2)

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[370m'
RESET = '\033[39m'

print(
    CYAN +
    '************* Bienvenido a mi trivia sobre análisis matemático **************'
    + RESET)
print(
    CYAN +
    '*************       Pondremos a prueba tus conocimientos       **************'
    + RESET)
print()
print(
    '************* puntos < 50   : Estudiante en proceso de aprendizaje **************'
)
print(
    '************* 50 <= puntos < 75 : Buen estudiante                    **************'
)
print(
    '************* 75 <= puntos      : Estudiante sobresaliente          **************'
)
resp_ok = 0
resp_letras = ('a', 'b', 'c', 'd')
print()
nombre_estudiante = input('Ingresa su primer nombre: ')
print()
print(
    f'''Hola {nombre_estudiante} responde las siguientes preguntas escribiendo la letra de la
alternativa y presionando la tecla enter para enviar tu respuesta. Comienzas el juego con {random.randint(0, 101)} puntos.
''')
print(
    '*****************************************************************************'
)
print()
print(
    f'******************************* ¡Comencemos {nombre_estudiante}! **********************'
)
print()
time.sleep(3)
print('Pregunta N°1')
print()
print(GREEN+'Cual es la derivada de f(x) = 2x^2 + 100'+RESET)
print('''
  a) 2x^2
  b) 4x^2
  c) 4x
  d) 4x + 100
''')
respuesta_1 = input('¿Que alternativa es la respuesta correcta? : ')
if respuesta_1 not in resp_letras:
    while respuesta_1 not in resp_letras:
        respuesta_1 = input(
            'Debes ingresar la letra a, b, c o d. Ingresa nuevamente tu respuesta : '
        )
        if respuesta_1 not in resp_letras:
            continue
          
        if respuesta_1 == 'c':
            print()
            print("¡Correcto!")
            resp_ok += random.randint(0, 101)
        elif respuesta_1 != 'c':
            print()
            print("¡Incorrecto!")
            resp_ok -= random.randint(0, 101)
          

else:
    if respuesta_1 == 'c':
        print()
        print("¡Correcto!")
        resp_ok += random.randint(0, 101)
    else:
        print()
        print("¡Incorrecto!")
        resp_ok -= random.randint(0, 101)

print()

print(
    '*****************************************************************************'
)
print()
print('Pregunta N°2')
print()
print(GREEN+'Cual es la derivada de f(x) = x^(1/2)'+RESET)
print('''
  a) 1/(2x^(1/2))
  b) 0
  c) x/2^(1/2)
  d) x^(1/2)
''')

time.sleep(3)

respuesta_2 = input('¿Que alternativa es la respuesta correcta? : ')
if respuesta_2 not in resp_letras:
    while respuesta_2 not in resp_letras:
        respuesta_2 = input(
            'Debes ingresar la letra a, b, c o d. Ingresa nuevamente tu respuesta : '
        )
        print()
        if respuesta_2 not in resp_letras:
            continue

        if respuesta_2 == 'b':
            print(
                f'¡Incorrecto! {nombre_estudiante} el termino de la función no es una constante'
            )
            resp_ok -= random.randint(0, 101)
        elif respuesta_2 == 'c':
            print(
                f'¡Incorrecto! {nombre_estudiante} revisa el signo del exponente y luego simplifica la expresión'
            )
            resp_ok -= random.randint(0, 101)
        elif respuesta_2 == 'd':
            print(
                f'¡Incorrecto! {nombre_estudiante} no aplica la regla de derivación de función exponencial'
            )
        else:
            print()
            print("¡Correcto!")
            resp_ok += random.randint(0, 101)

else:
    if respuesta_2 == 'b':
        print(
            f'¡Incorrecto! {nombre_estudiante} el termino de la función no es una constante'
        )
        resp_ok -= random.randint(0, 101)
    elif respuesta_2 == 'c':
        print(
            f'¡Incorrecto! {nombre_estudiante} revisa el signo del exponente y luego simplifica la expresión'
        )
        resp_ok -= random.randint(0, 101)
    elif respuesta_2 == 'd':
        print(
            f'¡Incorrecto! {nombre_estudiante} no aplica la regla de derivación de función exponencial'
        )
        resp_ok -= random.randint(0, 101)
    else:
        print()
        print("¡Correcto!")
        resp_ok += random.randint(0, 101)

print()
print(
    '*****************************************************************************'
)
print()
print('Pregunta N°3')
time.sleep(3)
print()
print(GREEN+'Cual es la integral indefinida de S = ∫ x^3 dx'+RESET)
print('''
  a) x^3
  b) 3x^2
  c) x^4/4 
  d) x^4/4 + c
''')
respuesta_3 = input('¿Que alternativa es la respuesta correcta? : ')
if respuesta_3 not in resp_letras:
    while respuesta_3 not in resp_letras:
        respuesta_3 = input(
            'Debes ingresar la letra a, b, c o d. Ingresa nuevamente tu respuesta : '
        )
        if respuesta_3 not in resp_letras:
            continue
          
        if respuesta_3 == 'd':
            print()
            print("¡Correcto!")
            resp_ok += random.randint(0, 101)
        elif respuesta_3 != 'd':
            print()
            print("¡Incorrecto!")
            resp_ok -= random.randint(0, 101)

else:
    if respuesta_3 == 'd':
        print()
        print("¡Correcto!")
        resp_ok += random.randint(0, 101)
    else:
        print()
        print("¡Incorrecto!")
        resp_ok -= random.randint(0, 101)

print()
print(
    '*****************************************************************************'
)
print()
print()
print()
time.sleep(5)

if resp_ok < 50 :
    print(
        '*****************************************************************************'
    )
    print(
        f'**** Gracias {nombre_estudiante} por jugar mi trivia, alcansaste un total de {resp_ok} puntos, eres un estudiante en proceso de aprendizaje *******'
    )
    print(
        '*****************************************************************************'
    )
elif 50 <= resp_ok and  resp_ok < 75:
    print(
        '*****************************************************************************'
    )
    print(
        f'**************** Gracias {nombre_estudiante} por jugar mi trivia, alcansaste un total de {resp_ok} puntos, eres un buen estudiante ****************'
    )
    print(
        '*****************************************************************************'
    )
elif 75 <= resp_ok:
    print(
        '*****************************************************************************'
    )
    print(
        f'************ Gracias {nombre_estudiante} por jugar mi trivia, alcansaste un total de {resp_ok} puntos, eres un estudiante sobresaliente *************'
    )
    print(
        '*****************************************************************************'
    )

print()
print("Fin de la Trivia")
print("Desarrollado por Rober Quispe Ulloa")
