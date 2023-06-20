from functions.Functions import Functions as Selenium
import time
import allure
class index:
    #abrir el json
    def iniciar(self):
        #Variables localizador
        Nombre = "Data"
        #Variables de Datos

        Correo = Selenium.leer_celda(self,"A1",Nombre)
        NombreCompleto = Selenium.leer_celda(self,"B1",Nombre)
        MensajeIndex = Selenium.leer_celda(self, "C1",Nombre)
        print(Correo)
        print(NombreCompleto)
        print(MensajeIndex)

        # time.sleep(10)
        Selenium.get_json_file(self, "Index")
        Selenium.esperar_elemento(self, "Logo")
        print("sadasd")

        Selenium.get_elements(self,"Home").click()
        Selenium.esperar_elemento(self,"Logo")
        print("Se dio clic al home")

        Selenium.get_elements(self, "Contact").click()
        print("sadasd2")


        Selenium.get_elements(self,"CorreoElectronico").send_keys(Correo)
        time.sleep(5)
        Selenium.get_elements(self,"TextBoxNombre").send_keys(NombreCompleto)
        print("sadasd4")
        time.sleep(5)
        Selenium.get_elements(self,"Mensaje").send_keys(MensajeIndex)
        Selenium.capturar_pantalla(self)
        time.sleep(10)

        Selenium.get_elements(self,"EnviarMensaje").click()
        Selenium.alert_windows(self)
        time.sleep(10)
        print("asdsad6")







