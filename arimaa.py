from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)



def copiar_tablero(t : Tablero) -> Tablero:
    """
    PRE: {True}
    Args: 
        t (Tablero) : es una lista de lista de casillas sobre el cual se quiere realizar una copia.

    Returns: devuelve un tablero nuevo *copia*, el cual contiene los mismos elementos que el tablero *t* que el dado
    """
    
    copia : Tablero = []
    for fila in t:
         copia.append(fila.copy())
    return copia



#### Ejercicio 1


# Explicacion: esta funcion busca decidir (es True o False) si un tablero (una lista de listas, ver en ejemplo_tablero) es valido. 
# Es valido, devuelve True, si el tablero es la tiene una cantidad ALTO de filas (la longitud del tablero es ALTO) 
# y cada fila tiene la longitud ANCHO

def tablero_bien_formado(t : Tablero) -> bool:
        """
        Indica si el tablero ingresado tiene una cantidad 8 de filas y cada fila tiene la longitud 8. #preguntar pongo ancho/alto o 8 

        PRE: {True}
        Args:
            t (Tablero) : es una lista de lista de casillas sobre la que se quiere definir si esta bien formada.

        Returns:
            True ←→ todas las filas en el tablero *t* son 8 y todas las casillas dentro de cada fila tambien es 8.
        """
        esTableroBienFormado: bool = False

        if len(t) == ALTO:
                for fila in t:
                        if len(fila) == ANCHO:
                               esTableroBienFormado = True
                        else: 
                              return False  
        else: 
                return False

        return esTableroBienFormado



# Explicacion: esta funcion busca decidir (es True o False) si una poscicion: pos = (fila,columna) pertenece al tablero del juego
# es True si la parte de filas en pos (pos.fila -> pos[0]) esta entre 0 y el alto 
# Y si la parte de columnas en pos (pos.columna -> pos[1]) esta entre 0 y el ancho

def posicion_en_tablero(pos : Posicion) -> bool:
    """
    Indica si la posicion *pos* dada esta dentro del tablero de juego.
    
    PRE: {True}
    Args: 
        pos (Posicion) : es una variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente sobre la cual se quiere analizar.

    Returns:
        True ←→ la primera y segunda componente de posicion *pos* estan en el rango [0,8).
    
    """
    if (0 <= (pos.fila) < ALTO) and (0 <= (pos.columna) < ANCHO): # si la pos pertenece al tablero...
        return True
    
    else: 
        return False


# Explicacion: esta funcion busca decidir (es True o False) si un movimiento: (accion, poscicion, direcciones) es valido
# con accion = MOVER_A_SECAS -> muevo mi pieza en UNA sola direccion 
          # o  ARRASTRAR ->  muevo mi pieza a una direcion y "tiro" (hacia atras) de la pieza de mi opnente hacia la direccion que decida
          # o  EMPUJAR ->  muevo mi pieza a una direccion y "empujo" (hacia adelante) a la pieza de mi opnente en la direccion que decida
# con poscicion = tupla de (fila, columna) que dice la fila donde esta mi pieza, el origen de mi pieza
# con dirreciones = lista de NORTE,SUR,ESTE,OESTE que dice 1ero a donde muevo MI pieza y en la 2da a donde muevo la pieza OPONENTE

# devuelve True si la poscion donde esta mi pieza por mover pertenece al tablero (m.origen: Poscion = (fila, columna))
# Y dependiendo el caso:
# si la accion es MOVER_A_SECAS su lista de direciones(m.pasos) debe contener SOLO UNA direcion ( a donde me voy a mover)
# o si la accion es ARRASTRAR su lista de direciones(m.pasos) debe contener DOS direciones ( 1: a donde me voy a mover) ( 2: a donde muevo al oponente)
# o si la accion es EMPUJAR su lista de direciones(m.pasos) debe contener DOS direciones ( 1: a donde me voy a mover) ( 2: a donde muevo al oponente)

def movimiento_bien_formado(m : Movimiento) -> bool:
    """
    Indica si el movimiento *m* dado esta bien formado.
        
    PRE: {True}
    Args:
        m (Movimiento) : representa un movimiento como una tripla (accion (Acción), origen (Posicion), pasos (list[Direccion])), la cual se quiere revisar que este o no bien formada. 
    
    Returns: True ←→ posicion_en_tablero(origen) == True ∧  (m. acción = Mover_a_secas → |m. pasos| = 1) ∧ (m. acción = Arrastrar → |m. pasos| = 2) ∧ (m. acción = Empujar → |m. pasos| = 2).
    """

    if posicion_en_tablero(m.origen):
        if m.accion == MOVER_A_SECAS and len(m.pasos) == 1:
                return True
        
        elif m.accion == ARRASTRAR and len(m.pasos) == 2:
                return True
        
        elif m.accion == EMPUJAR and len(m.pasos) == 2: 
                return True
    
    return False



