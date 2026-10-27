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




#### Ejercicio 1

# problema tablero_bien_formado ( in t : Tablero ) : Bool {
        # requiere { True }
        # asegura { res = true ←→ tableroBienFormado (t) }
        # }

# aux tableroBienFormado (t : Tablero ) :=
        # |t| = Alto
        #  ∧ para todo i:Z.(0 ≤ i < |t| → |t[i]| = Ancho 

# Explicacion: esta funcion busca decidir (es True o False) si un tablero (una lista de listas, ver en ejemplo_tablero) es valido. 
# Es valido, devuelve True, si el tablero es la tiene una cantidad ALTO de filas (la longitud del tablero es ALTO) 
# y cada fila tiene la longitud ANCHO

def tablero_bien_formado(t : Tablero) -> bool:

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




# problema posición_en_tablero ( in pos : Posición ) : Bool {
        # requiere { True }
        # asegura { res = true ←→ posiciónEnTablero (pos) }
        # }

# aux posiciónEnTablero (pos : Posición ) :=
        # 0 ≤ pos. fila < Alto
        # ∧ 0 ≤ pos. columna < Ancho

# Explicacion: esta funcion busca decidir (es True o False) si una poscicion: pos = (fila,columna) pertenece al tablero del juego
# es True si la parte de filas en pos (pos.fila -> pos[0]) esta entre 0 y el alto 
# Y si la parte de columnas en pos (pos.columna -> pos[1]) esta entre 0 y el ancho

def posicion_en_tablero(pos : Posicion) -> bool:
      
        if (0 <= (pos.fila) < ALTO) and (0 <= (pos.columna) < ANCHO): # si la pos pertenece al tablero...
                return True
        else: 
                return False

# t =           ['hcdmedch', #7
#               'rrrrrrrr', #6
#               '--------', #5
#               '--------', #4
#               '--------', #3
#               '--------', #2
#               'RRRRRRRR', #1
#               'HCDMEDCH'] #01234567

# print(posicion_en_tablero(Posicion(0,8)))




# problema movimiento_bien_formado ( in m : Movimiento ) : Bool {
        # requiere { True }
        # asegura { res = true ←→ movimientoBienFormado (m) }
        # }

# aux movimientoBienFormado (m : Movimiento ) :=
# posiciónEnTablero (m. origen )
        # ∧ (m. acción = Mover_a_secas → |m. pasos | = 1)
        # ∧ (m. acción = Arrastrar → |m. pasos | = 2)
        # ∧ (m. acción = Empujar → |m. pasos | = 2)

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

    if posicion_en_tablero(m.origen):
        if m.accion == MOVER_A_SECAS and len(m.pasos) == 1:
                return True
        
        elif m.accion == ARRASTRAR and len(m.pasos) == 2:
                return True
        
        elif m.accion == EMPUJAR and len(m.pasos) == 2: 
                return True
        
    else:
         return False



             
# problema juego_bien_formado ( in j : Juego ) : Bool {
    # requiere { True }
    # asegura { res = true ←→ juegoBienFormado (j ) }
# }

# aux juegoBienFormado (j : Juego ) :=
    # tableroBienFormado (j . tablero )
    # ∧ 0 ≤ j . pasosConsumidos < Max_pasos

# Explicacion: esta funcion decide (es True o False) si un juego: (tablero, color, pasosConsumidos) esta bien formado 
# donde color representa a que jugador le toca jugar y pasosConsumidos es el numero (int) de pasos que ya se hizo por el jugador de ese color en el turno actual
# se revisa si el tablero esta bien formado Y si la cantidad de pasos es menor a 4 

def juego_bien_formado(j : Juego) -> bool:
    return tablero_bien_formado(j.tablero) and (0 <= j.pasos_consumidos < MAX_PASOS)




#### Ejercicio 2

# problema posición_vecina_hacia ( in pos : Posición , in d : Dirección ) : Posición {
    # requiere { True }
    # asegura { esPosiciónVecinaHacia (pos, d, res) }
    # }
