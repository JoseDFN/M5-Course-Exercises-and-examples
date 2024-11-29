from mascotas import Mascota, regMascotas

registro = regMascotas()

while True:
    menu = """--- Menu ---
    1. Agregar Mascota
    2. Listar Mascota
    3. Editar Mascota
    4. Eliminar Mascota
    5. Salir
    
    Ingrese una opcion: """

    option = int(input(menu))
    match option:
        case 1:
            nombre = input("Nombre de la mascota: ")
            especie = input("Especie de la mascota: ")
            edad = input("Edad de la mascota: ")

            mascota = Mascota(especie, edad, nombre)
            registro.agregar_mascota(mascota)
        case 2:
            registro.listar_mascotas()
        case 3:
            indice = int(input("Ingrese el indice del registro: "))
            nombre = input("Nombre de la mascota: ")
            especie = input("Especie de la mascota: ")
            edad = input("Edad de la mascota: ")

            nueva_mascota = Mascota(especie, edad, nombre)
            registro.editar_mascota(indice-1, nueva_mascota)

        case 4:
            indice = int(input("Ingrese el indice del registro: "))
            registro.eliminar_mascota(indice-1)

        case 5:
            print("Bye")
            break

        case _:
            print("Opcion no valida")