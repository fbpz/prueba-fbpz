sectores=["norte","centro","sur"]
def registrar_pedidos(pedidos):
    try:
        nombre=input("ingrese nombre y apellido: ")
        direccion=input("ingrese direccion: ")
        sector=input("ingrese su sector: ").lower()
        while sector not in sectores:
            print("ingrese sector valido")
       
        mediano=int(input("ingrese cantidad de paquetes medianos: "))
        grandes=int(input("ingrese grandes: "))
        pequenos=int(input("ingrese cantidad de paquetes pequeños: "))
         
    except:
        print("ingrese opcion valida")
        
            

    pedidos.append({
        "nombre":nombre,
        "direccion":direccion,
        "sector":sector,
        "mediano":mediano,
        "grandes":grandes,
        "pequeños":pequenos,
    })

    print("registro creado")
    
def listar_pedido(pedidos):
    for pedido in pedidos:
        print(pedido)
        return

def imprimir_hoja(pedidos):
    sector_a_imprimir=input("ingrese el sector para imprimir la planilla")
    if sector_a_imprimir=="":
       lista_paquetes=pedidos
       nombre_archivo="planilla_todos.txt"
    elif sector_a_imprimir in sectores:
        lista_paquetes=[]
        for paquete in pedidos: 
            if paquete["sector"]== sector_a_imprimir:
                lista_paquetes.append(paquete)
        nombre_archivo=f"planilla_{sector_a_imprimir}.txt"
    else:
        print("ingrese sector valido")

    with open(f"{nombre_archivo}","w") as archivo:
        for pedido in lista_paquetes:
            archivo.write(f"nombre y apellido: {pedido["nombre"]}\n"),
            archivo.write(f"direccìon: {pedido["direccion"]}\n"),
            archivo.write(f"Sector: {pedido["sector"]}\n"),
            archivo.write(f":Mediano {pedido["mediano"]}\n"),
            archivo.write(f"Grandes: {pedido["grandes"]}\n"),
            archivo.write(f"pequeños: {pedido["pequeno"]}\n"),

            