# aux esPosiciónVecinaHacia (pos : Posición , d : Dirección , pos′ : Posición ) :=
    # (d = Norte → (pos′ . fila = pos. fila + 1 ∧ pos′ . columna = pos. columna ))
    # ∧ (d = Sur → (pos′ . fila = pos. fila - 1 ∧ pos′ . columna = pos. columna ))
    # ∧ (d = Este → (pos′ . fila = pos. fila ∧ pos′ . columna = pos. columna + 1))
    # ∧ (d = Oeste → (pos′ . fila = pos. fila ∧ pos′ . columna = pos. columna - 1))

# Explicacion: esta funcion devuelve una pos_vecina: (fila,columna) en una direccion "d" respecto a una pos: (fila,columna) dada
# entonces si:
# d = NORTE debe devolver el vecino de arriba -> pos_vecina es (fila + 1, columna)
# d = SUR debe devolver el vecino de abajo -> pos_vecina es (fila - 1, columna)
# d = ESTE debe devolver el vecino de la derecha -> pos_vecina es (fila, columna + 1)
# d = OESTE debe devolver el vecino de la izquierda -> pos_vecina es (fila, columna - 1)

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:

    if   d == NORTE:
        resultado: Posicion  = Posicion(pos.fila +1, pos.columna)
    elif d == SUR:
         resultado = Posicion(pos.fila - 1, pos.columna)
    elif d == ESTE:
         resultado = Posicion(pos.fila, pos.columna + 1)
    else:
        resultado = Posicion(pos.fila, pos.columna - 1)

    return resultado




# problema casilla_en_posición ( in t : Tablero , in pos : Posición ) : Casilla {
    # requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
    # asegura { res = t[pos. fila ][pos. columna ] }

# Explicacion: esta funcion da la casilla de la poscion dentro del tablero
# se busca que hay en la posicion t[fila][columna] y devuelve una c: Casilla (puede ser vacio o pieza: (figura, color) )

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    
    c: Casilla = t[p.fila][p.columna]

    return c




# problema hay_casilla_vacía ( in t : Tablero , in pos : Posición ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posici ó nEnTablero (pos) }
    # asegura { res = true ←→ hayCasillaVacía(t, pos) }

# aux hayCasillaVacía(t : Tablero , pos : Posición ) :=
# posiciónEnTablero (pos)
# ∧ t[pos. fila ][pos. columna ] = Vacía

# Explicacion: decide (True o False) dada una pos: (fila,columna) revisa si en el tablero t[fila][columna] es vacia 
# si esa casilla (c: casilla = t[fila][columna] ) es vacia devuelve True

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    
    c: Casilla = t[pos.fila][pos.columna]

    return (c == VACIA)




# problema hay_pieza_de_color ( in t : Tablero , in pos : Posición , in col : Color ) : Bool {
# requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
# asegura { res = true ←→ hayPiezaDeColor (t, pos, col) }

# aux hayPiezaDeColor (t : Tablero , pos : Posición , col : Color ) :=
# existe f : Figura . hayFiguraDeColor (t, pos, f , col)

# aux hayFiguraDeColor (t : Tablero , pos : Posición , f : Figura , col : Color ) :=
# posiciónEnTablero (pos)
# ∧ ¬hayCasillaVacía (t, pos)
# ∧ t[pos. fila ][pos. columna ]. figura = f
# ∧ t[pos. fila ][pos. columna ]. color = col

# Explicacion: decide (es True o False) si en la poscicion pos en el tablero hay una pieza Y es del color dado

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
   
   c: Casilla = t[pos.fila][pos.columna]

   return ( not (hay_casilla_vacia(t,pos)) and ( c.color == col ) )




#### Ejercicio 3

# problema hay_casilla_vacía_hacia ( in t : Tablero , in pos : Posición , in d : Dirección ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
    # asegura { res = true ←→ hayCasillaVacíaHacia (t, pos, d) }

# aux hayCasillaVacíaHacia (t : Tablero , pos : Posición , d : Dirección ) :=
    # existe pos′: Posición . (
    # esPosicionVecinaHacia (pos, d, pos′ )
    # ∧ hayCasillaVacía(t, pos′ )

# Explicacion: decide (es True o False) si hay una casilla vacia en una direccion particular dada
# Para ello buscamos la posicion vecina en esa direccion y con esa pos_vecina evaluamos si es que su casilla es vacia o no 

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    
    pos_vecina: Posicion = posicion_vecina_hacia(pos,d)

    return ( posicion_en_tablero(pos_vecina) and hay_casilla_vacia(t, pos_vecina) )




