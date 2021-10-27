import random

class Generala():
    def __init__(self, jugadores = [], turno = None):
        self.jugadores = jugadores
        self.jugadores.extend([Jugador(1), Jugador(2)])
        self.tabla = Tabla(jugadores)
        self.turno = turno
      
    def determinar_turno_siguiente(self):
        return self.jugadores[0] if self.turno == None or not self.turno.jugador.numero % 2 else self.jugadores[1]
    
    def juego(self):
        print('GENERALA'.center(60, '='))
        while not self.tabla.juego_terminado():
            self.realizar_turno()
        x = self.tabla.determinar_ganador()
        if x[0] == None:
            print('¡El juego termina en EMPATE! Ambos jugadores tienen {} puntos.'.format(x[1]))
        else:
            print('¡J{} ha GANADO! J1: {} puntos.   J2: {} puntos.'.format(x[0], x[1], x[2]))

    def realizar_turno(self):
        self.turno = Turno(self.determinar_turno_siguiente())
        continuar, dados_a_mantener = True, None
        print('{}\n'.format(self.tabla))
        print(('TURNO DE J{}'.format(self.turno.jugador.numero)).center(50, '-'))
        while self.turno.nro_lanzamientos <= 2 and continuar:
            print('TIRADA Nº{}\n'.format(self.turno.nro_lanzamientos + 1))
            self.turno.realizar_lanzamiento(dados_a_mantener)
            print('Dados: {}\n'.format(self.turno.dados))
            while self.turno.nro_lanzamientos <= 2:
                try:
                    relanzar = input('¿Desea realizar un nuevo lanzamiento? (S/N)\n')
                    if relanzar not in ('S', 's', 'N', 'n'):
                        raise Exception('La entrada no es válida.\n')
                    elif relanzar in ('S', 's'):
                        print('\n¿Qué dados desea mantener?\n')
                        print('(Ingrese los números de las POSICIONES (1, 2, 3, 4 y/o 5) de los dados que NO desea volver a tirar,')
                        print(' e ingrese un 0 para dejar de ingresar dados).')
                        dados_a_mantener = []
                        while True:
                            try:
                                dado = input('\nDADO: ')
                                if not dado in ('0', '1', '2', '3', '4', '5'):
                                    raise Exception('El valor ingresado no es válido.')
                                if int(dado) - 1 in dados_a_mantener:
                                    raise Exception('La posición ingresada ya se ha conservado.')
                                if dado == '0':
                                    print('\n')
                                    break
                                dados_a_mantener.append(int(dado) - 1)
                                if len(dados_a_mantener) == 5:
                                    continuar = False  #si elige guardar los cinco dados, el juego continua como si hubiera elegido no realizar un nuevo lanzamiento
                            except Exception as e:
                                print('\nERROR: {}'.format(e))
                    else:
                        continuar = False
                    break
                except Exception as e:
                    print('\nERROR: {}'.format(e))
        self.anotar_jugada(self.turno.jugador)

    def anotar_jugada(self, jugador):
        juegos = ('1', '2', '3', '4', '5', '6', 'ESCALERA', 'FULL', 'POKER', 'GENERALA')
        print('\n¿Qué jugada desea anotar? (ingrese el nombre correspondiente)\n- 1, 2, 3, 4, 5, 6, Escalera, Full, Póker o Generala -')
        print('Recuerde que si no cumple las condiciones de la jugada elegida, se anotarán 0 puntos en la tabla.')
        while True:
            try:
                nombre_jugada = input('\nJUGADA: ')
                if nombre_jugada.upper() == 'PÓKER':
                    nombre_jugada = 'POKER'
                if nombre_jugada.upper() not in juegos:
                    raise Exception('El nombre de jugada ingresado no es válido.')
                fila_jugada = juegos.index(nombre_jugada.upper())
                if not self.tabla.verificar_jugada_no_realizada((jugador.numero - 1, fila_jugada)):
                    raise Exception('La jugada elegida ya fue realizada.')
                else:
                    break
            except Exception as e:
                print('\nERROR: {}'.format(e))
        self.tabla.anotar_jugada(
            jugador, 
            self.turno.dados.calcular_puntos(self.turno.nro_lanzamientos, nombre_jugada, self.turno.dados.verificar_estado_juegos(nombre_jugada)), 
            fila_jugada
            )  
            
            #anotar_jugada() toma como argumento el jugador, el puntaje a anotar y la fila de la tabla en la que está la jugada
            #calcular_puntos() toma como argumento la cantidad de lanzamientos que han tenido lugar en ese turno, la jugada a anotar y el estado de la misma

class Jugador():
    def __init__(self, numero):
        self.numero = numero
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, value):
        self.__numero = value

class Turno():
    def __init__(self, jugador, nro_lanzamientos = 0):
        self.dados = Dados()
        self.jugador = jugador
        self.nro_lanzamientos = nro_lanzamientos
    
    @property
    def nro_lanzamientos(self):
        return self.__nro_lanzamientos
    
    @nro_lanzamientos.setter
    def nro_lanzamientos(self, value):
        self.__nro_lanzamientos = value
        
    def realizar_lanzamiento(self, dados_a_mantener = None):
        self.dados.tirar_dados(dados_a_mantener)
        self.nro_lanzamientos += 1
    
