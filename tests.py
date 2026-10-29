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

# def test_accion_mal(self):
#   self.assertFalse(movimiento_bien_formado(Movimiento(cualquiercosa, Posicion(0, 1), [SUR])))
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


class test_son_posiciones_vecinas(unittest.TestCase): #definida antes del Ej 1

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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(1, 1), NORTE))

    def test_hay_casilla_vacia_hacia_mal(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(0, 7), NORTE))

    def test_hay_casilla_vacia_hacia_mal(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(1, 7), SUR))

    def test_hay_casilla_vacia_hacia_desde_vacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(1, 1), NORTE))

class test_hay_pieza_amiga_vecina(unittest.TestCase):

    def test_hay_pieza_amiga_vecina_ok(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))

#    def test_hay_pieza_amiga_vecina_en_vacia(self): No tiene sentido hacer este test pues hacia
#                                                    donde se busca una aliada no puede estar vacia        

    def test_hay_pieza_amiga_vecina_ok_dos(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t,Posicion(7, 0)))

    def test_no_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
            'R-hRD-Rr', #7
            'M----d--', #6
            '-h-rrCR-', #5
            'R-rcE---', #4
            '--drRR--', #3
            '-HD-H--m', #2
            '--r-RCc-', #1
            're---r--', #0
            #01234567
            ])
        self.assertFalse(hay_pieza_amiga_vecina(t,Posicion(2, 7)))

    def test_no_hay_pieza_amiga_vecina_dos(self):
        t = leer_tablero([
            'R-hRD-Rr', #7
            'M----d--', #6
            '-h-rrCR-', #5
            'R-rcE---', #4
            '--drRR--', #3
            '-HD-H--m', #2
            '--r-RCc-', #1
            're---r--', #0
            #01234567
            ])
        self.assertFalse(hay_pieza_amiga_vecina(t,Posicion(7, 7)))

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia_ok(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))

    def test_hay_pieza_enemiga_mas_debil_hacia_fuera(self):
        t = leer_tablero([
                '--Hdm---', #7
                'r--HhC--', #6
                'e---R-C-', #5
                'ME--d---', #4
                'h--RDcRr', #3
                'R-R-r--r', #2
                '-RRcrRD-', #1
                '--r---rr', #0
                #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(0, 2), ESTE))

    def test_hay_pieza_enemiga_mas_debil_hacia_vacia(self):
        t = leer_tablero([
                '--Hdm---', #7
                'r--HhC--', #6
                'e---R-C-', #5
                'ME--d---', #4
                'h--RDcRr', #3
                'R-R-r--r', #2
                '-RRcrRD-', #1
                '--r---rr', #0
                #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(0, 2), OESTE))

    def test_hay_pieza_enemiga_mas_debil_hacia_mismo_color(self):
        t = leer_tablero([
                '--Hdm---', #7
                'r--HhC--', #6
                'e---R-C-', #5
                'ME--d---', #4
                'h--RDcRr', #3
                'R-R-r--r', #2
                '-RRcrRD-', #1
                '--r---rr', #0
                #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(4, 0), ESTE))

    def test_hay_pieza_enemiga_mas_debil_hacia_misma_fuerza(self):
        t = leer_tablero([
                '--Hdm---', #7
                'r--HhC--', #6
                'e---R-C-', #5
                'ME--d---', #4
                'h--RDcRr', #3
                'R-R-r--r', #2
                '-RRcrRD-', #1
                '--r---rr', #0
                #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(3, 6), ESTE))

class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina_ok(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

    def test_hay_pieza_enemiga_mas_fuerte_vecina_falso(self):
            t = leer_tablero([
                  'R-e--mRr', #7
                  '------dE', #6
                  'h--Rr-RR', #5
                  'c--R-C--', #4
                  '-rCHDrr-', #3
                  '----rc--', #2
                  'h-R-M-R-', #1
                  'rr-D-dH-', #0
                  #01234567
                ])
            self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(0, 6)))

    def test_hay_pieza_enemiga_mas_fuerte_vecina_ok_dos(self):
                t = leer_tablero([
                      'R-e--mRr', #7
                      '------dE', #6
                      'h--Rr-RR', #5
                      'c--R-C--', #4
                      '-rCHDrr-', #3
                      '----rc--', #2
                      'h-R-M-R-', #1
                      'rr-D-dH-', #0
                      #01234567
                    ])
                self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(7, 7)))

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada_ok(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))

    def test_hay_pieza_congelada_en_vacia(self):
        t = leer_tablero([
                '--d--H-D', #7
                '-hMc--r-', #6
                '--r--C-H', #5
                '--------', #4
                '-CeD----', #3
                '---R----', #2
                '--------', #1
                '--------', #0
                #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(0, 0)))

    def test_hay_pieza_congelada_no_hay_enemiga(self):
        t = leer_tablero([
                '--d--H-D', #7
                '-hMc--r-', #6
                '--r--C-H', #5
                '--------', #4
                '-CeD----', #3
                '---R----', #2
                '--------', #1
                '--------', #0
                #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(3, 2)))

    def test_hay_pieza_congelada_hay_aliada(self):
        t = leer_tablero([
                '--d--H-D', #7
                '-hMc--r-', #6
                '--r--C-H', #5
                '--------', #4
                '-CeD----', #3
                '---R----', #2
                '--------', #1
                '--------', #0
                #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(3, 3)))

"""
#### Ejercicio 4

class test_puede_realizar_movimiento(unittest.TestCase):

    def test_mover_a_secas_ok(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

#### Ejercicio 5

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

#### Ejercicio 6
"""


class test_realizar_movimiento(unittest.TestCase):
  
    def test_mover_a_secas(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---m----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '--------', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 1) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)


    def test_arrastrar(self):
            t0 = leer_tablero([
                'rrrr-rrr', #7
                'ccddhh-e', #6
                '--------', #5
                '-rM-----', #4
                '--H-----', #3
                '--------', #2
                'E--HDDCC', #1
                'RRRRRRRR', #0
                #01234567
                ])
            tN = leer_tablero([
                'rrrr-rrr', #7
                'ccddhh-e', #6
                '--------', #5
                '--rM----', #4
                '--H-----', #3
                '--------', #2
                'E--HDDCC', #1
                'RRRRRRRR', #0
                #01234567
                ])
            j0 = Juego(t0, DORADO, 0) 
            jN = Juego(tN, DORADO, 2) 
            mN = Movimiento(ARRASTRAR, Posicion(4, 2), [ESTE,ESTE])
            self.assertTrue(puede_realizar_movimiento(j0, mN))
            self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_empujar(self):
            t0 = leer_tablero([
                'rrrr-rrr', #7
                'ccdd-h-e', #6
                '--------', #5
                '--Rm----', #4
                '--h-----', #3
                '--------', #2
                'E--HDDCC', #1
                'R-RRRRRR', #0
                #01234567
                ])
            tN = leer_tablero([
                'rrrr-rrr', #7
                'ccdd-h-e', #6
                '--------', #5
                '--hm----', #4
                '--------', #3
                '--------', #2
                'E--HDDCC', #1
                'R-RRRRRR', #0
                #01234567
                ])
            j0 = Juego(t0, PLATEADO, 2) 
            jN = Juego(tN, DORADO, 0) 
            mN = Movimiento(EMPUJAR, Posicion(3, 2), [NORTE,NORTE])
            self.assertTrue(puede_realizar_movimiento(j0, mN))
            self.assertEqual(realizar_movimiento(j0, mN), jN)
            
"""

#### Ejercicio 7

class test_ganador_del_juego(unittest.TestCase):

    def test_promueve_conejo_dorado_turno_del_oponente(self):
        t = leer_tablero([
              'rr----Rr', #7
              'c-----me', #6
              '---Ed-R-', #5
              '-M---R--', #4
              '---R----', #3
              '-rrrr---', #2
              '-H---DCC', #1
              'R-----RR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)
"""

if __name__ == '__main__':
    unittest.main(verbosity=2)
