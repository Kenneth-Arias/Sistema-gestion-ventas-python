import pandas as pd
import csv, os

def agregar_movimiento(lista_herramientas):
    #Leer los datos
    while True:
        try: 
            herramienta = input('\nÍngrese el nombre del producto: ').upper()
            cantidad = int(input('Ingrese la cantidad: '))
            fecha = input('Íngrese la fecha de ingreso del producto (AAAA-MM-DD): ')
            precio = float(input('Íngrese el precio del producto: '))
            cliente = input('Ingrese el nombre del cliente: ')
        except ValueError:  
            print('Entradas no validas, por favor intetenlo nuevamente!')
            continue
    
        memoria = {
            'herramienta' : herramienta,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
            'cliente' : cliente
        }
         
        lista_herramientas.append(memoria)
        
        #Volver a ingresar una herramienta nueva
        continuar = input('Desea ingresar otra herramienta s/n :').lower()
        if continuar == 's':
            print('\n---- Ingresando otra herramienta ----')
        elif continuar == 'n':
            break
        else: 
            print ('Opción no valida')

#Guardar archivo

def guardar_movimientos(movimientos):
    if not movimientos:
        print('No hay movimientos que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #si el archivo existe agrego Append  'A'
            with open('movimientos.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['herramienta','cantidad','precio','fecha', 'cliente'])
                guardar.writerows(movimientos)        
        else: #Si no existe abro en modo escritura 'W'
            with open('movimientos.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['herramienta','cantidad','precio','fecha', 'cliente'])
                guardar.writeheader()
                guardar.writerows(movimientos)
                
        movimientos = []
        print('\nDatos guardados exitosamente!')
        
#Analisis de Ventas        
  
def analisis_movimientos():
    df = pd.read_csv('movimientos.csv')
    reader = csv.DictReader('movimentos.csv')
    print('\n----------------- RESUMEN VENTAS -----------------')
    
    #Total de ventas
    df['subtotal'] = df['cantidad'] * df['precio']
    total_ingresos = df['subtotal'].sum()
    
    print(f'\n1. TOTAL de ventas {total_ingresos:.2f}')
    
    #Herramienta más vendida
    herramienta_top = df.groupby('herramienta')['cantidad'].sum().idxmax()
    print('2. La herramienta más vendida es : ', herramienta_top)
    
    #Mejor cliente
    cliente_top = df.groupby('cliente')['cantidad'].sum().idxmax()  
    print(f'3. Cliente con más compras: {cliente_top}')
    
    #Ventas por fecha
    ventas_por_fecha = df.groupby('fecha')['subtotal'].sum()
    print('\n----------------- VENTAS POR FECHA -----------------')
    print(ventas_por_fecha)
    