# Explicacion: esta funcion decide (es True o False) si un juego: (tablero, color, pasosConsumidos) esta bien formado 
# donde color representa a que jugador le toca jugar y pasosConsumidos es el numero (int) de pasos que ya se hizo por el jugador de ese color en el turno actual
# se revisa si el tablero esta bien formado Y si la cantidad de pasos es menor a 4 

def juego_bien_formado(j : Juego) -> bool:
    """
    Indica si un juego *j* dado esta bien formado.

    PRE: {True}
    Args:
        j (Juego) : representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                    donde el tablero *t* es el actual del juego,
                    el color *turno* es el del jugador al que le toca jugar, 
                    y *pasosConsumidos* es el numero entero de pasos ya efectuados.
    
    Returns: True ←→ tablero_bien_formado(t) == True ∧ *pasosConsumidos* <= 4
    """
    return tablero_bien_formado(j.tablero) and (0 <= j.pasos_consumidos < MAX_PASOS)




#### Ejercicio 2


# Explicacion: esta funcion devuelve una pos_vecina: (fila,columna) en una direccion "d" respecto a una pos: (fila,columna) dada
# entonces si:
# d = NORTE debe devolver el vecino de arriba -> pos_vecina es (fila + 1, columna)
# d = SUR debe devolver el vecino de abajo -> pos_vecina es (fila - 1, columna)
# d = ESTE debe devolver el vecino de la derecha -> pos_vecina es (fila, columna + 1)
# d = OESTE debe devolver el vecino de la izquierda -> pos_vecina es (fila, columna - 1)

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
    PRE: {True}
    Args:
        j (Juego) : representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                    donde el tablero *t* es el actual del juego,
                    el color *turno* es el del jugador al que le toca jugar 
                    y *pasosConsumidos* es el numero entero de pasos ya efectuados
    
    Returns:  devuelve la posicion vecina *pos_vecina: Posicion* de la posicion *pos* dada, la cual cumple con 
              (d = Norte → (pos_vecina.fila = pos.fila + 1    ∧    pos_vecina.columna = pos.columna ))
            ∧ (d = Sur →   (pos_vecina.fila = pos.fila - 1    ∧    pos_vecina.columna = pos.columna ))
            ∧ (d = Este →  (pos_vecina.fila = pos.fila        ∧    pos_vecina.columna = pos.columna + 1))
            ∧ (d = Oeste → (pos_vecina.fila = pos.fila        ∧    pos_vecina.columna = pos.columna - 1))
    """

    if   d == NORTE:
        resultado: Posicion  = Posicion(pos.fila +1, pos.columna)
    elif d == SUR:
         resultado = Posicion(pos.fila - 1, pos.columna)
    elif d == ESTE:
         resultado = Posicion(pos.fila, pos.columna + 1)
    else:
        resultado = Posicion(pos.fila, pos.columna - 1)

    return resultado



# Explicacion: esta funcion da la casilla de la poscion dentro del tablero
# se busca que hay en la posicion t[fila][columna] y devuelve una c: Casilla (puede ser vacio o pieza: (figura, color) )

def casilla_en_posicion(t : Tablero, pos : Posicion) -> Casilla:
    """
        PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) == True }
        Args: 
            t (Tablero) : una lista de lista de casillas.
            pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, sobre la cual se quiere definir su casilla en el tablero *t*.
            
        Returns: devuelve una Casilla *c* la cual refiere a la posicion *pos* dada en el tablero *t*
    """

    c: Casilla = t[pos.fila][pos.columna]

    return c



# Explicacion: decide (True o False) dada una pos: (fila,columna) revisa si en el tablero t[fila][columna] es vacia 
# si esa casilla (c: casilla = t[fila][columna] ) es vacia devuelve True

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    """
        PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) == True }
        Args: 
            t (Tablero) : una lista de lista de casillas.
            pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                             sobre la cual se quiere definir si su casilla en el tablero *t* esta vacia o no.
            
        Returns: True ←→ la Casilla *c*, la cual refiere a la posicion *pos* dada en el tablero *t*, es vacia. 
    """

    c: Casilla = t[pos.fila][pos.columna]

    return (c == VACIA)



# Explicacion: decide (es True o False) si en la poscicion pos en el tablero hay una pieza Y es del color dado

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
        PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) == True }
        Args: 
            t (Tablero) : una lista de lista de casillas.
            pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                             sobre la cual se quiere definir si su casilla en el tablero *t* tiene una Pieza del color *col* dado.
            col (Color) : la variable refiere a PLATEADO o DORADO. 
            
        Returns: True ←→ si la Casilla *c*, la cual refiere a la posicion *pos* dada en el tablero *t*, no es vacia y el color de su figura es igual al color *col* dado. 
    """

    c: Casilla = t[pos.fila][pos.columna]

    return ( not (hay_casilla_vacia(t,pos)) and ( c.color == col ) )




