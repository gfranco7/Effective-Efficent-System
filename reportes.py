def reportes(datos_1, datos_2):
    datos_1=dict(datos_1)
    datos_2=dict(datos_2)
    while True:

        print("---------------------")
        print("1. Para mostrar informe de productos y servicios")
        print("2. Para mostrar informe de ventas")
        print("3. Para mostrar informe de usuarios en ventas")
        print("4. Para regresar al menú principal")
        
        try:
            opc = int(input("Ingrese la opción: "))
            if opc == 1:
                info_proser(datos_1,datos_2)
            elif opc ==2:
                info_ventas(datos_1,datos_2)
            elif opc ==3:
                info_users(datos_1, datos_2)
            elif opc == 4:
                    break
                
            else:
                print("Opción no existe.")
                reportes(datos_1, datos_2)          
        except Exception:
            print("Vuelva a ingresar la opción")
            reportes(datos_1, datos_2)



def info_proser(datos_1,datos_2):
    print("--  --  --  --  --  --")
    for i in datos_2["services"]:
        print("Para servicio: "+i["name"])
        print(f"Se cuenta con ",{i["lot"]}," unidades")
    print("-- -- -- -- -- -- ")
    for i in datos_2["products"]:
        print("Para el producto: "+i["name"])
        print(f"Se cuenta con ",{i["lot"]}," unidades")   
    print("-- -- -- -- -- -- ") 
    reportes(datos_1, datos_2)
    return(datos_2)
    

def info_ventas(datos_1,datos_2):
    datos_2=dict(datos_2)
    total_sold_ser=[]
    total_sold_pro=[]
    
    for i in datos_2["services"]:
        total_sold_ser.append(i["sold"])
    major_sold=max(total_sold_ser)
    for i in datos_2["services"]:
        if major_sold == i["sold"]:
            print(f"El servicio de mas alta demanda es: ",{i["name"]})
            
    for j in datos_2["products"]:
        total_sold_pro.append(j["sold"])
    major_sold=max(total_sold_pro)
    for j in datos_2["products"]:
        if major_sold == j["sold"]:
            print(f"El producto de mas alta demanda es: ",{j["name"]})
    
    reportes(datos_1, datos_2)
    return datos_2


def info_users(datos_1, datos_2):
    datos_1 = dict(datos_1)
    
    for i in datos_1["usuarios"]:
        print(i["name"])
        print(f"El usuario ha adquirido",{i["ad_services"]}, "serivios")
        print(f"El usuario ha adquirido",{i["ad_products"]}, "productos")
    reportes(datos_1, datos_2)
    return datos_1
        
        
     
    
    
    
    
        
    
       

