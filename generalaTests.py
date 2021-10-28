import unittest
import generala

class TestsGenerala(unittest.TestCase):
    
    #Tests de estado del juego
    
    def test_estado_inicial(self):
        x = generala.Generala(jugadores = [], turno = None)
        self.assertEqual(
            [isinstance(x, generala.Generala),
            len(x.jugadores) == 2,
            isinstance(x.jugadores[0], generala.Jugador), 
            isinstance(x.jugadores[1], generala.Jugador),
            x.turno is None,
            isinstance(x.tabla, generala.Tabla),
            x.tabla.jugadas == [['X' for y in range(10)] for x in range(2)]],
            [True for x in range(7)] 
        )
    
    def test_estado_turno(self):
        x = generala.Turno(generala.Jugador(0))
        self.assertEqual(
            [isinstance(x, generala.Turno),
            isinstance(x.jugador, generala.Jugador),
            isinstance(x.dados, generala.Dados),
            len(x.dados.dados) == 0,
            x.nro_lanzamientos == 0],
            [True for x in range(5)]
        )
    
    def test_juego_en_curso(self):
        x = generala.Generala(jugadores = [], turno = None)
        self.assertFalse(
            x.tabla.juego_terminado()
        )
    
    #Tests de turnos y lanzamientos
    
    def test_determinar_siguiente_turno(self):
        x = generala.Generala(jugadores = [], turno = None)
        self.assertEqual(x.determinar_turno_siguiente(), x.jugadores[0])

    def test_2_determinar_siguiente_turno(self):
        x = generala.Generala(jugadores = [], turno = None)
        x.turno = generala.Turno(x.jugadores[1])
        self.assertEqual(x.determinar_turno_siguiente(), x.jugadores[0])

    def test_3_determinar_siguiente_turno(self):
        x = generala.Generala(jugadores = [], turno = None)
        x.turno = generala.Turno(x.jugadores[0])
        self.assertEqual(x.determinar_turno_siguiente(), x.jugadores[1])

    def test_realizar_lanzamiento_inicial(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 0)
        x.realizar_lanzamiento()
        self.assertEqual(
            [len(x.dados.dados) == 5,
            x.nro_lanzamientos == 1],
            [True for x in range(2)]
        )
        self.assertEqual(
            [y in (1, 2, 3, 4, 5, 6) for y in x.dados.dados],
            [True for x in range(5)]
        )
    
    def test_realizar_segundo_lanzamiento(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 0)
        x.realizar_lanzamiento()
        x.realizar_lanzamiento()
        self.assertEqual(
            [len(x.dados.dados) == 5,
            x.nro_lanzamientos == 2],
            [True for x in range(2)]
        )
        self.assertEqual(
            [y in (1, 2, 3, 4, 5, 6) for y in x.dados.dados],
            [True for x in range(5)]
        )
    
    def test_realizar_tercer_lanzamiento(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 0)
        x.realizar_lanzamiento()
        x.realizar_lanzamiento()
        x.realizar_lanzamiento()
        self.assertEqual(
            [len(x.dados.dados) == 5,
            x.nro_lanzamientos == 3],
            [True for x in range(2)]
        )
        self.assertEqual(
            [y in (1, 2, 3, 4, 5, 6) for y in x.dados.dados],
            [True for x in range(5)]
        )
    
    #Tests de dados
    
    def test_mantener_algunos_dados(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 0)
        x.dados.dados = [1, 4, 5, 6, 2]
        x.realizar_lanzamiento(dados_a_mantener = [0, 1, 2])
        self.assertEqual(
            [len(x.dados.dados) == 5,
            x.nro_lanzamientos == 1,
            x.dados.dados[:3:] == [1, 4, 5]],
            [True for x in range(3)]
        )
        self.assertEqual(
            [y in (1, 2, 3, 4, 5, 6) for y in x.dados.dados],
            [True for x in range(5)]
        )
    
    def test_2_mantener_algunos_dados(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 0)
        x.dados.dados = [6, 3, 5, 4, 2]
        x.realizar_lanzamiento(dados_a_mantener = [3, 4])
        self.assertEqual(
            [len(x.dados.dados) == 5,
            x.nro_lanzamientos == 1,
            x.dados.dados[:2:] == [4, 2]],
            [True for x in range(3)]
        )
        self.assertEqual(
            [y in (1, 2, 3, 4, 5, 6) for y in x.dados.dados],
            [True for x in range(5)]
        )
    
    #Tests del estado de las jugadas
    
    def test_verificar_estado_jugada_1(self):
        x = generala.Dados()
        x.dados = [1, 1, 3, 4, 1]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 3,
                x.verificar_estado_juegos('2') == 0,
                x.verificar_estado_juegos('3') == 1,
                x.verificar_estado_juegos('4') == 1,
                x.verificar_estado_juegos('5') == 0,
                x.verificar_estado_juegos('6') == 0,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == False,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )

    def test_verificar_estado_jugada_2(self):
        x = generala.Dados()
        x.dados = [1, 2, 3, 6, 6]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 1,
                x.verificar_estado_juegos('2') == 1,
                x.verificar_estado_juegos('3') == 1,
                x.verificar_estado_juegos('4') == 0,
                x.verificar_estado_juegos('5') == 0,
                x.verificar_estado_juegos('6') == 2,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == False,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_3(self):
        x = generala.Dados()
        x.dados = [1, 1, 6, 5, 4]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 2,
                x.verificar_estado_juegos('2') == 0,
                x.verificar_estado_juegos('3') == 0,
                x.verificar_estado_juegos('4') == 1,
                x.verificar_estado_juegos('5') == 1,
                x.verificar_estado_juegos('6') == 1,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == False,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_4(self):
        x = generala.Dados()
        x.dados = [1, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 1,
                x.verificar_estado_juegos('2') == 1,
                x.verificar_estado_juegos('3') == 1,
                x.verificar_estado_juegos('4') == 1,
                x.verificar_estado_juegos('5') == 1,
                x.verificar_estado_juegos('6') == 0,
                x.verificar_estado_juegos('ESCALERA') == True,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == False,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_5(self):
        x = generala.Dados()
        x.dados = [6, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 0,
                x.verificar_estado_juegos('2') == 1,
                x.verificar_estado_juegos('3') == 1,
                x.verificar_estado_juegos('4') == 1,
                x.verificar_estado_juegos('5') == 1,
                x.verificar_estado_juegos('6') == 1,
                x.verificar_estado_juegos('ESCALERA') == True,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == False,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_6(self):
        x = generala.Dados()
        x.dados = [1, 5, 5, 1, 1]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 3,
                x.verificar_estado_juegos('2') == 0,
                x.verificar_estado_juegos('3') == 0,
                x.verificar_estado_juegos('4') == 0,
                x.verificar_estado_juegos('5') == 2,
                x.verificar_estado_juegos('6') == 0,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == True,
                x.verificar_estado_juegos('POKER') == False,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_7(self):
        x = generala.Dados()
        x.dados = [2, 2, 2, 3, 3]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 0,
                x.verificar_estado_juegos('2') == 3,
                x.verificar_estado_juegos('3') == 2,
                x.verificar_estado_juegos('4') == 0,
                x.verificar_estado_juegos('5') == 0,
                x.verificar_estado_juegos('6') == 0,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == True,
                x.verificar_estado_juegos('POKER') == False,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_8(self):
        x = generala.Dados()
        x.dados = [1, 5, 5, 5, 5]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 1,
                x.verificar_estado_juegos('2') == 0,
                x.verificar_estado_juegos('3') == 0,
                x.verificar_estado_juegos('4') == 0,
                x.verificar_estado_juegos('5') == 4,
                x.verificar_estado_juegos('6') == 0,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == True,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_9(self):
        x = generala.Dados()
        x.dados = [4, 4, 4, 4, 2]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 0,
                x.verificar_estado_juegos('2') == 1,
                x.verificar_estado_juegos('3') == 0,
                x.verificar_estado_juegos('4') == 4,
                x.verificar_estado_juegos('5') == 0,
                x.verificar_estado_juegos('6') == 0,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == True,
                x.verificar_estado_juegos('GENERALA') == False
            ],
            [True for x in range(10)]
        )
    
    def test_verificar_estado_jugada_10(self):
        x = generala.Dados()
        x.dados = [6, 6, 6, 6, 6]
        self.assertEqual(
            [
                x.verificar_estado_juegos('1') == 0,
                x.verificar_estado_juegos('2') == 0,
                x.verificar_estado_juegos('3') == 0,
                x.verificar_estado_juegos('4') == 0,
                x.verificar_estado_juegos('5') == 0,
                x.verificar_estado_juegos('6') == 5,
                x.verificar_estado_juegos('ESCALERA') == False,
                x.verificar_estado_juegos('FULL') == False,
                x.verificar_estado_juegos('POKER') == True,
                x.verificar_estado_juegos('GENERALA') == True
            ],
            [True for x in range(10)]
        )
    
    #Tests del cálculo de puntos
    
    def test_calcular_puntos_1_primer_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [1, 1, 3, 4, 1]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_1_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [1, 1, 3, 4, 1]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_1_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [1, 1, 3, 4, 1]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_2_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [1, 2, 3, 6, 6]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 12,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_2_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [1, 2, 3, 6, 6]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 12,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_2_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [1, 2, 3, 6, 6]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 12,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_3_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [1, 1, 6, 5, 4]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_3_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [1, 1, 6, 5, 4]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_3_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [1, 1, 6, 5, 4]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_4_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [1, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 25,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_4_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [1, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 20,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_4_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [1, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 20,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_5_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [6, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 25,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_5_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [6, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 20,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_5_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [6, 5, 3, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 4,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 5,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 20,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_6_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [1, 5, 5, 1, 1]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 10,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 35,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_6_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [1, 5, 5, 1, 1]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 10,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 30,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_6_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [1, 5, 5, 1, 1]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 3,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 10,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 30,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_7_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [2, 2, 2, 3, 3]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 35,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_7_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [2, 2, 2, 3, 3]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 30,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_7_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [2, 2, 2, 3, 3]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 6,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 30,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_8_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [1, 5, 5, 5, 5]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 20,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 45,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_8_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [1, 5, 5, 5, 5]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 20,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 40,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_8_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [1, 5, 5, 5, 5]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 1,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 20,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 40,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_9_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [4, 4, 4, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 16,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 45,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_9_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [4, 4, 4, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 16,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 40,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_9_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [4, 4, 4, 4, 2]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 2,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 16,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 40,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 0
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_10_primera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 1)
        x.dados.dados = [6, 6, 6, 6, 6]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 30,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 45,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 50
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_10_segunda_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 2)
        x.dados.dados = [6, 6, 6, 6, 6]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 30,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 40,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 50
            ],
            [True for x in range(10)]
        )
    
    def test_calcular_puntos_10_tercera_tirada(self):
        x = generala.Turno(generala.Jugador(1), nro_lanzamientos = 3)
        x.dados.dados = [6, 6, 6, 6, 6]
        self.assertEqual(
            [
                x.dados.calcular_puntos(x.nro_lanzamientos, '1', x.dados.verificar_estado_juegos('1')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '2', x.dados.verificar_estado_juegos('2')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '3', x.dados.verificar_estado_juegos('3')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '4', x.dados.verificar_estado_juegos('4')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '5', x.dados.verificar_estado_juegos('5')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, '6', x.dados.verificar_estado_juegos('6')) == 30,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'ESCALERA', x.dados.verificar_estado_juegos('ESCALERA')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'FULL', x.dados.verificar_estado_juegos('FULL')) == 0,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'POKER', x.dados.verificar_estado_juegos('POKER')) == 40,
                x.dados.calcular_puntos(x.nro_lanzamientos, 'GENERALA', x.dados.verificar_estado_juegos('GENERALA')) == 50
            ],
            [True for x in range(10)]
        )
    
    #Tests de verificación y anotación de jugadas
    
    def test_anotar_J1_1_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 0))
        )
        x.anotar_jugada(x.jugadores[0], 5, 0)
        self.assertEqual(
            x.jugadas,
            [[5, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_1_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[[1, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 0))
        )
    
    def test_anotar_J1_2_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 1))
        )
        x.anotar_jugada(x.jugadores[0], 4, 1)
        self.assertEqual(
            x.jugadas,
            [['X', 4, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_2_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 6, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 1))
        )
    
    def test_anotar_J1_3_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 2))
        )
        x.anotar_jugada(x.jugadores[0], 9, 2)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 9, 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_3_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 9, 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 2))
        )
    
    def test_anotar_J1_4_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 3))
        )
        x.anotar_jugada(x.jugadores[0], 4, 3)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 4, 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_4_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 4, 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 3))
        )
    
    def test_anotar_J1_5_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 4))
        )
        x.anotar_jugada(x.jugadores[0], 10, 4)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 10, 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_5_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 10, 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 4))
        )
    
    def test_anotar_J1_6_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 5))
        )
        x.anotar_jugada(x.jugadores[0], 6, 5)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 6, 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_6_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 6, 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 5))
        )
    
    def test_anotar_J1_7_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 6))
        )
        x.anotar_jugada(x.jugadores[0], 25, 6)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 25, 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_7_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 25, 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 6))
        )
    
    def test_anotar_J1_8_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 7))
        )
        x.anotar_jugada(x.jugadores[0], 35, 7)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 35, 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_8_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 35, 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 7))
        )
    
    def test_anotar_J1_9_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 8))
        )
        x.anotar_jugada(x.jugadores[0], 45, 8)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 45, 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_9_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 45, 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 8))
        )
    
    def test_anotar_J1_10_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 9))
        )
        x.anotar_jugada(x.jugadores[0], 50, 9)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 50],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J1_10_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 50],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[0].numero - 1, 9))
        )
    
    def test_anotar_J2_1_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 0))
        )
        x.anotar_jugada(x.jugadores[1], 5, 0)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],[5, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J2_1_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],[1, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 0))
        )
    
    def test_anotar_J2_2_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 1))
        )
        x.anotar_jugada(x.jugadores[1], 4, 1)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 4, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J2_2_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 6, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 1))
        )
    
    def test_anotar_J2_3_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 2))
        )
        x.anotar_jugada(x.jugadores[1], 9, 2)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 9, 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J2_3_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 9, 'X', 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 2))
        )
    
    def test_anotar_J2_4_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 3))
        )
        x.anotar_jugada(x.jugadores[1], 4, 3)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 4, 'X', 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J2_4_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 4, 'X', 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 3))
        )
    
    def test_anotar_J2_5_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 4))
        )
        x.anotar_jugada(x.jugadores[1], 10, 4)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 10, 'X', 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J2_5_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 10, 'X', 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 4))
        )
    
    def test_anotar_J2_6_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 5))
        )
        x.anotar_jugada(x.jugadores[1], 6, 5)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 6, 'X', 'X', 'X', 'X']]
        )
    
    def test_anotar_J2_6_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 6, 'X', 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 5))
        )
    
    def test_anotar_J2_7_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 6))
        )
        x.anotar_jugada(x.jugadores[1], 25, 6)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 25, 'X', 'X', 'X']]
        )
    
    def test_anotar_J2_7_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 25, 'X', 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 6))
        )
    
    def test_anotar_J2_8_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 7))
        )
        x.anotar_jugada(x.jugadores[1], 35, 7)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 35, 'X', 'X']]
        )
    
    def test_anotar_J2_8_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 35, 'X', 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 7))
        )
    
    def test_anotar_J2_9_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 8))
        )
        x.anotar_jugada(x.jugadores[1], 45, 8)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 45, 'X']]
        )
    
    def test_anotar_J2_9_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 45, 'X']])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 8))
        )
    
    def test_anotar_J2_10_válido(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X' for x in range(10)] for y in range(2)])
        self.assertTrue(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 9))
        )
        x.anotar_jugada(x.jugadores[1], 50, 9)
        self.assertEqual(
            x.jugadas,
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 50]]
        )
    
    def test_anotar_J2_10_ya_jugado(self):
        x = generala.Tabla([generala.Jugador(1), generala.Jugador(2)], jugadas=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 50]])
        self.assertFalse(
            x.verificar_jugada_no_realizada((x.jugadores[1].numero - 1, 9))
        )
    
    #Test de fin de juego
    
    def test_juego_terminado(self):
        x = generala.Generala(jugadores = [], turno = None)
        x.tabla.jugadas = [[0 for x in range(10)] for y in range(2)]
        self.assertTrue(
            x.tabla.juego_terminado()
        )
    
    def test_partida_empatada(self):
        x = generala.Generala(jugadores = [], turno = None)
        x.tabla.jugadas = [[0 for x in range(10)] for y in range(2)]
        self.assertEqual(
            x.tabla.determinar_ganador(),
            (None, 0)
        )
    
    def test_J1_ganador(self):
        x = generala.Generala(jugadores = [], turno = None)
        x.tabla.jugadas = [[4 for x in range(10)], [1 for y in range(10)]]
        self.assertEqual(
            x.tabla.determinar_ganador(),
            (1, 40, 10)
        )
    
    def test_J2_ganador(self):
        x = generala.Generala(jugadores = [], turno = None)
        x.tabla.jugadas = [[3 for x in range(10)], [6 for y in range(10)]]
        self.assertEqual(
            x.tabla.determinar_ganador(),
            (2, 30, 60)
        )

if __name__ == '__main__':
    unittest.main()