#### Ejercicio 3


# Explicacion: decide (es True o False) si hay una casilla vacia en una direccion particular dada
# Para ello buscamos la posicion vecina en esa direccion y con esa pos_vecina evaluamos si es que su casilla es vacia o no 

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
        PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) == True }
        Args: 
            t (Tablero) : una lista de lista de casillas.
            pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                             sobre la cual se quiere definir si su casilla vecina dentro del tablero *t* en una direccion *d* particular esta vacia o no.
            
        Returns: True ←→ la casilla vecina en la direccion *d* de la poscicion *pos*  dada , esta en el tablero *t* y es vacia. 
    """
    pos_vecina: Posicion = posicion_vecina_hacia(pos,d)
    
    if posicion_en_tablero(pos_vecina) and hay_casilla_vacia(t, pos_vecina):  
        return  True
    
    return False



# Explicacion: esta funcion decide (es True o False) si existe alguna pieza en alguna direccion (norte,sur,este,oeste)
# tal que esa pieza es del mismo color que la pieza en la posicion ingresada.
# Para eso, buscamos revisar cada vecino en cada direccion. Al revisar comparamos el color del vecino con el color de la pos ingresada.
# al primer vecino en la primera direccion que se encuentra se devuelve True

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    """
        PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) == True }
        Args: 
            t (Tablero) : una lista de lista de casillas.
            pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                             sobre la cual se quiere definir si tiene alguna casilla vecina en el tablero *t* con una Pieza del mismo color que del de la posicion *pos* dada.
            
        Returns: True ←→ si existe alguna casilla vecina en el tablero *t* respecto a la posicion *pos* dada, tal que esa casilla no es vacia y el color de su figura es igual al color de la posicion *pos* dada. 
    """

    
    ds: list[Direccion] = [NORTE,SUR,ESTE,OESTE]
  
    if not(hay_casilla_vacia(t,pos)):
        c: Casilla = t[pos.fila][pos.columna]
        col: Color = c.color

        for d in ds:
            pos_vecina: Posicion = (posicion_vecina_hacia(pos,d))
            if posicion_en_tablero(pos_vecina) and not ( hay_casilla_vacia(t,pos_vecina)):
                c_vecina: Casilla = t[pos_vecina.fila][pos_vecina.columna]
                pieza: Casilla = c_vecina    
                if pieza.color == col:
                    return True

    return False



# Explicacion:  dada una pos: Posicion(fila,columna) donde hay una pieza (es decir, no es vacia) 
# decide (es True o False) si es que hay una pieza enemiga (del otro color) en una direccion particular: d y 
# esta tiene menor fuerza que la fuerza de la pieza en la pos ingresada.
# Para hacerlo se busca el color y la fuerza de la pos_vecina en la direccion d ingresada.
# De pertenecer al tablero pos_vecina, comparamos el color a ver si es enemiga, y si lo es comparamos su fuerza.
# En el caso de ser enemiga y de fuerza menor se devuelve True sino devuelve False

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
            PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) ∧ ¬hay_casilla_vacia(pos) == True }
            Args: 
                t (Tablero) : una lista de lista de casillas.
                pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                                 sobre la cual se quiere definir si tiene una casilla vecina dentro del tablero *t* en una direccion particular con una pieza del color contrario y de menor fuerza respecto a la posicion *pos* dada.
                
            Returns: True ←→ si existe una casilla vecina a la posicion *pos* dada dentro del tablero *t* en la direccion *d* particular, tal que esa casilla tiene una figura de contrario color y de menor fuerza respecto a la posicion *pos* dada.
    """
    

    casilla_pos: Casilla = t[pos.fila][pos.columna]
    figura_pos: Figura = casilla_pos.figura
    fuerza_pos: int = fuerza(figura_pos)

    pos_vecina: Posicion = posicion_vecina_hacia(pos,d)

    if posicion_en_tablero(pos_vecina) and not hay_casilla_vacia(t, pos_vecina):
        casilla_vecina: Casilla = t[pos_vecina.fila][pos_vecina.columna]
        figura_vecina: Figura = casilla_vecina.figura
        fuerza_vecina = fuerza(figura_vecina)
    
        if (casilla_vecina.color != casilla_pos.color) and (fuerza_pos > fuerza_vecina):
                return True
                
    return False



