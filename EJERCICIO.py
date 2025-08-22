def revision():
    while True: 
        print("Nesesita que le colabore")
        rta = input("RESPONDA: SI o NO: ")
        
        while rta.strip().lower() not in ("si", "no"):
            print("solo, si o no??")
            rta = input("RESPONDA: SI o NO: ").strip().lower()

        if rta.strip().lower() == "si":
            print("Ok, cuéntame qué sucede con el vehiculo \n") 
            opciones = "1. El carro no arranca. 2. El carro arranca pero se apaga al acelerar. 3. El carro arranca pero el color del humo es... "
            print(opciones)
            respuesta = input("el vehiculo tene esto: ")

            if respuesta == "1":  
                print("Pero las luces del tablero están apagadas o prendidas?")
                luces_tablero = input("¿Apagadas o Prendidas? Responda. ").strip().lower()
                if luces_tablero == "prendidas":
                    print("\n lo que tiene es un fallo en el motor de arranque ")
                elif luces_tablero == "apagadas":
                    print("\n lo que tiene es pq tiene la batería descargada ")

            elif respuesta == "2":
                print("\n lo que tiene es pq tiene un problema en el suministro de combustible ")

            elif respuesta == "3":
                color_humo = input("¿Blanco o Negro? Responda. ").strip().lower()
                if color_humo == "negro":
                    print("\n  lo que tiene es una mezcla rica en combustible ")
                elif color_humo == "blanco":
                    print("\n lo tiene es una falla en la junta de culata ")

        elif rta.strip().lower() == "no":
            print("ADIOS")
            break 

        print("\n¿Necesita que revise algo más?")
        final = input("RESPONDA: SI o NO: ").strip().lower()
        if final == "no":
            print("ADIOS")
            break  

revision()

