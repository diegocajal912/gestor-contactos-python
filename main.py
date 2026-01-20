from db_connection import get_connection

def agregar_contacto():
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO contactos (nombre, email, telefono)
            VALUES (?, ?, ?)
            """,
            (nombre, email, telefono)
        )

        conn.commit()
        conn.close()
        print("Contacto agregado correctamente")

    except Exception as e:
        print("Error al agregar contacto:", e)



def ver_contactos():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nombre, email, telefono FROM contactos")
        contactos = cursor.fetchall()

        if not contactos:
            print("No hay contactos cargados.")
        else:
            print("\n--- LISTA DE CONTACTOS ---")
            for contacto in contactos:
                print(f"ID: {contacto.id}")
                print(f"Nombre: {contacto.nombre}")
                print(f"Email: {contacto.email}")
                print(f"Teléfono: {contacto.telefono}")
                print("--------------------------")

        conn.close()

    except Exception as e:
        print("Error al mostrar contactos:", e)



def eliminar_contacto():
    try:
        id_contacto = input("Ingresá el ID del contacto a eliminar: ")

        conn = get_connection()
        cursor = conn.cursor()

        # 1. Verificar si el contacto existe
        cursor.execute(
            "SELECT COUNT(*) FROM contactos WHERE id = ?",
            (id_contacto,)
        )
        existe = cursor.fetchone()[0]

        if existe == 0:
            print("No existe un contacto con ese ID.")
        else:
            # 2. Eliminar el contacto
            cursor.execute(
                "DELETE FROM contactos WHERE id = ?",
                (id_contacto,)
            )
            conn.commit()
            print("Contacto eliminado correctamente.")

        conn.close()

    except Exception as e:
        print("Error al eliminar contacto:", e)



def mostrar_menu():
    print("\n--- GESTOR DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Salir")

    

while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")