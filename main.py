
users = []
uuid = 1
run_app = True

while run_app:
    print("\n===== REGISTRO DE USUARIOS =====")
    print("1. Registrar usuario(s)")
    print("2. Listar todos los usuarios")
    print("3. Editar usuario")
    print("4. Eliminar usuario")
    print("0. Salir...")
    user_option = int(input('\nElige la opción deseada: '))

    match user_option:
        case 1:
            records = int(input('Cuántos registros nuevos deseas crear? '))

            for i in range(records):
                print(f"\n===== Ingresa los datos del usuario {i + 1} =====")

                name = input('Ingresa nombre(s): ')
                while len(name) <= 5 or len(name) >= 50:
                    print('Por favor ingresa nombres válidos')
                    name = input('Ingresa nombre(s): ')

                surname = input('Ingresa apellidos: ')
                while len(surname) <= 5 or len(surname) >= 50:
                    print('Por favor ingresa apellidos válidos')
                    surname = input('Ingresa apellidos: ')

                phone = input('Ingresa número de teléfono: ')
                while len(phone) != 10:
                    print('El teléfono debe contener 10 dígitos')
                    phone = input('Ingresa número de teléfono: ')

                email = input('Ingresa Email: ')
                while len(email) <= 5 or len(email) >= 50:
                    print('Por favor ingresa un email válido')
                    email = input('Ingresa email: ')

                user = {
                    "user_id": uuid,
                    "name": name,
                    "surname": surname,
                    "phone": phone,
                    "email": email,
                }
                users.append(user)
                uuid += 1

                print(f'Hola {user["name"]} {user["surname"]} en breve recibirás un correo a {user["email"]}')

        case 2:
            print("===== Lista de usuarios =====")
            print("ID\tNombre")

            for user in users:
                print(f"{user["user_id"]}\t{user["name"]} {user["surname"]}")

            _ = input("Presiona cualquier tecla para regresar al menú...")

        case 3:
            print("===== Editar usuario =====")
            user_to_edit = int(input("Ingresa el ID del usuario a editar: "))

            for index, user in enumerate(users):
                if user_to_edit == user["user_id"]:
                    print(f"\n===== Ingresa los datos del usuario con ID {user_to_edit} =====")

                    user["name"] = input('Ingresa nombre(s): ')
                    while len(user["name"]) <= 5 or len(user["name"]) >= 50:
                        print('Por favor ingresa nombres válidos')
                        user["name"] = input('Ingresa nombre(s): ')

                    user["surname"] = input('Ingresa apellidos: ')
                    while len(user["surname"]) <= 5 or len(user["surname"]) >= 50:
                        print('Por favor ingresa apellidos válidos')
                        user["surname"] = input('Ingresa apellidos: ')

                    user["phone"] = input('Ingresa número de teléfono: ')
                    while len(user["phone"]) != 10:
                        print('El teléfono debe contener 10 dígitos')
                        user["phone"] = input('Ingresa número de teléfono: ')

                    user["email"] = input('Ingresa Email: ')
                    while len(user["email"]) <= 5 or len(user["email"]) >= 50:
                        print('Por favor ingresa un email válido')
                        user["email"] = input('Ingresa email: ')

                    print("Usuario editado correctamente")

            _ = input("Presiona cualquier tecla para regresar al menú...")

        case 4:
            print("===== Eliminar usuario =====")
            user_to_delete = int(input("Ingresa el ID del usuario a eliminar: "))

            for index, user in enumerate(users):
                if user_to_delete == user["user_id"]:
                    del users[index]

            _ = input("Presiona cualquier tecla para regresar al menú...")

        case 0:
            print("===== Hasta luego =====")
            run_app = False