# Explicacion: la funcion decide (es True o False) si existe una pieza enemiga mas fuerte al rededor de la pieza en la pos ingresada 
# para eso definimos variables sobre la pos ingresada (su color, su fuerza), 
# luego por direccion en la lista de direcciones ("ds") buscamos el vecino en esa d y comparamos colores para buscar enemigos
# al hallar el vecino enemigo comparamos sus fuerzas, si la fuerza del enemigo es mayor a la fuerza de la figura en la pos ingresada entonces devolvemos True


def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    """
            PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) ∧ ¬hay_casilla_vacia(pos) == True }
            Args: 
                t (Tablero) : una lista de lista de casillas.
                pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                                 sobre la cual se quiere definir si tiene alguna casilla vecina dentro del tablero *t* con una pieza del color contrario y de menor fuerza respecto a la posicion *pos* dada.
                
            Returns: True ←→ si existe alguna casilla vecina a la posicion *pos* dada dentro del tablero *t*, tal que esa casilla tiene una figura de contrario color y de menor fuerza respecto a la posicion *pos* dada.
    """


    c_pos: Casilla = t[pos.fila][pos.columna]
    f_pos: Figura = c_pos.figura
    col_pos: Color = c_pos.color
    fuerza_pos: int = fuerza(f_pos)
    
    ds: list[Direccion] = [NORTE,SUR,ESTE,OESTE]

    for d in ds:
        pos_vecina_d: Posicion = posicion_vecina_hacia(pos,d)
        if posicion_en_tablero(pos_vecina_d):            
            if not(hay_casilla_vacia(t,pos_vecina_d)):
                c_vecina_d: Casilla = t[pos_vecina_d.fila][pos_vecina_d.columna]
                f_vecina_d: Figura = c_vecina_d.figura 
                fuerza_vecina_d: int = fuerza(f_vecina_d)
                
                if not(hay_pieza_de_color(t, pos_vecina_d, col_pos))  :
                    if fuerza_vecina_d > fuerza_pos:
                        return True

    return False 



# Explicacion: esta funcion decide ( es True o False) si una pos se encuentra congelada 
# Para eso, se revisa si es o no vacia la casilla de esa pos. 
# Luego si hay una pieza vecina enemiga mas fuerte Y no hay una pieza amiga vecina, entonces devuelve True (sino devuelve False)

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    """
            PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) == True }
            Args: 
                t (Tablero) : una lista de lista de casillas.
                pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                                 sobre la cual se quiere definir de tener alguna pieza en el tablero *t*, si esta congeladoa o no. 
                
            Returns: True ←→ si la pieza de la posicion *pos* dada esta o no congelada. 
    """

    if not( hay_casilla_vacia(t, pos)):
         if hay_pieza_enemiga_mas_fuerte_vecina(t, pos) and not(hay_pieza_amiga_vecina(t,pos)):
              return True

    return False



#### Ejercicio 4


# Explicacion: la funcion decide ( es True o False) si la direccion de un movimiento esta habilitada 
# Para eso, declara las variables pieza, f: figura, col: color y revisa 
# si la pieza es conejo y dorado NO puede ir al sur
# si la pieza es conejo y plateado NO puede ir al norte

