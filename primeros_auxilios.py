# solicitar que verifique si responde a estímulos
estimulos = input('¿Responde a Estimulos? [y/n]\n').lower()

if estimulos == 'y':
    print(f' Valorar la necesidad de llevarlo al hospital más cercano '.center(70, '='), end='\n\n')
else:
    print(f'Abrir la vía Aérea.'.center(70, '='), end='\n\n')
    respira = input('¿Respira? [y/n]\n').lower()

    if respira == 'y':
        print(f' Permitirle posición de suficiente ventilación '.center(70, '='), end='\n\n')
    else:
        print(f' Administrar 5 ventilaciones y llamar a Ambulancia '.center(70, '='), end='\n\n')


        # inicializar el valor de ambulancia, lo que permite recorrer al menos una vez el ciclo
        ambulancia = 'n'

        while ambulancia == 'n':
            signos = input('¿Tiene signos de vida?[y/n]\n').lower()

            if signos == 'y':
                print(f' Reevaluar a la espera de la Ambulancia '.center(70, '='), end='\n\n')
            else:
                print(f' Administrar Compresiones Torácicas hasta que llegue la Ambulancia '.center(70, '='), end='\n\n')

            ambulancia = input('¿Llegó la ambulancia? [y/n]\n')

print(f''.center(70, '='))
print(f' Programa Terminado '.center(70, '='))
print(f''.center(70, '='))