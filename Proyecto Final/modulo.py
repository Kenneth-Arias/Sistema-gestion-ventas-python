import pandas as pd
import csv, os

def agregar_movimiento(lista_herramientas):
    #Leer los datos
    while True:
        try: 
            herramienta = input('\nÍngrese el nombre del producto: ').upper()
            movimiento = input('Entrada o salida: ').lower()
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
            'cliente' : cliente,
            'movimiento' : movimiento
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
                guardar = csv.DictWriter(archivo,fieldnames=['herramienta','cantidad','precio','fecha', 'cliente', 'movimiento'])
                guardar.writerows(movimientos)        
        else: #Si no existe abro en modo escritura 'W'
            with open('movimientos.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['herramienta','cantidad','precio','fecha', 'cliente', 'movimiento'])
                guardar.writeheader()
                guardar.writerows(movimientos)
                
        movimientos = []
        print('\nDatos guardados exitosamente!')
        
#Analisis de Ventas        
  
def analisis_movimientos():
    df = pd.read_csv('movimientos.csv')
    reader = csv.DictReader('movimentos.csv')
    
    df['subtotal'] = df['cantidad'] * df['precio']
    ventas = df[df['movimiento'].str.lower() == 'salida']
    
    print('\n----------------- RESUMEN VENTAS -----------------')
    
    #Total de ingresos por ventas (salida)
    ventas = df[df['movimiento'].str.lower() == 'salida']
    total_ventas = ventas['subtotal'].sum()
    print(f'1. Total de ingresos por ventas (salida): ${total_ventas:.2f}')

    #Total de egresos por compras (entrada)
    compras = df[df['movimiento'].str.lower() == 'entrada']
    total_compras = compras['subtotal'].sum()
    print(f'2. Total de egresos por compras (entrada): ${total_compras:.2f}')

    #Herramienta más vendida
    herramienta_top = df.groupby('herramienta')['cantidad'].sum().idxmax()
    print('3. La herramienta más vendida es : ', herramienta_top)

    #Mejor cliente
    if 'cliente' in df.columns and not ventas.empty:
        cliente_top = ventas.groupby('cliente')['cantidad'].sum().idxmax()
        print(f'4. Cliente con más compras: {cliente_top}')

    #Ventas por fecha
    ventas_por_fecha = df.groupby('fecha')['subtotal'].sum()
    print('\n----------------- VENTAS POR FECHA -----------------')
    print(ventas_por_fecha)
    
    stock = pd.Series(dtype=int)
    for _, row in df.iterrows():
        nombre = row['herramienta']
        cant = row['cantidad']
        mov = row['movimiento'].strip().lower()
        if pd.isna(cant):
            continue
        if nombre not in stock:
            stock[nombre] = 0
        if mov == 'entrada':
            stock[nombre] += cant
        elif mov == 'salida':
            stock[nombre] -= cant

    print('\n-------- REVISION DE STOCK --------')
    for herramienta, cantidad in stock.items():
        print(f'- {herramienta}: {cantidad} unidades')
        if cantidad < 5:
            print(' Pocas existencias.')
        elif cantidad > 50:
            print(' Exceso de inventario.')
    