def direcciónDeMovimientoHabilitada(t: Tablero, pos: Posicion, d: Direccion) -> bool: #auxiliar
    """
        PRE: { tablero_bien_formado(t) == True ∧  posicion_en_tablero(pos) == True }
        Args: 
            t (Tablero) : una lista de lista de casillas.
            pos (Posicion) : variable que refiere a una fila (int) en su primer componente y a una columna (int) en su segunda componente, 
                             sobre la cual se quiere definir si su casilla se puede mover o no en una direccion *d* particular. 
            d (Direccion): direccion sobre la que se quiere concluir si se puede mover o no. 

        Returns: True ←→ si es que hay una pieza en la posicion *pos* dentro del tablero *t* 
                             ∧ ((f = Conejo ∧ col = Dorado ) → d ̸= Sur ) ∧ ((f = Conejo ∧ col = Plateado ) → d ̸= Norte )
    """

    if (hay_casilla_vacia(t,pos)):
        return False

    pieza: Casilla = t[pos.fila][pos.columna]
    f: Figura = pieza.figura
    col: Color = pieza.color

    if (f == CONEJO) and (col == DORADO) and (d == SUR):
            return  False
    elif (f == CONEJO) and (col == PLATEADO) and (d == NORTE):
            return  False

    return True 


# Explicacion: la funcion decide ( es True o False) si la accion de un movimiento se puede realizar
# Para eso, declara las variables accion, d: dirreccion y revisa 
# si la accion es MOVER_A_SECAS y la direccion a la que quiero mover mi pieza esta vacia                                          -> se puede (=True)
# si la accion es ARRASTRAR y hay una casilla vacia en la direccion a la que quiero mover mi pieza 
# Y hay una pieza enemiga mas debil en la posicion opuesta a la que quiero arrastrar                                              -> se puede (=True)
# si la accion es EMPUJAR (ultima opcion), se busca la pos vecina en la direccion ()"d"), 
# si no esta vacia entonces revisa si es mas debil Y si hay una casilla vacia a donde voy a empujar a la otra pieza ("d_empuje")  -> se puede (=True)

def puedeRealizarAcción(t: Tablero, m: Movimiento) -> bool: #auxiliar
    """
        PRE: { tablero_bien_formado(t) == True ∧  movimiento_bien_formado(m) == True }
        Args: 
            t (Tablero) : una lista de lista de casillas.
                

        Returns: True ←→ ( m.accion == MOVER_A_SECAS -> hay casilla vacia en la posicion de la direccion 
                                                        a donde quiero ir (m.pasos[0]) ) dentro del tablero *t* )                     
                         ∧
                         ( m.accion == ARRASTRAR -> hay una casilla vacia en la posicion de la direccion
                                                    a donde quiero ir (m.pasos[0]) dentro del tablero *t*                    
                                                    ∧                       
                                                    hay una pieza enemiga mas debil en la posicion de la direccion opuesta a donde quiero arrastrar
                                                    (opuesta(m.pasos[1]) ) 
                         ∧
                         ( m.accion == EMPUJAR -> hay una casilla vacia en la posicion de la direccion
                                                  a donde quiero ir (m.pasos[0]) dentro del tablero *t*  
                                                  ∧
                                                  la posicion en la direccion en donde quiero empujar al enemigo (m.pasos[1]) esta dentro del tablero *t* 
                                                  ∧
                                                  hay pieza enemiga mas debil_hacia en la posicion a la que quiero ir 
                                                  ∧
                                                  hay una casilla vacia en donde quiero empujar al enemigo )

    """
    pos: Posicion = m.origen 
    accion: Accion = m.accion
    d: Direccion = m.pasos[0]

    pos_hacia: Posicion = posicion_vecina_hacia(pos,d)

    if posicion_en_tablero(pos_hacia):
        
        if accion == MOVER_A_SECAS:
            return hay_casilla_vacia_hacia(t, pos, d)

        elif accion == ARRASTRAR :
            d_arrastre: Direccion = m.pasos[1]
            
            return  (hay_casilla_vacia_hacia(t,pos,d)) and (hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(d_arrastre)))
                 

        else:
            d_empuje: Direccion = m.pasos[1]
            pos_enemiga_empuje: Posicion = pos_hacia
            pos_empuje: Posicion = posicion_vecina_hacia(pos_enemiga_empuje,d_empuje)

            if not(posicion_en_tablero(pos_empuje)):   
                    return False
            
            return  (  (hay_pieza_enemiga_mas_debil_hacia(t,pos,d)) and (hay_casilla_vacia_hacia(t, pos_enemiga_empuje, d_empuje))  )
                      

    return False