# problema hay_pieza_amiga_vecina ( in t : Tablero , in pos : Posición ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posici ó nEnTablero (pos) }
    # requiere { hayPieza (t, pos) }
    # asegura { res = true ←→ hayPiezaAmigaVecina (t, pos) }

# aux hayPiezaAmigaVecina (t : Tablero , pos : Posición ) :=
    # existe d: Dirección . hayPiezaAmigaHacia (t, pos, d
  
# aux hayPiezaAmigaHacia (t : Tablero , pos : Posición , d : Dirección ) :=
    # existe col: Color . existe posamiga : Posición . (
    # hayPiezaDeColor (t, pos, col)
    # ∧ esPosiciónVecinaHacia (pos, d, posamiga )
    # ∧ hayPiezaDeColor (t, posamiga , col)
    # )

# Explicacion: esta funcion decide (es True o False) si existe alguna pieza en alguna direccion (norte,sur,este,oeste)
# tal que esa pieza es del mismo color que la pieza en la posicion ingresada.
# Para eso, buscamos revisar cada vecino en cada direccion. Al revisar comparamos el color del vecino con el color de la pos ingresada.
# al primer vecino en la primera direccion que se encuentra se devuelve True

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    ds: list[Direccion] = [NORTE,SUR,ESTE,OESTE]
    c: Casilla = t[pos.fila][pos.columna]
    col: Color = c.color

    for d in ds:
        pos_vecina: Posicion = (posicion_vecina_hacia(pos,d))
        c_vecina: Casilla = t[pos_vecina.fila][pos_vecina.columna]

        if not ( hay_casilla_vacia(t,pos_vecina)):
            pieza: Pieza = c_vecina
            if pieza.color == col:
                 return True

    return False




# problema hay_pieza_enemiga_más_débil_hacia ( in t : Tablero, in pos : Posición,in d : Dirección ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
    # requiere { hayPieza (t, pos) }
    # asegura { res = true ←→ hayPiezaEnemigaMásDébilHacia (t, pos, d) }
    # }

# aux hayPiezaEnemigaMásDébilHacia (t : Tablero , pos : Posición , d : Dirección ) :=
    # existe f : Figura .existe col: Color . existe posenemiga : Posición .existe fenemiga : Figura . (
    # hayFiguraDeColor (t, pos, f , col)
    # ∧ esPosiciónVecinaHacia (pos, d, posenemiga )
    # ∧ hayFiguraDeColor (t, posenemiga , fenemiga , oponente (col))
    # ∧ fuerza (f ) > fuerza (fenemiga )

# Explicacion:  dada una pos: Posicion(fila,columna) donde hay una pieza (es decir, no es vacia) 
# decide (es True o False) si es que hay una pieza enemiga (del otro color) en una direccion particular: d y 
# esta tiene menor fuerza que la fuerza de la pieza en la pos ingresada.
# Para hacerlo se busca el color y la fuerza de la pos_vecina en la direccion d ingresada.
# De pertenecer al tablero pos_vecina, comparamos el color a ver si es enemiga, y si lo es comparamos su fuerza.
# En el caso de ser enemiga y de fuerza menor se devuelve True sino devuelve False

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    casilla_pos: Casilla = t[pos.fila][pos.columna]
    figura_pos: Figura = casilla_pos.figura
    fuerza_pos: int = fuerza(figura_pos)

    pos_vecina: Posicion = posicion_vecina_hacia(pos,d)
    casilla_vecina: Casilla = t[pos_vecina.fila][pos_vecina.columna]
    figura_vecina: Figura = casilla_vecina.figura
    fuerza_vecina = fuerza(figura_vecina)

    if posicion_en_tablero(pos_vecina):
         
         if casilla_vecina.color == casilla_pos.color:
              return False
         else:
              if  fuerza_pos > fuerza_vecina:
                   return True
              else:
                   return False
              
    return False




# problema hay_pieza_enemiga_más_fuerte_vecina ( in t : Tablero , in pos : Posición ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
    # requiere { hayPieza (t, pos) }
    # asegura { res = true ←→ hayPiezaEnemigaMásFuerteVecina (t, pos) }
