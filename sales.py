def sales(datos_2,datos_1):
    datos_1=dict(datos_1)
    datos_2=dict(datos_2)
    
    user_id = []
    for i in (datos_1["usuarios"]):
        user_id.append(i["id"])
    print("Usuarios registrados: ")
    print(user_id)
    
    print("--------------------")
    print("1. para vender un servicio")
    print("2. para vender un producto")
    opc = int(input(":"))
    catalogo_ser = []
    catalogo_pro = []
    if opc == 1:
        print("Catálogo de servicios disponibles: ")
        for i in (datos_2["services"]):
            catalogo_ser.append(i["name"])
            catalogo_ser.append(i["serial"])
        print(catalogo_ser)
        print("----------------------")
        
        ser_ser = int(input("Ingrese el serial del servicio a vender: "))
        id_user = int(input("Ingrese el id del usuario quien recibira el servicio: "))
        
        if ser_ser in catalogo_ser and id_user in user_id:
            for i in (datos_2["services"]):
                if ser_ser == i["serial"]:
                    i["lot"] -= 1
                    i["sold"]+=1
            for j in (datos_1["usuarios"]):
                if id_user == j["id"]:
                     j["ad_services"] += 1
            print("---   ----   ----")         
            print("Servicio vendido con exito")
        else:
            print("---   ----   ----")  
            print("Usuario o servicio no válido")
            print("---   ----   ----")  
            sales(datos_2,datos_1)
    elif opc == 2:
        print("Catálogo de productos disponibles: ")
        for i in (datos_2["products"]):
            catalogo_pro.append(i["name"])
            catalogo_pro.append(i["serial"])
        print(catalogo_pro)
        print("----------------------")
        
        ser_ser1 = int(input("Ingrese el serial del producto a vender: "))
        id_user1 = int(input("Ingrese el id del usuario quien recibira el producto: "))
        
        if ser_ser1 in catalogo_pro and id_user1 in user_id:
            for i in (datos_2["products"]):
                if ser_ser1 == i["serial"]:
                    i["lot"] -= 1
                    i["sold"]+=1
            for j in (datos_1["usuarios"]):
                if id_user1 == j["id"]:
                     j["ad_products"] += 1
            print("---   ----   ----")         
            print("Servicio vendido con exito")
            return datos_1,datos_2
        else:
            print("---   ----   ----")  
            print("Usuario o servicio no válido")
            print("---   ----   ----")  
            sales(datos_2,datos_1)
        return datos_1,datos_2
        
 
def promo_sales(datos_1,datos_2):
    datos_1=dict(datos_1)
    datos_2=dict(datos_2)
    user_id = []
    print("-----------------------")
    for i in (datos_1["usuarios"]):
        user_id.append(i["id"])
    print("Usuarios registrados: ")
    print(user_id)
    
    user_promo= int(input("Ingrese el id del usuario para revisar que ofertas tiene disponibles: "))
    if user_promo in user_id:
        for i in (datos_1["usuarios"]):
            if user_promo == i["id"] and i["category"] == "nuevo":
                 print("El usuario se encuentra en la categoría: " + i["category"])
                 print("Por lo tanto tendrá un descuento del 10 % en cualquier producto o servicio")
                 print("----------------------")
            elif user_promo == i["id"] and i["category"] == "regular":
                print("El usuario se encuentra en la categoría: " + i["category"])
                print("Por lo tanto tendrá un descuento del 20 % en cualquier producto o servicio")
                print("----------------------")
            elif user_promo == i["id"] and i["category"] == "leal":
                print("El usuario se encuentra en la categoría: " + i["category"])
                print("Por lo tanto tendrá un descuento del 40 % en cualquier producto o servicio")
                print("----------------------")
                
                
    return(datos_1)


def menu_sales(datos_1,datos_2):
    datos_1=dict(datos_1)
    datos_2=dict(datos_2)
    while True:
        print("---------------------")
        print("1. Para vender productos y servicios")
        print("2. Para verifcar a que usuarios se le puede aplicar descuentos")
        print("3. Para regresar al menú principal")      
        print("---------------------")  

        try:
            opc = int(input("Ingrese la opción: "))
            if opc == 1:
                sales(datos_2,datos_1)
            elif opc ==2:
                promo_sales(datos_1,datos_2)
            elif opc ==3:
                    break
                
            else:
                print("Opción no existe.")
                menu_sales(datos_1,datos_2)          
        except Exception:
            print("Vuelva a ingresar la opción")
            menu_sales(datos_1,datos_2)
                 
                 
    
    
    