# Explicacion: en esta funcion se decide (es True o False) si un movimiento se puede realizar. 
# Para ello, se usan las funciones auxiliares previamente definidas (direcciónDeMovimientoHabilitada y puedeRealizarAcción)
# primero definimos el color del turno al que le toca jugar, luego definimos la pos donde esta mi pieza en la que voy a inicializar el movimiento
# despues si hay una pieza del color del turno en esa posicion origen y esa pieza no esta congelada, 
# se revisa si la direccion del movimiento es valida Y si los pasos consumidos junto a los pasos que voy a hacer (mover 1 o 2 piezas) no se pasan de 4 Y si se puede realizar la accion

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:      # juego = ( tablero, turno, pasosConsumidos)
    """
    PRE: {juego_bien_formado(j) == True ∧ movimiento_bien_formado(m) == True}
    Args: 
        j (Juego) : representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                    donde el tablero *t* es el actual del juego,
                    el color *turno* es el del jugador al que le toca jugar 
                    y *pasosConsumidos* es el numero entero de pasos ya efectuados
        m (Movimiento) : representa un movimiento como una tripla (accion (Acción), origen (Posicion), pasos (list[Direccion])), sobre la cual se quiere revisar 
                         si se puede realizar el movimiento o no 
    
    Returns: True ←→  hay una pieza no congelada del color *turno* en la posicion *origen* del movimiento
                      ∧ direcciónDeMovimientoHabilitada(j. tablero , m. origen , m. pasos [0]) == True
                      ∧ j.pasosConsumidos + |m.pasos| ≤ 4
                      ∧ puedeRealizarAcción(j. tablero , m) == True
    """
    
    turno : Color = j.turno
    t: Tablero = j.tablero
    pos: Posicion = m.origen  # m.origen -> (fila_origen, columna_origen)
    ds: list[Direccion] = m.pasos

    if not(hay_casilla_vacia(t,pos)) and (hay_pieza_de_color(t, pos, turno)) and (not(hay_pieza_congelada(t, pos))) :
           if direcciónDeMovimientoHabilitada(t, pos, ds[0]) and ( ( j.pasos_consumidos + len(ds)) <= MAX_PASOS) and puedeRealizarAcción(t,m) :
                return True 
                     
    return False




#### Ejercicio 5


# Explicacion: esta funcion busca eliminar del tablero las piezas que estan en las posiciones trampa en el caso de que no tenga una pieza amiga vecina
# para eso revisa por cada poscion trampa (pos_trampa), si la pos_trampa no esta vacia y no tiene una pieza amiga vecina
# de ser ambas condiciones True -> vacia la casilla de pos_trampa donde estaba la pieza (entonces si Casilla = PIEZA, ahora Casilla = VACIO)
# como solo modifica el mismo tablero ("t") dado, no debe hacer return, modifica el tablero dado

def activar_trampas(t : Tablero) -> Tablero:
    """
    PRE: {tablero_bien_formado(t) == True}
    Args: 
         t (Tablero) : una lista de lista de casillas.

    Returns: devuelve un tablero nuevo *t_res (Tablero)* el cual tiene las trampas activadas, 
             es decir si hay una pieza en una de las posciciones trampa y no esta rodeada de ninguna pieza amiga, la pieza debe ser eliminada del tablero 
             (la casilla en esa posicion trampa se vacia)
    """
    t_res: Tablero = copiar_tablero(t)

    for pos_trampa in POSICIONES_TRAMPA:
      # en hay pieza amiga vecina debe entrar si o si una pieza, no se si ponerlo en el mismo renglon o separarlo en 2 if's

        if not(hay_casilla_vacia(t_res, pos_trampa)):
            if not( hay_pieza_amiga_vecina( t_res, pos_trampa)) :
               t_res[pos_trampa.fila][pos_trampa.columna] = VACIA # revisar si esta bien poner "VACIA" o "CasillaVacia"

    return t_res # hay que crear un nuevo tablero?? devolvemos el mismo modificado



#### Ejercicio 6