# # }

# aux hayPiezaEnemigaMásFuerteVecina (t : Tablero , pos : Posición ) :=
    # existe d: Dirección . hayPiezaEnemigaMasFuerteHacia (t, pos, d)

# aux hayPiezaEnemigaMásFuerteHacia (t : Tablero , pos : Posición , d : Dirección ) :=
    # existe f : Figura.existe col: Color . existe posenemiga : Posición .existe fenemiga : Figura . (
    # hayFiguraDeColor (t, pos, f , col)
    # ∧ esPosiciónVecinaHacia (pos, d, posenemiga )
    # ∧ hayFiguraDeColor (t, posenemiga , fenemiga , oponente (col))
    # ∧ fuerza (f ) < fuerza (fenemiga )
    # )

# Explicacion: la funcion decide (es True o False) si existe una pieza enemiga mas fuerte al rededor de la pieza en la pos ingresada 
# para eso definimos variables sobre la pos ingresada (su color, su fuerza), 
# luego por direccion en la lista de direcciones ("ds") buscamos el vecino en esa d y comparamos colores para buscar enemigos
# al hallar el vecino enemigo comparamos sus fuerzas, si la fuerza del enemigo es mayor a la fuerza de la figura en la pos ingresada entonces devolvemos True

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    c_pos: Casilla = t[pos.fila][pos.columna]
    f_pos: Figura = c_pos.figura
    col_pos: Color = f_pos.color
    fuerza_pos: int = fuerza(figura)
    
    ds: list[Direccion] = [NORTE,SUR,ESTE,OESTE]

    for d in ds:
        pos_vecina_d: Posicion = posicion_vecina_hacia(pos,d)
        c_vecina_d: Casilla = t[pos_vecina_d.fila][pos_vecina_d.columna]
        f_vecina_d: Figura = c_vecina_d.figura 
        fuerza_vecina_d: int = fuerza(f_vecina_d)


        if not(hay_casilla_vacia(t, pos_vecina_d)) and not(hay_pieza_de_color(t, pos_vecina_d, col_pos))  :
            if fuerza_vecina_d > fuerza_pos:
                 return True

    return False 




# problema hay_pieza_congelada ( in t : Tablero , in pos : Posición ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
    # asegura { res = true ←→ hayPiezaCongelada (t, pos) }
    # }

# aux hayPiezaCongelada (t : Tablero , pos : Posición ) :=
    # hayPieza (t, pos) --> no esta vacia la casilla 
    # ∧ hayPiezaEnemigaMásFuerteVecina (t, pos)
    # ∧ ¬hayPiezaAmigaVecina (t, pos)

# Explicacion: esta funcion decide ( es True o False) si una pos se encuentra congelada 
# Para eso, se revisa si es o no vacia la casilla de esa pos. 
# Luego si hay una pieza vecina enemiga mas fuerte Y no hay una pieza amiga vecina, entonces devuelve True (sino devuelve False)

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:

    if not( hay_casilla_vacia(t, pos)):
         if hay_pieza_enemiga_mas_fuerte_vecina(t, pos) and not(hay_pieza_amiga_vecina(t,pos)):
              return True

    return False




#### Ejercicio 4

#definimos la funcion auxiliar: direcciónDeMovimientoHabilitada

# problema direcciónDeMovimientoHabilitada( in t : Tablero , pos : Posición , d : Dirección ) : Bool {
    # requiere { juegoBienFormado (j) ∧ movimientoBienFormado (m) }
    # asegura { res = true ←→ hayFiguraDeColor (t, pos, f , col) ∧ ((f = Conejo ∧ col = Dorado ) → d ̸= Sur ) ∧ ((f = Conejo ∧ col = Plateado ) → d ̸= Norte ) }
    # }

# aux direcciónDeMovimientoHabilitada (t : Tablero , pos : Posición , d : Dirección ) :=
# existe f : Figura .existe col: Color . (
    # hayFiguraDeColor (t, pos, f , col)
    # ∧ ((f = Conejo ∧ col = Dorado ) → d ̸= Sur )
    # ∧ ((f = Conejo ∧ col = Plateado ) → d ̸= Norte )
    # )

