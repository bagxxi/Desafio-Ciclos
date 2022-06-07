# importando librerias
import math

#pasamos los digitos para la multiplicación
secuencia = [2, 3, 4, 5, 6, 7]
# como la secuencia se reinicia si es que hay más números, se multiplica por dos
secuencia *= 2
# solicitamos el rut y lo invertimos de inmediato, para hacer el cálculo
invertir_rut = input('¡Hermano, grita tu RUT, sin puntos ni DV!: ')[::-1]
largo_rut = len(invertir_rut)
# multiplicamos cada digito del rut por la secuencia inicial
resultado = [int(n) * d for d, n in zip(secuencia[:largo_rut], invertir_rut)]
# hacemos el módulo 11, o sea, el resto de la suma del resultado dividido por 11
modulo_once = sum(resultado) % 11
digito_verificador = 11 - modulo_once

# aplicamos las reglas del algoritmo
if digito_verificador == 10:
    digito_verificador = 'K'
elif digito_verificador == 11:
    digito_verificador = 0
# PASO 7
print(f'El dígito verificador del rut ingresado es {digito_verificador}')