# explicacion: devuelve juego modificando valores del tablero dependiendo de la accion 

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    """
    PRE: {juego_bien_formado(j) == True ∧ movimiento_bien_formado(m) == True ∧ puede_realizar_movimiento(j,m) == True  }
    Args: 
            j (Juego) : representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                        donde el tablero *t* es el actual del juego,
                        el color *turno* es el del jugador al que le toca jugar 
                        y *pasosConsumidos* es el numero entero de pasos ya efectuados
            m (Movimiento) : representa el movimiento por realizar como una tripla (accion (Acción), origen (Posicion), pasos (list[Direccion])),

    Returns: devuelve un juego nuevo *j2*, el cual cumple:
            j2.tablero -> es el tablero j1 actualizado respecto a la accion de movimiento realizada 
                         (MOVER_A_SECAS -> se mueve la posicion *origen* hacia la casilla en la direccion m.pasos[0]) 
                         (ARRASTRAR -> se mueve la posicion *origen* hacia la casilla en la direccion m.pasos[0] y la pieza vecina enemiga que voy a arrastrar a la posicion en la direccion de arrastre)
                         (EMPUJE -> se mueve la posicion *origen* hacia la casilla en la direccion m.pasos[0] y la pieza vecina enemiga que voy a empujar a la posicion en la direccion de empuje)
            j2.turno -> es el mismo turno si (pasosConsumidos del j1 + |m.pasos|) < 4
                        es el color opuesto a j1.turno si pasosConsumidos del j1 + |m.pasos| == 4
            j2.pasos_consumidos-> es (pasosConsumidos del j1 + |m.pasos|) si es < 4
                                  si no es 0
    """

    tablero_original: Tablero = j.tablero
    t: Tablero = copiar_tablero(tablero_original)
    
    pos_origen: Posicion = m.origen 
    pieza: Casilla = casilla_en_posicion(t, pos_origen)

    pos_me_dirijo: Posicion = posicion_vecina_hacia(pos_origen, m.pasos[0])


    if m.accion==MOVER_A_SECAS:
        t[pos_me_dirijo.fila][pos_me_dirijo.columna] = pieza # pongo mi pieza en la casilla a la que queria moverme
        t[pos_origen.fila][pos_origen.columna] = VACIA # vacio la que estaba 

    elif m.accion == ARRASTRAR :
        d_arrastre: Direccion = m.pasos[1]
        pos_enemiga: Posicion = posicion_vecina_hacia(pos_origen, opuesta(d_arrastre))
        piezaEnemiga_arrastre: Casilla = t[pos_enemiga.fila][pos_enemiga.columna]

        t[pos_me_dirijo.fila][pos_me_dirijo.columna] = pieza
        t[pos_origen.fila][pos_origen.columna] = piezaEnemiga_arrastre
        t[pos_enemiga.fila][pos_enemiga.columna] = VACIA

    elif m.accion == EMPUJAR:
        pos_enemiga_origen: Posicion = posicion_vecina_hacia(m.origen, m.pasos[0])
        piezaEnemiga_empuje: Casilla = t[pos_enemiga_origen.fila][pos_enemiga_origen.columna]
        pos_enemiga_empuje: Posicion = posicion_vecina_hacia(pos_enemiga_origen,m.pasos[1])

        t[pos_enemiga_empuje.fila][pos_enemiga_empuje.columna] = piezaEnemiga_empuje
        t[pos_enemiga_origen.fila][pos_enemiga_origen.columna] = pieza
        t[pos_origen.fila][pos_origen.columna] = VACIA

    # despues de realizar la accion deseada, se activan las trampas:

    t_final: Tablero = activar_trampas(t)

# hay que revisar pasos consumidos y si se pasan o son iguales a 4 cambia el color del turno al opuesto y pone pasos consumidos en 0
# si no se pasa se deja el mismo turno y se cambian los pasos a pasos consumidos + len (m.pasos)
# cambiar de turno antes se podria pero esta fuera de nuestro alcance en el programa 

    pasosConsumidos: int =  j.pasos_consumidos + len(m.pasos)

    if pasosConsumidos == MAX_PASOS:
        pasosConsumidos = 0
        j2: Juego = Juego(t_final , oponente(j.turno), pasosConsumidos)
    else:
        j2 = Juego(t_final , j.turno, pasosConsumidos)
    
    return j2


#### Ejercicio 7


def conejo_en_fila_objetivo(t: Tablero, col: Color) -> bool: #auxiliar
    """
    PRE: {tablero_bien_formado(t) == True}
    Args: 
        t (Tablero) : una lista de lista de casillas.
        col (Color) : la variable refiere a PLATEADO o DORADO, sobre el cual se quiere revisar si hay conejo en la     
                      fila objetivo 
                      (fila 7, si col == DORADO) (fila 0, si col == PLATEADO)

    Returns: True ←→ si hay alguna casilla en la fila objetivo con una pieza del color dado ∧ figura conejo en el     
                     tablero *t* 
    """

    hay_conejo: bool = False

    if col == DORADO:
        fila_objetivo: int = 7

    else:
        fila_objetivo: int = 0 

    for i in range(0, ANCHO, 1):
         pos: Posicion = Posicion(fila_objetivo, i)

         if not(hay_casilla_vacia( t, pos)) :
               casilla: Casilla = t[fila_objetivo][i]
               figura: Figura = casilla.figura
               color: Color = casilla.color

               if figura == CONEJO and color == col:
                    hay_conejo = True

    return hay_conejo


