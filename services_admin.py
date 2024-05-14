def create_service(datos_2):
    datos_2 = dict(datos_2)
    servicio={}
    servicio["name"]=input("Ingrese el nombre del servicio: ")
    servicio["description"]=input("Ingrese la descripción: ")
    try:
        servicio["cost"] = int(input("Ingrese el precio: "))
    except Exception:
        servicio["cost"] = 0
    try:
        servicio["lot"] = int(input("Ingrese la cantidad de unidades: "))
    except Exception:
        servicio["lot"] = 0
    
    while True:
        try:
            servicio["serial"] = int(input("Ingrese el serial: "))
            break
        except Exception:
            print("Alerta!")
            print("-Ingrese un serial válido sin números ni comas-")               
    datos_2["services"].append(servicio)
    print("El servicio se ha registrado con éxito!")
    return datos_2


def delete_service(datos_2):
    datos_2 = dict(datos_2)
    seriales=[]
    for i in (datos_2["services"]):
        seriales.append(i["serial"])
    print(seriales)
    
    d_serial =int(input("Ingrese el serial del servicio que desea eliminar: "))
    
    
    for i in datos_2["services"]:
        if d_serial == i["serial"]:
            
            datos_2["services"].remove(i)
            print("Servicio eliminado!")
            return datos_2
        
    if d_serial != i["serial"]:
        print("El servicio no existe o ya fue eliminado")


def update_service(datos_2):

    datos_2 = dict(datos_2)
    seriales =[]
    
    for i in (datos_2["services"]):
        seriales.append(i["serial"])
        
    print(seriales)
    
    contador_services = 0
    serial = int(input("Ingrese el serial del servicio que desea modificar = "))
    
    for i in (datos_2["services"]):
            if serial in seriales and serial == i["serial"]:
                contador_services += 1
                new_name =str(input("Actualizar el nombre. De lo contrario escriba -0- :"))
                if new_name == "0":
                         print(" ")
                else: i["name"]=new_name
                print("")
            
                new_description=str(input("Actualizar description. De lo contrario escriba -0- : "))
                if new_description == "0":
                        print(" ")
                else: i["description"]=new_description
                print("")
                

                try: 
                    new_cost=int(input("Actualizar tel precio. De lo contrario oprima enter :"))
                    if new_cost == "0":
                        print(" ")
                    else: i["cost"]=new_cost
                except:
                    print(" ")
            
                
                try: 
                    new_lot=int(input("Actualizar la cantidad. De lo contrario escriba -0- :"))
                    if new_lot == "0":
                        print(" ")
                    else: i["lot"]=new_lot
                except:
                    print(" ")
                    
                new_serial=int(input("Actualizar Serial. De lo contrario escriba -0- : "))
                if new_serial== "0":
                        print(" ")
                elif new_serial not in seriales:
                    i["serial"]=new_serial
                else: 
                    "Serial existente o inválido"
                print("")
                print("*******************************")
                print("Se han actualizado los datos del usuario correctamente!")
                return (datos_2)
    if contador_services == 0:
        print("Usuario no encontrado")

    
def menu_services(datos_1, datos_2):
    while True:
        
        print("-- -- -- --  --  --  --")
        print("1. Para crear servicio")
        print("2. Para modificar servicio")  
        print("3. Para eliminar servicio")
        print("4. Para volver al menú principal")
        
        
        try:
            opc = int(input("Ingrese su opción: "))
            if opc ==1:
                create_service(datos_2)       
            elif opc == 2:
                update_service(datos_2)
            elif opc == 3:
                update_service(datos_2)
            elif opc == 4:
                break
            else:
                print("Opción no existe")
                    
            print("***************************************")
            
        except Exception:
            print("Opción inválida")
            print("***************************************")
            menu_services(datos_1, datos_2)
    