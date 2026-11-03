
def tablero_8x8_inicial_ejemplo():
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


juegoprueba2 = Juego(tablero_8x8_inicial_ejemplo(), DORADO, 0)

print(todos_los_movimientos_posibles(juegoprueba2))
def caso2(self):
        t = leer_tablero([
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
        j = Juego(t,PLATEADO,1)
        listaDeMovimientos: list[Movimiento]=[]
        pruebaJuego:list[Movimiento]= todos_los_movimientos_posibles(j)

        self.assertEqual(listaDeMovimientos,pruebaJuego)



def tablero_8x8_inicial_ejemplo():
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


juegoprueba2 = Juego(tablero_8x8_inicial_ejemplo(), DORADO, 0)

print(todos_los_movimientos_posibles(juegoprueba2))

class todos_los_movimientos_posibles(unittest.TestCase):
    def test_vacio(self):
        t = leer_tablero([
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
        j = Juego(t,DORADO,1)
        listaDeMovimientos: list[Movimiento]=[]
        pruebaJuego:list[Movimiento]= todos_los_movimientos_posibles(j)

        self.assertEqual(listaDeMovimientos,pruebaJuego)