# Explicacion: la funcion decide ( es True o False) si la direccion de un movimiento esta habilitada 
# Para eso, declara las variables pieza, f: figura, col: color y revisa 
# si la pieza es conejo y dorado NO puede ir al sur
# si la pieza es conejo y plateado NO puede ir al norte

def direcciónDeMovimientoHabilitada(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    pieza: Pieza = t[pos.fila][pos.columna]
    f: Figura = pieza.figura
    col: Color = pieza.color

    habilitado: bool = True

    if (f == CONEJO) and (col == DORADO) and (d == SUR):
        habilitado = False
    elif (f == CONEJO) and (col == PLATEADO) and (d == NORTE):
        habilitado = False

    return habilitado 

#definimos la funcion auxiliar: puedeRealizarAcción

# problema puedeRealizarAcción(t : Tablero , m : Movimiento):
#   requiere: { movimiento_bien_formado(m)}
#   requiere: { tablero_bien_formado(t)}
#   asegura: { True <-> (m.acción = Mover_a_secas → puedeMoverASecas (t, m. origen , m. pasos [0])) ∧ 
#                       (m.acción = Arrastrar → puedeArrastrar (t, m.origen , m.pasos[0] , m.pasos[1])) ∧ 
#                       (m.acción = Empujar → puedeEmpujar (t, m. origen , m. pasos [0] , m. pasos [1]) }

# aux puedeMoverASecas (t : Tablero , pos : Posición , d : Dirección ) :=
    # hayCasillaVacíaHacia (t, pos, d)

# aux puedeArrastrar (t : Tablero , pos : Posición , d, darrastre : Dirección ) :=
    # hayCasillaVacíaHacia (t, pos, d)
    # ∧ hayPiezaEnemigaMásDébilHacia (t, pos, opuesta (d arrastre ))

# aux puedeEmpujar (t : Tablero , pos : Posición , d, dempuje : Dirección ) :=
    # hayPiezaEnemigaMásDébilHacia (t, pos, d)
    # ∧ existe posenemiga : Posición . ( esPosiciónVecinaHacia (pos, d, posenemiga )
    # ∧ hayCasillaVacíaHacia (t, posenemiga , dempuje )


# Explicacion: la funcion decide ( es True o False) si la accion de un movimiento se puede realizar
# Para eso, declara las variables accion, d: dirreccion y revisa 
# si la accion es MOVER_A_SECAS y la direccion a la que quiero mover mi pieza esta vacia                                          -> se puede (=True)
# si la accion es ARRASTRAR y hay una casilla vacia en la direccion a la que quiero mover mi pieza 
# Y hay una pieza enemiga mas debil en la posicion opuesta a la que quiero arrastrar                                              -> se puede (=True)
# si la accion es EMPUJAR (ultima opcion), se busca la pos vecina en la direccion ()"d"), 
# si no esta vacia entonces revisa si es mas debil Y si hay una casilla vacia a donde voy a empujar a la otra pieza ("d_empuje")  -> se puede (=True)

def puedeRealizarAcción(t: Tablero, m: Movimiento) -> bool:
    pos: Posicion = m.origen 
    accion: Accion = m.accion
    d: Direccion = m.pasos[0]

    puedeRealizarAccion: bool = False
    
    if accion == MOVER_A_SECAS and hay_casilla_vacia_hacia(t, pos, d):
        puedeRealizarAccion = True

    elif accion == ARRASTRAR :
        d_arrastre: Accion = m.pasos[1]
        if hay_casilla_vacia_hacia(t, pos, d) and hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(d_arrastre)):
              puedeRealizarAccion = True

    else:
        d_empuje: Accion = m.pasos[1]
        pos_vecina: Posicion = posicion_vecina_hacia(pos,d)

        if not(hay_casilla_vacia(t, pos_vecina)):
             if hay_pieza_enemiga_mas_debil_hacia(t,pos,d) and hay_casilla_vacia_hacia(t, pos_vecina, d_empuje):
                puedeRealizarAccion = True

    return puedeRealizarAccion 

# problema puede_realizar_movimiento ( in j : Juego , in m : Movimiento ) : Bool {
    # requiere { juegoBienFormado (j) ∧ movimientoBienFormado (m) }
    # asegura { res = true ←→ puedeRealizarMovimiento (j , m) }
    # }

