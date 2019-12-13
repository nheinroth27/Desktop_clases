from curses import wrapper
import time
from pprint import pprint


def crear_campo(tam):
    fila=[]
    matriz=[]
    for fil in range(tam):
        fila.append('.')
    for fil in range(tam):
        matriz.append(fila)
    pprint(matriz)   # genera bien 
    return matriz

def movimientos():
    fila=0
    columna=0
    caracter='#'
    if columna>0:   #para no salir de rango  
        matriz[fila][columna-1]="."
        matriz[fila][columna]=caracter
    else:
        matriz[fila][columna]=caracter
        columna+= 1  
    if columna==tamanho:  # verificamos si es que llego al tope la columna
        columna=0  






def main(screen):
    # Clear screen
    screen.clear()
    # This raises ZeroDivisionError when i == 10.
    fila=0  # para los movimientos 
    columna=0  # para los movimientos 
    linea=" "
    caracter="#"
    cambiofila=0
    while True:
        try:
            i=0
            for row in range(tamanho):
                for col in range(tamanho):
                    linea= linea +" "+ matriz[row][col]  # formamos el texto a imprimir
                screen.addstr(i, 0, linea)
                i=i+1
                linea=" "
            screen.refresh() # refrescamos la pantalla
            time.sleep(1)  # pausa  de 1 segundo
            #movimientos()  # llamamos al procedimiento
            
            if columna>0:   #para no salir de rango  
                matriz[fila][columna-1]="."
                matriz[fila][columna]=caracter
            else:
                matriz[fila][columna]=caracter
            columna+= 1  
            if columna==tamanho:  # verificamos si es que llego al tope la columna
                matriz[fila][columna]="."  # para terminar de completar la grilla
                columna=0 
        except KeyboardInterrupt:
            break
            print("pulse una tecla para terminar")
            print(matriz)
            screen.getkey()
    



tamanho=8  # es de 4 por 4 
matriz=crear_campo(tamanho)
wrapper(main)