def no_hay_conejos(t: Tablero, col: Color) -> bool: #auxiliar
    """
    PRE: {tablero_bien_formado(t) == True}
    Args: 
        t (Tablero) : una lista de lista de casillas.
        col (Color) : la variable refiere a PLATEADO o DORADO, sobre el cual se quiere revisar que haya o no conejos.

    Returns: True ←→ no hay ninguna casilla con una pieza del color dado ∧ figura conejo en el tablero *t* 
    """

    hay_conejos: bool = False
    
    for f in range(0, ALTO, 1):
        for c in range(0, ANCHO, 1):
            pos: Posicion = Posicion(f,c)
            if not(hay_casilla_vacia( t, pos)) :
                casilla: Casilla = t[f][c]
                figura: Figura = casilla.figura
                color: Color = casilla.color
                if figura == CONEJO and color == col:
                    hay_conejos = True 

    return not(hay_conejos) # si hay conejos -> da False; si no hay conejos -> da True

def reune_condiciones_de_ganar(t: Tablero, col: Color)-> bool: #auxiliar
    """
    PRE: {tablero_bien_formado(t) == True}
    Args:  
        t (Tablero) : una lista de lista de casillas.
        col (Color) : la variable refiere a PLATEADO o DORADO, sobre el cual se quiere revisar 
                      si cumple condiciones de ganar
    
    Returns: True ←→ hay un conejo en la fila de objetivo de cada jugador ∨ no hay ningun conejo del oponente. 
    """

    return (  (conejo_en_fila_objetivo(t, col) or (no_hay_conejos(t, oponente(col))))  )


def esJugadorGanador(j: Juego, col: Color) -> bool: #auxiliar
    """
    PRE: {juego_bien_formado(j) == True}
    Args:
        j (Juego) : representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                        donde el tablero *t* es el actual del juego,
                        el color *turno* es el del jugador al que le toca jugar 
                        y *pasosConsumidos* es el numero entero de pasos ya efectuados.

    Returns: True ←→
                (si el turno es el color del oponente y reune condiciones para ganar el color dado)  ∨
                (hay conejo en la fila inicial del oponente o el oponenete no tiene conejos)
                ∨ 
                (si el turno es el color dado y reune condiciones para ganar el color dado ) ∨ 
                ( (hay conejo en la fila inicial del oponente o el oponenete no tiene conejos) ∧ (el oponente no tiene conejos en el tablero) )
    """

    t: Tablero = j.tablero 
    turno: Color = j.turno


    if j.pasos_consumidos != 0:
         return False
    
    elif turno == oponente(col):
         return reune_condiciones_de_ganar(t,col)

    else: 
        return ( (reune_condiciones_de_ganar(t,col)) and ( not (reune_condiciones_de_ganar(t, oponente(col)))) )


def hay_ganador_determinado(j : Juego) -> bool:
    """
    PRE: {juego_bien_formado(j) == True}
    Args:
        j (Juego) : representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                        donde el tablero *t* es el actual del juego,
                        el color *turno* es el del jugador al que le toca jugar 
                        y *pasosConsumidos* es el numero entero de pasos ya efectuados.

    Returns: devuelve si es que hay algun ganador dentro del juego *j*.
    """

    return ( (esJugadorGanador(j, DORADO)) or (esJugadorGanador(j,PLATEADO)) )


def ganador_del_juego(j : Juego) -> Color:
    """
    PRE: {juego_bien_formado(j) == True ∧ hay_ganador_determinado(j) == True}
    Args:
        j (Juego) : representa el estado actual del juego como una tripla de la siguiente forma: (t (Tablero), turno (Color), pasosConsumidos (int))
                    donde el tablero *t* es el actual del juego,
                    el color *turno* es el del jugador al que le toca jugar 
                    y *pasosConsumidos* es el numero entero de pasos ya efectuados.

    Returns: devuelve el color del ganador del juego *j* dado. 
    """
    
    if esJugadorGanador(j, DORADO):
         return DORADO
    
    return PLATEADO

