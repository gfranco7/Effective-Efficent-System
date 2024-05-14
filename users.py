


def create_user(datos_1,datos_2):
    datos_1 = dict(datos_1)
    user={}
    user["name"]=input("Ingrese el nombre del Usuario: ")
    user["diretion"]=input("Ingrese la dirección : ")
    
    try:
        user["phone"]=int(input("Ingrese su número : "))
    except Exception:
        user["phone"] = 0
        print("Número inválido. Para modificarlo ingrese en la opción -actualizar perfil de usuarios- ")
   
    try:
        documento= int(input("Ingrese su documento : "))
        user["id"]=documento
    except Exception:
        user["id"] = 0
        print("Documento inválido. Para modificarlo ingrese en la opción -actualizar perfil de usuarios-")


    user["email"]=input("Ingrese el email del Usuario: ")
    
    print("1. Nuevo")
    print("2. Regular")
    print("3. Leal")         
    try:
                category_user = int(input("Ingrese la categoría del usuario= "))
                if category_user == 1:
                     user["category"]="nuevo"
                     user["ad_products"] = 0 
                     user["ad_services"]= 0
                     
                elif category_user == 2:
                    user["category"]="regular"
                    try:
                        user["ad_products"]=int(input("Ingrese la cantidad de productos adquiridos por el usuario : "))
                        user["ad_services"]=int(input("Ingrese la cantidad de servicios adquiridos por el usuario : "))
                    except Exception:
                        user["phone"] = 0
                        print("Valor inválido. Para modificarlo ingrese en la opción -actualizar perfil de usuarios- ")
                elif category_user == 3:
                    user["category"]="leal"
                    try:
                        user["ad_products"]=int(input("Ingrese la cantidad de productos adquiridos por el usuario : "))
                        user["ad_services"]=int(input("Ingrese la cantidad de servicios adquiridos por el usuario : "))
                    except Exception:
                        user["phone"] = 0
                        print("Valor inválido. Para modificarlo ingrese en la opción -actualizar perfil de usuarios- ")
                else:
                    print("Opción no existe. Se guardará como nuevo.")
                    user["category"]="Nuevo"
                
    except Exception:
                print("Error")
    
    
    datos_1["usuarios"].append(user)
    print("-------------------------------------")
    print("El registro se ha completado con éxito")
    print("-------------------------------------")
    menu_users(datos_1, datos_2)
    return datos_1
    


def update_user(datos_1,datos_2):

    datos_1 = dict(datos_1)
    nombres=[]
    
    for i in (datos_1["usuarios"]):
        nombres.append(i["id"])
        
    print(nombres)
    
    contador_users = 0
    user_id = int(input("Ingrese el Id que desea modificar = "))
    
    for i in (datos_1["usuarios"]):
            if user_id in nombres and user_id == i["id"]:
                contador_users += 1
                new_name =str(input("Actualizar el nombre. De lo contrario escriba -0- :"))
                if new_name == "0":
                         print(" ")
                else: i["name"]=new_name
            
                new_direction=str(input("Actualizar dirección. De lo contrario escriba -0- : "))
                if new_direction == "0":
                        print(" ")
                else: i["direction"]=new_direction

                new_phone=input("Actualizar teléfono. De lo contrario escriba -0- :")
                if new_phone== "0":
                        print(" ")
                else: i["phone"]=new_phone

                new_id=int(input("Actualizar Documento. De lo contrario escriba -0- : "))
                if new_id== 0:
                        print(" ")
                else: i["id"]=new_id

                new_email=input("Actualizar email. De lo contrario escriba -0- : ")
                if new_email== "0":
                        print(" ")
                else: i["email"]=new_email

                new_category=input("Actualizar categoría. De lo contrario escriba -0- : ")
                if new_category== "0":
                        print(" ")
                else: i["category"]=new_category
                
                new_product=input("Actualizar cantidad de productos adquiridos. De lo contrario escriba -0- : ")
                if new_product==0:
                    print(" ")
                else: i["ad_products"]=new_product
                
                new_service=input("Actualizar cantidad de servicios adquiridos. De lo contrario escriba -0- : ")
                if new_service==0:
                    print(" ")
                else: i["ad_services"]=new_service
                
                print("*******************************")
                print("Se han actualizado los datos del usuario correctamente!")
                return (datos_1)
    if contador_users == 0:
        print("Usuario no encontrado")         
    menu_users(datos_1, datos_2)


def delete_user(datos_1, datos_2):
    datos_1 = dict(datos_1)
    nombres=[]
    for i in (datos_1["usuarios"]):
        nombres.append(i["id"])
    print(nombres)
    

    user_id =int(input("Ingrese el documento del usuario que desea eliminar: "))
    contador_user = 0
    for i in datos_1["usuarios"]:
        
        if user_id == i["id"]:
            contador_user +=1
            datos_1["usuarios"].remove(i)
            print("Usurio eliminado!")
            return datos_1
    if contador_user == 0:
        print("El usuario no existe o ya fue eliminado")    
    menu_users(datos_1, datos_2)
    

def user_list(datos_1):
    datos_1 = dict(datos_1)
    print("A continuación se mostrarán los perfiles de usuarios disponibles:")
    print("**** ***********    ******** *********")
    for i in (datos_1["usuarios"]):
        
        print(i)
    print("*****************************")
    return None
    


def menu_users(datos_1, datos_2, menu_principal):
    
    while True:
        
        print("-- -- -- --  --  --  --")
        print("1. Para crear perfil de usuario")
        print("2. Para modificar perfil de usuario")  
        print("3. Para eliminar perfil de usuario")
        print("4. Para ver perfil de usuario")
        print("5. Para volver al menú principal")
        
        try:
            opc = int(input("Ingrese su opción: "))
            if opc ==1:
                create_user(datos_1,datos_2)       
            elif opc == 2:
                update_user(datos_1,datos_2)
            elif opc == 3:
                delete_user(datos_1,datos_2)
            elif opc == 4:
                user_list(datos_1)  
            elif opc == 5:
                
                break  
            else:
                print("Opción no existe")
                    
            print("***************************************")

        except Exception:
            print("Opción inválida")
            print("***************************************")
            menu_users(datos_1, datos_2, menu_principal)
            
      





     

     
    
