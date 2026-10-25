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

print("espero: True")
print(tablero_bien_formado([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]))

print("espero: False")
print(tablero_bien_formado([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0],[0,0,0]]))


# problema posición_en_tablero ( in pos : Posición ) : Bool {
        # requiere { True }
        # asegura { res = true ←→ posiciónEnTablero (pos) }
        # }

# aux posiciónEnTablero (pos : Posición ) :=
        # 0 ≤ pos. fila < Alto
        # ∧ 0 ≤ pos. columna < Ancho


def posicion_en_tablero(pos : Posicion) -> bool:
        
        if (0 <= pos.fila < ALTO) and (0 <= pos.columna < ANCHO): # si la pos pertenece al tablero...
                return True
        else: 
                return False
    

# problema movimiento_bien_formado ( in m : Movimiento ) : Bool {
        # requiere { True }
        # asegura { res = true ←→ movimientoBienFormado (m) }
        # }

# aux movimientoBienFormado (m : Movimiento ) :=
# posiciónEnTablero (m. origen )
        # ∧ (m. acción = Mover_a_secas → |m. pasos | = 1)
        # ∧ (m. acción = Arrastrar → |m. pasos | = 2)
        # ∧ (m. acción = Empujar → |m. pasos | = 2)


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


def juego_bien_formado(j : Juego) -> bool:
   return tablero_bien_formado(j.tablero) and (0 <= j.pasosConsumidos < MAX_PASOS)

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

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    

    if   d == NORTE:
        resultado: Posicion  = (pos.fila +1, pos.columna)
    elif d == SUR:
         resultado = (pos.fila - 1, pos.columna)
    elif d == ESTE:
         resultado = (pos.fila, pos.columna + 1)
    else:
        resultado = (pos.fila, pos.columna - 1)

    return resultado

# problema casilla_en_posición ( in t : Tablero , in pos : Posición ) : Casilla {
    # requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
    # asegura { res = t[pos. fila ][pos. columna ] }
    
def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    return t[p.fila][p.columna]

# problema hay_casilla_vac í a ( in t : Tablero , in pos : Posición ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posici ó nEnTablero (pos) }
    # asegura { res = true ←→ hayCasillaVacía(t, pos) }

# aux hayCasillaVacía(t : Tablero , pos : Posición ) :=
# posiciónEnTablero (pos)
# ∧ t[pos. fila ][pos. columna ] = Vacía

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    return (t[pos.fila][pos.columna] == VACIA)

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


def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
   
   return ( not(hay_casilla_vacia(t,pos)) and t[pos.fila][pos.columna].color == col )

#### Ejercicio 3

# problema hay_casilla_vacía_hacia ( in t : Tablero , in pos : Posición , in d : Dirección ) : Bool {
    # requiere { tableroBienFormado (t) ∧ posiciónEnTablero (pos) }
    # asegura { res = true ←→ hayCasillaVacíaHacia (t, pos, d) }

# aux hayCasillaVacíaHacia (t : Tablero , pos : Posición , d : Dirección ) :=
    # existe pos′: Posición . (
    # esPosicionVecinaHacia (pos, d, pos′ )
    # ∧ hayCasillaVacía(t, pos′ )

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    
    pos_vecina: Posicion = posicion_vecina_hacia(pos,d)

    return posicion_en_tablero(pos_vecina) and hay_casilla_vacia(pos_vecina)


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

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:

    direcciones: list[Direccion] = [NORTE,SUR,ESTE,OESTE]
    color = t[pos.fila][pos.columna].color

    for d in direcciones:
        pos_vecina: Posicion = (posicion_vecina_hacia(pos,d))

        if not ( hay_casilla_vacia(t,pos)):
            pieza: Pieza = t[pos_vecina.fila][pos_vecina.columna]
            if pieza.color == color:
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

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    
    fuerza_pos = fuerza(t[pos.fila][pos.columna].figura)
    
    pos_en_direccion: Posicion = posicion_vecina_hacia(pos,d)

    fuerza_vecina = fuerza(t[pos_en_direccion.fila][pos_en_direccion.columna].figura)

    if posicion_en_tablero(pos_en_direcion):
         
         if t[pos_en_direccion.fila][pos_en_direccion.columna].color == t[pos.fila][pos.columna].color:
              return False
         else:
              if  fuerza_pos > fuerza_vecina:
                   return True
              else:
                   return False

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

#### Ejercicio 4

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    raise Exception("No implementado")

#### Ejercicio 5

def activar_trampas(t : Tablero) -> Tablero:
    raise Exception("No implementado")

#### Ejercicio 6

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    raise Exception("No implementado")

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")

