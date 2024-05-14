
from sales import*
from services_admin import *
from users import*
from reportes import*
from datetime import datetime
def exc_fecha(message):
    date_today = datetime.now()
    date_today = datetime.strftime(date_today,"%d-%m-%Y - %H:%M:%S")
    file = open("excepciones.txt","a")
    file.write(date_today + "  "+ message+"\n")
    file.close


def ingreso_menu():
    print("****************************************")
    print("Bienvenid@ a CLARO Efficient Effective System (EES)!")
    user = str(input("Ingrese su usuario == "))
    usercode = input("Ingrese su contraseña == ")
    user1 = "adminboss"
    usercode1 = "admin007"
    
    if user == user1 and usercode == usercode1:    
        ingreso = "Ingreso exitoso!" 
        print("******************************************")
        print(ingreso)
        print("******************************************")   
            
             
    else: print("Usuario o contraseña incorrectos. Vuelva a intentarlo")


    
def menu_principal(datos_1,datos_2):
    while True:
        print("----    ----    ----    ----    ----    ----")
        print("1. Para crear, modificar, ver o eliminar perfil de usuarios")
        print("2. Para crear, modificar, ver o eliminar servicios")
        print("3. Para verificar reportes de servicios, productos, ventas o usuarios")
        print("4. Para realizar ventas")
        print("5. Para finalizar el programa")
        print("----    ----    ----    ----    ----    ----")
        try:
            opc = int(input("Ingrese su opción: "))
            if opc ==1:
                menu_users(datos_1,datos_2,menu_principal)
            elif opc == 2:
                menu_services(datos_1, datos_2)
            elif opc == 3:
                reportes(datos_1, datos_2)
            elif opc == 4:
                menu_sales(datos_1,datos_2)
            elif opc == 5:
                print("---   ---   ---   ---   ---")
                print("Seción finalizada! Siempre puedes contar con -EES- para gestionar tu empresa!-")
                print("---   ---   ---   ---   ---")
                break
            else:
                print("Opción inválida")
                menu_principal(datos_1,datos_2)

    
            print("***************************************")
            
        except Exception:
            print("Opción inválida")
            print("***************************************")
            exc_fecha("En menu principal se ingreso un valor no numerico")
        



    