from definiciones import *
from arimaaEjExtras import *

def posiciones_de_las_piezas(j:Juego)->dict[Pieza,list[Posicion]]:
    '''
    PRE: { juego_bien_formado(j)}
    Args: 
        j (Juego): representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                    donde el tablero *t* es el actual del juego,
                    el color *turno* es el del jugador al que le toca jugar 
                    y *pasosConsumidos* es el numero entero de pasos ya efectuados.

        returns: devuelve un diccionario con las posiciones de cada pieza 
    '''
    res: dict[Pieza,list[Posicion]] ={}
    t:Tablero = j.tablero

    for f in range(ALTO):
        for c in range(ANCHO):
            pos: Posicion = Posicion(f,c)
            casilla: Casilla = t[f][c] # puede ser o vacio o pieza 

            if not hay_casilla_vacia(t, pos):
                pieza: Pieza = casilla # me aseguro que la la clave del dict sea de tipo pieza

                if pieza not in res: # si no esta la inicializo (pieza existe solo si no esta vacia)
                    res[pieza] = [] # creo una lista vacia 

                res[pieza].append(pos) # sumo a la lista vacia previamente creada la pos de la pieza actual que no es vacia

    return res

def movimientos_x_pos(j: Juego, pos: Posicion) -> list[Movimiento]:
    listaDeMovimientos: list[Movimiento] = []
    ds: list[Direccion] =[NORTE,SUR,ESTE,OESTE]

    #MOVER A SECAS
    for d in ds:
        m: Movimiento = Movimiento( MOVER_A_SECAS, pos , [d])
        if puede_realizar_movimiento(j, m):
            listaDeMovimientos.append(m)

    #ARRASTRAR
    for d1 in ds:
        for d2 in ds:
            m: Movimiento = Movimiento( ARRASTRAR, pos , [d1,d2])
            if puede_realizar_movimiento(j, m):
                        listaDeMovimientos.append(m)

    #EMPUJAR
    for d1 in ds:
            for d2 in ds:
                m: Movimiento = Movimiento( EMPUJAR, pos , [d1,d2])
                if puede_realizar_movimiento(j, m):
                            listaDeMovimientos.append(m)
    
    return listaDeMovimientos



def todos_los_movimientos_posibles(j: Juego) -> list[Movimiento]:
    '''
    PRE: {juego_bien_formado(j)}
    Args: j (Juego) :   representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                        donde el tablero *t* es el actual del juego,
                        el color *turno* es el del jugador al que le toca jugar 
                        y *pasosConsumidos* es el numero entero de pasos ya efectuados.

    Returns: una lista con todos los posibles movimientos validos por cada pieza del jugador de turno. 

    '''
    res: list[Movimiento] = []
    posiciones: dict[Pieza,list[Posicion]] = posiciones_de_las_piezas(j)
    turno:Color = j.turno

    for pieza in posiciones:
        if turno == pieza.color:

            for pos in posiciones[pieza]:
                movimientos = movimientos_x_pos(j,pos)

                for m in movimientos:
                    if m not in res:
                        res.append(m)

    return res
                            


