import unittest
import P1, P2, P3, P4, P5, P6, P7, P8

# corre este para probar el examen entero
if __name__ == '__main__':
    unittest.main()


class P1Test(unittest.TestCase):
    def test_int(self):
        termino = (8, 3)
        resultado = (2, 4)
        self.assertEqual(resultado, P1.integra_termino(termino))

    def test_int2d(self):
        termino = (8, 4)
        resultado = (1.6, 5)
        self.assertEqual(resultado, P1.integra_termino(termino))

    def test_double(self):
        termino = (8.8, 3)
        resultado = (2.2, 4)
        self.assertEqual(resultado, P1.integra_termino(termino))


class P2Test(unittest.TestCase):
    def test_empty(self):
        polinomio = []
        resultado = []
        self.assertEqual(resultado, P2.integra_polinomio(polinomio))

    def test_a(self):
        polinomio = [(1, 1), (8, 4), (8.8, 3)]
        resultado = [(0.5, 2), (1.6, 5), (2.2, 4)]
        self.assertEqual(resultado, P2.integra_polinomio(polinomio))


class P3Test(unittest.TestCase):
    def test_a(self):
        polinomio = [(2, 2), (8, 4), (8.8, 3)]
        resultado = "2x2+8x4+8.8x3"
        self.assertEqual(resultado, P3.conv_str(polinomio).replace(" ", ""))

    def test_b(self):
        polinomio = [(3, 3)]
        resultado = "3x3"
        self.assertEqual(resultado, P3.conv_str(polinomio).replace(" ", ""))


class P4Test(unittest.TestCase):
    def test_1t(self):
        x = 2
        polinomio = [(3, 3)]
        resultado = 24
        self.assertEqual(resultado, P4.evalua_pol(polinomio, x))

    def test_2t(self):
        x = 2
        polinomio = [(3, 3), (5, 2)]
        resultado = 44
        self.assertEqual(resultado, P4.evalua_pol(polinomio, x))

    def test_coefneg(self):
        x = 1
        polinomio = [(3, 3), (5, 2), (-2, 1)]
        resultado = 6
        self.assertEqual(resultado, P4.evalua_pol(polinomio, x))

    def test_vacio(self):
        x = 4
        polinomio = []
        resultado = 0
        self.assertEqual(resultado, P4.evalua_pol(polinomio, x))


class P5Test(unittest.TestCase):
    def test_decimales(self):
        lista = [727.7, 1086.5, 1091.0, 1361.3, 1490.5, 1956.1]
        resultado = 420.96
        decimales_a_comparar = 2
        self.assertAlmostEqual(resultado, P5.desv_std(lista), decimales_a_comparar)

    def test_desviacioncero(self):
        lista = [5, 5, 5]
        resultado = 0
        self.assertEqual(resultado, P5.desv_std(lista))

    def test_desviacionint(self):
        lista = [4, 5, 6]
        resultado = 1.0
        self.assertEqual(resultado, P5.desv_std(lista))


class P6Test(unittest.TestCase):
    def test_mix(self):
        lista = [4, 5, 6]
        resultado = 10
        self.assertEqual(resultado, P6.suma_pares(lista))

    def test_solopares(self):
        lista = [4, 8, 6]
        resultado = 18
        self.assertEqual(resultado, P6.suma_pares(lista))

    def test_soloimpares(self):
        lista = [1, 5, 7]
        resultado = 0
        self.assertEqual(resultado, P6.suma_pares(lista))

    def test_vacio(self):
        lista = []
        resultado = 0
        self.assertEqual(resultado, P6.suma_pares(lista))


class P7Test(unittest.TestCase):
    
    def test_vacio(self):
        entrada = []
        salida = {}
        self.assertEqual(salida, P7.cuenta_palabras(entrada))
        
    def test_norep(self):
        entrada = ["hola", "bien"]
        salida = {"hola": 1, "bien": 1}
        self.assertEqual(salida, P7.cuenta_palabras(entrada))
    
    def test_minusc(self):
        entrada = ["hola", "hola", "bien"]
        salida = {"hola": 2, "bien": 1}
        self.assertEqual(salida, P7.cuenta_palabras(entrada))
    
    def test_mayusc(self):
        entrada = ["HOLA", "HOLA", "BIEN"]
        salida = {"hola": 2, "bien": 1}
        self.assertEqual(salida, P7.cuenta_palabras(entrada))
    
    def test_mix(self):
        entrada = ["hola", "HoLa", "BYE"]
        salida = {"hola": 2, "bye": 1}
        self.assertEqual(salida, P7.cuenta_palabras(entrada))
    
    def test_mix2(self):
        entrada = ["come", "HoLa", "come", "bien", "bien", "bien"]
        salida = {"hola": 1, "come": 2, "bien": 3}
        self.assertEqual(salida, P7.cuenta_palabras(entrada))


class P8Test(unittest.TestCase):
    def test_inicio(self):
        entrada = '"hola" es una palabra, "vas bien" es otra palabra'
        resultado= ["hola", "vas bien"]
        self.assertEqual(resultado, P8.extrae_comillas(entrada))

    def test_b(self):
        entrada = 'Inicio "hola" es una palabra, "vas bien" es otra palabra'
        resultado= ["hola", "vas bien"]
        self.assertEqual(resultado, P8.extrae_comillas(entrada))

    def test_vacio(self):
        entrada = 'Inicio hola es una palabra, vas bien es otra palabra'
        resultado= []
        self.assertEqual(resultado, P8.extrae_comillas(entrada))

    def test_invalid(self):
        entrada = 'Inicio "hola es una palabra, "vas bien" es otra palabra'
        resultado = None
        self.assertEqual(resultado, P8.extrae_comillas(entrada))

    def test_final(self):
        entrada = 'Inicio "hola" es una palabra, "vas bien"'
        resultado= ["hola", "vas bien"]
        self.assertEqual(resultado, P8.extrae_comillas(entrada))

    def test_consecutivo(self):
        entrada = 'Inicio "hola""vas bien"'
        resultado= ["hola", "vas bien"]
        self.assertEqual(resultado, P8.extrae_comillas(entrada))

    def test_otro(self):
        entrada = 'Inicio "este" y  "aquel" ademas "ese" y "asi"'
        resultado= ["este", "aquel", "ese", "asi"]
        self.assertEqual(resultado, P8.extrae_comillas(entrada))
