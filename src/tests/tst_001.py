import unittest
from functions.Functions import Functions as Selenium
import allure
@allure.feature(u'Test Udemy 1')
@allure.story(u'001: verificar query result')
@allure.testcase(u'Caso de Prueba 0001', u'http://my.tas.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u'The PO givens')



class test1024(Selenium,unittest.TestCase):
    def setUp(self):
        with allure.step(u'Paso 1: Ingresar a gogle'):
            Selenium.abrir_navegador(self)

    def test_01(self):
        with allure.step(u'Paso 2: Ingresar a gogle'):
            pass

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
