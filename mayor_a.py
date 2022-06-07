# importamos sys para poder pasar el argumento al ejecutar programa por terminal
import sys

#solicitamos el ingreso de datos, según solicitado en ejercicio
valor_superior = int(sys.argv[1])

# diccionario provisto:
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

#recorrer el diccionario
for mes, valor in ventas.items():
    #comparar el value con el valor solicitado al usuario
    if valor > valor_superior:
        #imprimir el mes y el valor
        print(mes, valor)

#darle un toque personal para cerrar el programa:
print(f''.center(50, '='))


# una solución alternativa, pero que imprime en una sola línea, es:
# print({k:v for k,v in ventas.items() if v > valor_superior})
# donde k corresponde a key, v a value