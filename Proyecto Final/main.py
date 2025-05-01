#Proyecto de Kenneth Arias Solís 
#Sistema de organizacion de inventario

#importaciones
import os
import pandas as pd

from modulo import agregar_movimiento, guardar_movimientos, analisis_movimientos


#Funciones
def pause():
    input("\nPresione ENTER para continuar...")
    

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


#Menú principal
def menu():
    print("\nBienvenido al Sistema de organizacion de Inventario")
    
    #Variables del sistema
    movimientos = []
    
    while(True):
        print('\n--- Sistema de Ventas de Ferretería ---')
        print('1. Agregar movimientos a la memoria')
        print('2. Guardar datos en un archivo CSV')
        print('3. Analizar los datos')
        print('4. Salir')
        opcion = input('Ingrese una opción: ')

        if opcion == "1":
            print('\n------ Agregando movimiento ------')
            agregar_movimiento(movimientos)
            print(*movimientos)
            pause()

        elif opcion == "2":
            print('\n---- Guardar datos en un archivo CSV ----')
            guardar_movimientos(movimientos)
            pause()

        elif opcion == "3":
            limpiar_pantalla()
            analisis_movimientos()
            pause()

        elif opcion == "4":
            print('\nMuchas gracias por usar el programa!!')
            pause()
            break
        
        else:
            print('Opcion no valida, vuelva a intenterlo')
            pause()
            
            
if __name__ == '__main__':
    limpiar_pantalla()
    pause()
    menu()