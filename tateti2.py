tablero1 = [[0,0,0],
            [0,0,0],
            [0,0,0]]

tablero2 = [["","",""],
            ["","",""],
            ["","",""]]
fin = False
#jugador1 = input ("Ingrese el nombre del jugador 1: ")
#jugador2 = input ("Ingrese el nombre del jugador 2: ")

def validar_ganador (tab):
        d1 = 0
        d2 = 0
        lista_contadores = [0,0,0]
        cont = 0
        for f in range (3):
                cont = 0
                for c in range(3):
                        if f == c and tab[0][0] != 0:
                                d1 += 1
                        if f + c == 2 and tab [0][2] != 0:
                                d2 += 1
                        if tab[cont][c] == tab[f][c]: #and tab [cont][0] != 0
                                lista_contadores[cont]+= 1
                        cont += 1
        if d1 == 3:
                if tab[0][0] == 1:
                        print ("gano jugador 1")
                else:
                        print ("gano jugador 2")
        elif d2 == 3:
                if tab[0][2] == 1:
                        print ("gano jugador 1")
                else:
                        print ("gano jugador 2")
        ch = 0
        for h in lista_contadores:
                if h == 3:
                        if tab[ch][0] == 1:
                                print ("gano jugador 1")
                        else:
                                print ("gano jugador 2")
                ch += 1

validar_ganador(tablero1)              

                         
'''
def print_tablero (un_tablero):
        conta = 0 
        print ("   0  1  2")
        for fila in un_tablero:
                print (conta, fila)
                conta = conta + 1

print_tablero (tablero2)

k = 1
while fin == False:
        if k % 2 == 0:
                print ("Turno de ", jugador1)
                fila = input ("Asigne la fila ")
                columna = input ("Asigne la columna ")
                if tablero1[fila][columna] == 0:
                        tablero1[fila][columna] == "x"
                validar_ganador(tablero1)
        else:
                print ("Turno de ", jugador2)
                fila = input ("Asigne la fila ")
                columna = input ("Asigne la columna ")
                if tablero1[fila][columna] == 0:
                        tablero1[fila][columna] == "o"
                validar_ganador(tablero1)
        '''
                