# aux puedeRealizarMovimiento (j : Juego , m : Movimiento ) :=
    # hayPiezaDeColor (j. tablero , m. origen , j. turno )
    # ∧ ¬hayPiezaCongelada (j. tablero , m. origen )
    # ∧ direcciónDeMovimientoHabilitada (j. tablero , m. origen , m. pasos [0])
    # ∧ j. pasosConsumidos + |m. pasos | ≤ Max_pasos
    # ∧ puedeRealizarAcción(j. tablero , m)

# Explicacion: en esta funcion se decide (es True o False) si un movimiento se puede realizar. 
# Para ello, se usan las funciones auxiliares previamente definidas (direcciónDeMovimientoHabilitada y puedeRealizarAcción)
# primero definimos el color del turno al que le toca jugar, luego definimos la pos donde esta mi pieza en la que voy a inicializar el movimiento
# despues si hay una pieza del color del turno en esa posicion origen y esa pieza no esta congelada, 
# se revisa si la direccion del movimiento es valida Y si los pasos consumidos junto a los pasos que voy a hacer (mover 1 o 2 piezas) no se pasan de 4 Y si se puede realizar la accion

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:      # juego = ( tablero, turno, pasosConsumidos)
    turno : Color = j.turno
    t: Tablero = j.tablero
    pos: Posicion = m.origen  # m.origen -> (fila_origen, columna_origen)
    ds: list[Direccion] = m.pasos


    if hay_pieza_de_color(t, pos, turno) and not(hay_pieza_congelada(t, pos)) :
           if direcciónDeMovimientoHabilitada(t, pos, ds[0]) and ( ( j.pasos_consumidos + len(ds)) <= MAX_PASOS) and puedeRealizarAcción(t,m) :
                return True 
                     
    return False




#### Ejercicio 5


# problema activar_trampas ( in t : Tablero ) : Tablero {
    # requiere { tableroBienFormado (t) }
    # asegura { tableroBienFormado (res) }
    # asegura { esTableroDespuésDeActivarTodasLasTrampas (t, res) }
    # }

# aux esTableroDespuésDeActivarTodasLasTrampas (t0 , t1 : Tablero ) :=
    # existe t intermedio1 ,t intermedio2 ,t intermedio3 : Tablero . (
    # esTableroDespuésDeActivarTrampa (t0 , tintermedio1 , Posiciones_trampa [0])
    # ∧ esTableroDespuésDeActivarTrampa (tintermedio1 , tintermedio2 , Posiciones_trampa [1])
    # ∧ esTableroDespuésDeActivarTrampa (tintermedio2 , tintermedio3 , Posiciones_trampa [2])
    # ∧ esTableroDespuésDeActivarTrampa (tintermedio3 , t1 , Posiciones_trampa [3])
    # )

# aux esTableroDespuésDeActivarTrampa (t0 , t1 : Tablero , postrampa : Posición ) :=
    # ( hayPiezaAmigaVecina (t0 , postrampa ) → t1 = t0 )
    # ∧ (¬hayPiezaAmigaVecina (t0 , postrampa ) → esTableroSacandoPieza (t0 , t1 , postrampa ))

        
# aux esTableroSacandoPieza (t0 , t1 : Tablero , pos : Posición ) :=
    # tablerosCoincidenSalvoEnLaPosición(t0 , t1 , pos)
    # ∧ hayCasillaVacía(t1 , pos)

# aux tablerosCoincidenSalvoEnLaPosición(t1 , t2 : Tablero , pos : Posición ) :=
    # para todo pos′ : Posición .(
    # ( posiciónEnTablero (pos′ ) ∧ pos′ ̸= pos) →
    # tablerosCoincidenEnLaPosición(t1 , t2 , pos′ )
    # )

# aux tablerosCoincidenEnLaPosición(t1 , t2 : Tablero , pos : Posición ) :=
    # t1 [pos. fila ][pos. columna ] = t2 [pos. fila ][pos. columna ]

