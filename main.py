#imports
from datos import *
from menu import *
from services_admin import *
from users import*
from sales import*
from reportes import*

#Constants
RUTA_BASE_DE_DATOS_1 = "admin.json"
RUTA_BASE_DE_DATOS_2 = "services.json"

datos_1 = cargar_datos(RUTA_BASE_DE_DATOS_1)
datos_2 = cargar_datos(RUTA_BASE_DE_DATOS_2)

while True:
    menu_principal(datos_1,datos_2)
    
    guardar_datos(datos_1, RUTA_BASE_DE_DATOS_1)
    guardar_datos(datos_2, RUTA_BASE_DE_DATOS_2)
    break

