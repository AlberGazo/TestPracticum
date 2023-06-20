import os
import time
class Inicializar():
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    #JsonData
    Json = basedir + u'\data'
    JsonResponseData = basedir + u'\data\json'

    NAVEGADOR = u'CHROME'
    #Evidencias
    Path_Evidencias = basedir + u'\data\capturas'

    #Hoja de Datos
    Excel = basedir + u'\data'

    Environment = 'Form'

    if Environment == 'Dev':
        URL = 'https://www.demoblaze.com/'
        User = 'mdiaz'
        Pass = 'Mm121666'
        DB_HOST = 'localhost'
        DB_PORT = '5432'
        DB_DATABASE = 'curso_api'
        DB_USER = 'postgres'
        DB_PASS = 'postgres'

    if Environment == 'Form':
        URL = 'https://demoqa.com/automation-practice-form'
        User = 'mdiaz'
        Pass = 'Mm121666'
        DB_HOST = 'localhost'
        DB_PORT = '5432'
        DB_DATABASE = 'curso_api'
        DB_USER = 'postgres'
        DB_PASS = 'postgres'


    if Environment == 'Test':
        URL = 'https://demoqa.com/webtables'
        User = 'mdiaz'
        Pass = 'Mm121666'