# Explicacion: esta funcion busca eliminar del tablero las piezas que estan en las posiciones trampa en el caso de que no tenga una pieza amiga vecina
# para eso revisa por cada poscion trampa (pos_trampa), si la pos_trampa no esta vacia y no tiene una pieza amiga vecina
# de ser ambas condiciones True -> vacia la casilla de pos_trampa donde estaba la pieza (entonces si Casilla = PIEZA, ahora Casilla = VACIO)
# como solo modifica el mismo tablero ("t") dado, no debe hacer return, modifica el tablero dado

def activar_trampas(t : Tablero) -> Tablero:

    for pos_trampa in POSICIONES_TRAMPA:
      # en hay pieza amiga vecina debe entrar si o si una pieza, no se si ponerlo en el mismo renglon o separarlo en 2 if's

        if not(hay_casilla_vacia(t, pos_trampa)) and  not( hay_pieza_amiga_vecina( t, pos_trampa)) :
             t[pos_trampa.fila][pos_trampa.columna] = VACIA # revisar si esta bien poner "VACIA" o "CasillaVacia"

    return t # hay que crear un nuevo tablero?? devolvemos el mismo modificado



    
#### Ejercicio 6

# problema realizar_movimiento ( in j : Juego , in m : Movimiento ) : Juego {
    # requiere { juegoBienFormado (j ) ∧ movimientoBienFormado (m) }
    # requiere { puedeRealizarMovimiento (j , m) }
    # asegura { juegoBienFormado (res) }
    # asegura { juegoPostMovimiento (j , res, m) }
    # }

# aux juegoPostMovimiento (j0 , j1 : Juego , m : Movimiento ) :=
    # tableroPostMovimiento (j0 . tablero , j1 . tablero , m)
    # ∧ juegoConTurnoPosiblementeAvanzado (j0 , j1 , m)

# aux juegoConTurnoPosiblementeAvanzado (j0 , j1 : Juego , m : Movimiento ) :=
    # ( hayQueCambiarDeTurno (j0 , m) → (j1 . turno = oponente (j0 . turno ) ∧ j1 . pasosConsumidos = 0)) hay que cambiar de turno cuando el color es el del oponente y ya no se consumen mas pasos
    # ∧ (¬hayQueCambiarDeTurno (j0 , m) → (j1 . turno = j0 . turno ∧ j1 . pasosConsumidos = j0 . pasosConsumidos + |m. pasos |))

# aux hayQueCambiarDeTurno (j : Juego , m : Movimiento ) :=
    # j . pasosConsumidos + |m. pasos | = Max_pasos

# aux tableroPostMovimiento (t0 , t1 : Tablero , m : Movimiento ) :=
    # (m.acción = Mover_a_secas → tableroPostMoverASecas (t0 , t1 , m.origen , m.pasos [0]))
    # ∧ (m.acción = Arrastrar → tableroPostArrastrar (t0 , t1 , m.origen , m.pasos [0] , m.pasos [1]))
#     # ∧ (m.acción = Empujar → tableroPostEmpujar (t0 , t1 , m.origen , m.pasos [0] , m.pasos [1]))

# aux tableroPostMoverASecas (t0 , t1 : Tablero , pos : Posición , d : Dirección ) :=
    # existe posdestino : Posición . existe tintermedio : Tablero . (
    # esPosiciónVecinaHacia (pos, d, posdestino )
    # ∧ esTableroTrasladandoPieza (t0 , tintermedio , pos, posdestino )
    # ∧ esTableroDespu é sDeActivarTodasLasTrampas (tintermedio , t1 )
    # )

# aux tableroPostArrastrar (t0 , t1 : Tablero , pos : Posición , d, darrastre : Dirección ) :=
    # existe poshueco , posenemiga : Posición . existe tintermedio1 ,tintermedio2 : Tablero . (
    # esPosiciónVecinaHacia (pos, d, poshueco )
    # ∧ esPosiciónVecinaHacia (pos, opuesta (darrastre ) , posenemiga )
    # ∧ esTableroTrasladandoPieza (t0 , tintermedio1 , pos, poshueco )
    # ∧ esTableroTrasladandoPieza (tintermedio1 , tintermedio2 , posenemiga , pos)
    # ∧ esTableroDespu é sDeActivarTodasLasTrampas (tintermedio2 , t1 )
    # )

