# EJERCICIO 1 EXTRA ----------------------------------------------------------------------------
class test_posiciones_de_las_piezas(unittest.TestCase):

    def test_sin_piezas(self):
        t = tablero_8x8_vacio()
        j = Juego(t , DORADO, 0)
        self.assertEqual(posiciones_de_las_piezas(j),{})

    def test_figuras_iguales_distinto_color(self):
        t = leer_tablero([
            '--d----D', #7
            '--------', #6
            '--------', #5
            '--------', #4
            '---D----', #3
            '-----d--', #2
            '--------', #1
            '--------', #0
            #01234567
            ])
        j = Juego(t , DORADO, 0)
        self.assertEqual((posiciones_de_las_piezas(j)) , {Pieza(PERRO, PLATEADO): [Posicion(2,5), Posicion(7,2)] , Pieza(PERRO, DORADO) : [Posicion(3,3),Posicion(7,7)]})

    def test_figuras_distintas_mismo_color(self):
            t = leer_tablero([
                '--H-----', #7
                '--------', #6
                '--------', #5
                '--------', #4
                '---D----', #3
                '-----r--', #2
                'h-------', #1
                '--------', #0
                #01234567
                ])
            j = Juego(t , PLATEADO, 0)
            self.assertEqual((posiciones_de_las_piezas(j)) , {Pieza(CABALLO, PLATEADO): [Posicion(1,0)] , Pieza(CONEJO, PLATEADO) : [Posicion(2,5)], Pieza(PERRO, DORADO) : [Posicion(3,3)], Pieza(CABALLO, DORADO) : [Posicion(7,2)]})


# EJERCICIO 2 EXTRA -----------------------------------------------------------------------------

class test_todos_los_movimientos_posibles(unittest.TestCase):
    def test_movs_dorados(self):
        def tablero_ejemplo_hyr():
            return leer_tablero([
              'h-------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '-------R', #1
              '-------H', #0
              #01234567
            ])
        juegoprueba2 = Juego(tablero_ejemplo_hyr(), DORADO, 0)
        res_esperado = [Movimiento(MOVER_A_SECAS,Posicion(0,7),[OESTE]) , Movimiento(MOVER_A_SECAS,Posicion(1,7),[NORTE]), Movimiento(MOVER_A_SECAS,Posicion(1,7),[OESTE]) ]
        self.assertEqual(todos_los_movimientos_posibles(juegoprueba2) , res_esperado)

    def test_vacio(self):
        t = tablero_8x8_vacio()
        res_esperado = []
        juegoprueba3 = Juego(t, PLATEADO, 0)
        self.assertEqual(todos_los_movimientos_posibles(juegoprueba3), res_esperado)
        