class Dados():
    def __init__(self, dados = []):
        self.dados = dados

    @property
    def dados(self):
        return self.__dados

    @dados.setter
    def dados(self, value):
        self.__dados = value
    
    def tirar_dados(self, dados_a_mantener = None):
        if dados_a_mantener is not None:
            aux, i = [], 0
            for pos in dados_a_mantener:
                aux.append(self.dados.pop(pos - i))
                i += 1
            nuevos_dados = [random.randint(1,6) for x in range(len(self.dados))]
            self.dados = aux + nuevos_dados
        else:
            self.dados = [random.randint(1,6) for x in range(5)]
    
    def verificar_estado_juegos(self, jugada):  #para la jugada solicitada, devuelve la condición de la misma (cant. de 1s, 2s, ..., para las jugadas de números y verdadero o falso - 1 o 0 - para las demás).
        repetidos = []
        for x in range(1,7):
            if x in self.dados:
                repetidos.append(self.dados.count(x))
            else:
                repetidos.append(0)
        
        estado_jugadas = {  #diccionario de estados
            '1' : self.dados.count(1),
            '2' : self.dados.count(2),
            '3' : self.dados.count(3),
            '4' : self.dados.count(4),
            '5' : self.dados.count(5),
            '6' : self.dados.count(6),
            'escalera' : repetidos[:5:] == [1, 1, 1, 1, 1] or repetidos[1::] == [1, 1, 1, 1, 1],
            'full' : 3 in repetidos and 2 in repetidos,
            'poker' : 4 in repetidos or 5 in repetidos,
            'generala' : 5 in repetidos
        }
        
        return estado_jugadas[jugada.lower()]
    
    def calcular_puntos(self, numero_lanzamiento, que_jugada_elegir, estado_jugada):
        
        puntos_juegos = {
            '1' : 1, 
            '2' : 2, 
            '3' : 3, 
            '4' : 4, 
            '5' : 5, 
            '6' : 6,
            'escalera' : (20, 25),
            'full' : (30, 35),
            'poker' : (40, 45),
            'generala' : 50 
        }
        
        if type(puntos_juegos[que_jugada_elegir.lower()]) == tuple:  #si el dato almacenado en puntos_juegos es tupla (la jugada tiene puntuación distinta si es servida o no)
            punto_turno = puntos_juegos[que_jugada_elegir.lower()][1] if numero_lanzamiento == 1 else puntos_juegos[que_jugada_elegir.lower()][0]  #revisa el nro de turnos para determinar la puntuación
            puntaje = punto_turno * estado_jugada  #multiplica por la condición calculada en verificar_estado_juegos() (si no se cumple la condición, estado_jugada vale 0 y se anota 0)
        else:
            puntaje = puntos_juegos[que_jugada_elegir.lower()] * estado_jugada
        return puntaje

    def __str__(self):
        return ', '.join(str(x) for x in self.dados)

class Tabla():
    
    def __init__(self, jugadores, jugadas = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]):
        self.jugadores = jugadores
        self.jugadas = jugadas
    
    def verificar_jugada_no_realizada(self, jugada):
        return True if self.jugadas[jugada[0]][jugada[1]] == 'X' else False
    
    def anotar_jugada(self, jugador, valor, fila_jugada):
        self.jugadas[self.jugadores.index(jugador)][fila_jugada] = valor
    
    def juego_terminado(self):
        return True if 'X' not in self.jugadas[0] and 'X' not in self.jugadas[1] else False
    
    def determinar_ganador(self):  #devuelve una tupla indicando el nro del jugador ganador y el total de los puntos de ambos.
        if sum([x for x in self.jugadas[0] if type(x) == int]) == sum([x for x in self.jugadas[1] if type(x) == int]):
            return None, sum([x for x in self.jugadas[0] if type(x) == int])
        else:
            if sum([x for x in self.jugadas[0] if type(x) == int]) > sum([x for x in self.jugadas[1] if type(x) == int]):
                return 1, sum([x for x in self.jugadas[0] if type(x) == int]), sum([x for x in self.jugadas[1] if type(x) == int])  
            else:
                return 2, sum([x for x in self.jugadas[0] if type(x) == int]), sum([x for x in self.jugadas[1] if type(x) == int])
    
    def __str__(self):
        representacion = '''                              --------------------------------------------
                              |           |      J1      |       J2      |
                              |-----------|--------------|---------------|
                              |     1     |       (0,0)               (1,0)     
                              |-----------|--------------|---------------|
                              |     2     |       (0,1)               (1,1)     
                              |-----------|--------------|---------------|
                              |     3     |       (0,2)               (1,2)      
                              |-----------|--------------|---------------|
                              |     4     |       (0,3)               (1,3)      
                              |-----------|--------------|---------------|
                              |     5     |       (0,4)               (1,4)      
                              |-----------|--------------|---------------|
                              |     6     |       (0,5)               (1,5)      
                              |-----------|--------------|---------------|
                              | Escalera  |       (0,6)               (1,6)      
                              |-----------|--------------|---------------|
                              |   Full    |       (0,7)               (1,7)      
                              |-----------|--------------|---------------|
                              |   Poker   |       (0,8)               (1,8)      
                              |-----------|--------------|---------------|
                              |  Generala |       (0,9)               (1,9)      
                              |-----------|--------------|---------------|
                              |   TOTAL   |       SUMA               SUMB      
                              --------------------------------------------'''
        for i in range(2):
            for j in range(len(self.jugadas[i])):
                representacion = representacion.replace(('({0},{1})'.format(i,j)), str(self.jugadas[i][j]))
        numerosA, numerosB = [x for x in self.jugadas[0] if type(x) == int], [x for x in self.jugadas[1] if type(x) == int] 
        representacion = representacion.replace('SUMA', str(sum(numerosA)))
        representacion = representacion.replace('SUMB', str(sum(numerosB)))
        return representacion
    
if __name__ == '__main__':
    g = Generala()
    g.juego()