# aux tableroPostEmpujar (t0 , t1 : Tablero , pos : Posición , d, dempuje : Dirección ) :=
    # existe posenemiga , poshueco : Posición . existe tintermedio1 ,tintermedio2 : Tablero . (
    # esPosiciónVecinaHacia (pos, d, posenemiga )
    # ∧ esPosiciónVecinaHacia (posenemiga , dempuje , poshueco )
    # ∧ esTableroTrasladandoPieza (t0 , tintermedio1 , posenemiga , poshueco )
    # ∧ esTableroTrasladandoPieza (tintermedio1 , tintermedio2 , pos, posenemiga )
    # ∧ esTableroDespuésDeActivarTodasLasTrampas (tintermedio2 , t1 )
    # )


# aux esTableroTrasladandoPieza (t0 , t1 : Tablero , posorigen ,posdestino : Posición ) :=
    # existe f : Figura .existe col: Color .existe tintermedio : Tablero . (
    # hayFiguraDeColor (t0 , posorigen , f , col)
    # ∧ esTableroSacandoPieza (t0 , tintermedio , posorigen )
    # ∧ esTableroPoniendoPieza (tintermedio , t1 , posdestino , f , col)
#     # )

# aux esTableroPoniendoPieza (t0 , t1 : Tablero , pos: Posición , f : Figura , col: Color ) :=
    # tablerosCoincidenSalvoEnLaPosición (t0 , t1 , pos)
    # ∧ hayFiguraDeColor (t1 , pos, f , col)

# aux tablerosCoincidenSalvoEnLaPosici ó n (t1 , t2 : Tablero , pos : Posición ) :=
    # para todo pos′ : Posición .(
    # ( posiciónEnTablero (pos′ ) ∧ pos′̸ = pos) →
    # tablerosCoincidenEnLaPosición (t1 , t2 , pos′ )
    # )

# aux tablerosCoincidenEnLaPosición (t1 , t2 : Tablero , pos : Posición ) :=
    # t1 [pos. fila ][pos. columna ] = t2 [pos. fila ][pos. columna ]


# explicacion: devuelve juego modificando valores del tablero dependiendo de la accion --falta completar

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    t: Tablero = j.tablero
    
    pos_origen: Posicion = m.origen 
    pieza: Casilla = casilla_en_posicion(t, pos_origen)

    pos_me_dirijo: Posicion = posicion_vecina_hacia(pos_origen, m.pasos[0])


    if m.accion==MOVER_A_SECAS:
        t[pos_me_dirijo.fila][pos_me_dirijo.columna] = pieza # pongo mi pieza en la casilla a la que queria moverme
        t[pos_origen.fila][pos_origen.columna] = VACIO # vacio la que estaba 

    elif m.accion == ARRASTRAR :
        d_arrastre: Direccion = m.pasos[1]
        pos_enemiga: Posicion = posicion_vecina_hacia(pos_origen, opuesta(d_arrastre))
        piezaEnemiga: Casilla = t[pos_enemiga.fila][pos_enemiga.columna]

        t[pos_me_dirijo.fila][pos_me_dirijo.columna] = pieza
        t[pos_origen.fila][pos_origen.columna] = piezaEnemiga
        t[pos_enemiga.fila][pos_enemiga.columna] = VACIO

    elif m.accion == EMPUJAR:
        pos_enemiga_origen: Posicion = posicion_vecina_hacia(m.origen, m.pasos[0])
        piezaEnemiga: Pieza = t[pos_enemiga_origen.fila][pos_enemiga_origen.columna]
        pos_enemiga_empuje: Posicion = posicion_vecina_hacia(pos_enemiga_origen,m.pasos[1])

        t[pos_enemiga_empuje.fila][pos_enemiga_empuje.columna] = piezaEnemiga
        t[pos_enemiga_origen.fila][pos_enemiga_origen.columna] = pieza
        t[pos_origen.fila][pos_origen.columna] = VACIO

# hay que revisar pasos consumidos y si se pasan o son iguales a 4 cambia el color del turno al opuesto y pone pasos consumidos en 0
# si no se pasa se deja el mismo turno y se cambian los pasos a pasos consumidos + len (m.pasos)
# cambiar de turno antes se podria pero esta fuera de nuestro alcance en el programa 


    j2= (t , j.turno, j.pasosConsumidos)
    
    return j2

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")


