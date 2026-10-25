import unittest
from arimaa import *

# Las piezas se representan con las siguientes letras:
#   E : elefante
#   M : camello
#   H : caballo
#   D : perro
#   C : gato
#   R : ratón
# donde
#   mayúscula : dorado
#   minúscula : plateado

def tablero_8x8_vacio():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_8x8_inicial_ejemplo():
    return leer_tablero([
              'hcdmedch', #7
              'rrrrrrrr', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              'RRRRRRRR', #1
              'HCDMEDCH', #0
              #01234567
            ])

def tablero_9x8_vacio():
    return leer_tablero([
              '--------', #8
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
def tablero_una_fila_mas_larga():
    return leer_tablero([
        '--------', #7
        '--------', #6
        '--------', #5
        '--------', #4
        '--------', #3
        '--------', #2
        '--------', #1
        '---------', #0
        #012345678
    ])

#### Ejercicio 1

class test_tablero_bien_formado(unittest.TestCase):

    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

    def test_tablero_vacio(self):
        t = tablero_8x8_vacio()
        self.assertTrue(tablero_bien_formado(t))

    def test_sin_tablero(self):
        t = leer_tablero([])
        self.assertFalse(tablero_bien_formado(t))

    def test_tablero_9x8(self):
        t = tablero_9x8_vacio()
        self.assertFalse(tablero_bien_formado(t))

    def test_tablero_una_fila_mas_larga(self):
        t = tablero_una_fila_mas_larga()
        self.assertFalse(tablero_bien_formado(t))


class test_posicion_en_tablero(unittest.TestCase):
#  (fila,columna) ambos entre 0 y 7 inclusive
    def test_posicion_ok(self):
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))

    def test_fila_debajo_de_tablero(self):
        self.assertFalse(posicion_en_tablero(Posicion(-1,0)))

    def test_columna_debajo_de_tablero(self):
        self.assertFalse(posicion_en_tablero(Posicion(1,-7)))

    def test_fila_arriba_de_tablero(self):
        self.assertFalse(posicion_en_tablero(Posicion(8,2)))

    def test_columna_arriba_de_tablero(self):
        self.assertFalse(posicion_en_tablero(Posicion(7,8)))

    def test_ambos_debajo(self):
        self.assertFalse(posicion_en_tablero(Posicion(-1,-2)))

    def test_ambos_arriba(self):
        self.assertFalse(posicion_en_tablero(Posicion(8,8)))

class test_movimiento_bien_formado(unittest.TestCase):

    def test_mover_a_secas_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))

    def test_arrastrar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,ESTE])))

    def test_empujar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [NORTE,ESTE])))

    def test_posicion_fuera(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(-1, -1), [NORTE])))

#   def test_accion_mal(self):
#       self.assertFalse(movimiento_bien_formado(Movimiento(cualquiercosa, Posicion(0, 1), [SUR])))
# me da error cuando le doy otra cosa que no sea un movimiento valido. 
    def test_mover_a_secas_mal(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [ ])))

    def test_arrastrar_mal(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [ ])))

    def test_empujar_mal(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [ ])))

    
class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok1(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_ok2(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 3)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_mal_tablero(self):
        j = Juego(tablero_9x8_vacio(),PLATEADO,3)
        self.assertFalse(juego_bien_formado(j))

    # def test_juego_mal_turno(self):
    #     j = Juego(tablero_8x8_inicial_ejemplo(), cualquiercosa, 3)
    #    self.assertFalse(juego_bien_formado(j))       idem linea 129, me da error con un color que no reconoce en vez de False

    def test_juego_mas_pasos_cosumidos(self):
        j = Juego(tablero_8x8_inicial_ejemplo(), PLATEADO, 4)

#### Ejercicio 2


class test_posicion_vecina_hacia(unittest.TestCase):

    def test_posicion_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))

    def test_posicion_vecina_al_norte_fuera_de_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(-1,0), NORTE), Posicion(0, 0))

    def test_posicion_vecina_al_sur(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(7,0), SUR), Posicion(6, 0))

    def test_posicion_vecina_al_sur_fuera_de_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(-1,-1), SUR), Posicion(-2, -1))

    def test_posicion_vecina_al_oeste(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(7,1), OESTE), Posicion(7, 0))

    def test_posicion_vecina_al_oeste_fuera_de_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(-1,-1), OESTE), Posicion(-1, -2))

    def test_posicion_vecina_al_este(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(7,6), ESTE), Posicion(7, 7))
    
    def test_posicion_vecina_al_este_fuera_de_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(1,8), ESTE), Posicion(1, 9))


class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas_vertical(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

    def test_vecinas_horizontal(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0,0), Posicion(0, 1)))

    def test_son_vecinas_fuera_tablero(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(-1,-1),Posicion(-1,-2)))

    def test_son_vecinas_diagonales(self):
        self.assertFalse(son_posiciones_vecinas(Posicion(0,0), Posicion(1, 1)))


class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion_figura(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

    def test_casilla_en_posicion_vacia(self):
        t = tablero_8x8_vacio()
        self.assertEqual(casilla_en_posicion(t,Posicion(1,1)), CasillaVacia.VACIA)

    def test_casilla_vacia_en_posicion_trampa(self):
        t = tablero_8x8_vacio()
        self.assertEqual(casilla_en_posicion(t,Posicion(2,2)), CasillaVacia.VACIA)

    def test_casilla_en_posicion_figura_en_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertNotEqual(casilla_en_posicion(t,Posicion(0,0)), CasillaVacia.VACIA)

    def test_casilla_vacia_comparada_con_pieza(self):
        t = tablero_8x8_vacio()
        self.assertNotEqual(casilla_en_posicion(t,Posicion(0,0)), Pieza(CONEJO, PLATEADO))

    def test_casilla_figura_mal(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertNotEqual(casilla_en_posicion(t,Posicion(1,0)), Pieza(CABALLO, DORADO))

    def test_casilla_color_mal(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertNotEqual(casilla_en_posicion(t,Posicion(1,0)), Pieza(CONEJO, PLATEADO))

class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 0)))

    def test_casilla_no_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 0)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

    def test_hay_pieza_de_color_distinto(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t,Posicion(0,7), PLATEADO))

    def test_hay_pieza_de_color_en_tablero_vacio(self):
        t = tablero_8x8_vacio()
        self.assertFalse(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

#### Ejercicio 3

class test_hay_casilla_vacia_hacia(unittest.TestCase):

    def test_hay_casilla_vacia_hacia_ok(self):
        t = tablero_8x8_vacio()
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))
