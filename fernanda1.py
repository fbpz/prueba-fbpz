import funciones as fn
pedidos=[]
while True:
    try:
        print("      menu pricipal      ")
        print("1. registrar pedido")
        print("2. listar todos los pedidos")
        print("3. imprimir hoja de ruta")
        print("4. salir del programa")
        opcion=int(input("seleccione opcion:"))
        if opcion==1:
            fn.registrar_pedidos(pedidos)
        elif opcion==2:
            fn.listar_pedido(pedidos)
        elif opcion==3:
            fn.imprimir_hoja(pedidos)
            
        elif opcion==4:
            print("saliendo...")
            break
        
    except:
        print("ingrese opcion valida")