# -*- coding: utf-8 -*-

#hago que reconozca las Ñ con ese comentario, me funciona sin el comentario, así que lo hice re al pedo, parece

# importo string para el lowercase, aunque no me funcionó manual, pero cuando usé el comando, se importó
# string automáticamente
import string
from string import ascii_lowercase
# importo librería para enmascarar contraseña
import getpass
# creo una variable con las letras minúsculas sin la ñ
minusculas = string.ascii_lowercase

# acá pido la contraseña, y la dejo en minúsculas de inmediato
contrasenha = getpass.getpass('Ingresa la contraseña: ').lower()
# evito que ingresen una contraseña vacía
while contrasenha == '':
    contrasenha = getpass.getpass('La contraseña no puede estar vacía, intenta nuevamente: ').lower()
# evito que ingresen números:
con_numeros = any(chr.isdigit() for chr in contrasenha)
while con_numeros:
    contrasenha = getpass.getpass('La contraseña no puede tener números, intenta nuevamente: ').lower()
    con_numeros = any(chr.isdigit() for chr in contrasenha)
# pongo un contador para que ingresen una contraseña sin ñ
con_enhe = 1
# hago un ciclo para que pida de nuevo la contraseña si es que detectó que tenía una ñ
while con_enhe > 0:
    for letra in contrasenha:
        if letra == 'ñ':
            con_enhe += 1
    if con_enhe > 1:
        contrasenha = getpass.getpass('Ingresa la contraseña: ').lower()
        con_enhe = 1
    else:
        con_enhe = 0

# hago un contador de intentos y lo inicializo en 0
intentos = 0

# ahora, a lo que vinimos: aplicamos fuerza bruta a la contraseña
for letra in contrasenha:
    for caracter in minusculas:
        intentos += 1
        if letra == caracter:
            break

# ahora, me debe decir en cuántos intentos adivinó la contraseña:
print(f'Adiviné tu contraseña en {intentos} intentos.', end = '\n\n')
# evalúo la seguridad de la contraseña según mi propio estándar y lo hago saber al usuario:
if intentos <= 1000:
    print('Tu contraseña es muy insegura, considera cambiarla.')
else:
    print('Tu contraseña parece segura, aunque igual la adiviné, considera cambiarla.')