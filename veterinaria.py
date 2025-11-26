from conexion import Conexion

# Conexión global
conexion = Conexion()
cur, mydb = conexion.conectar()


class Veterinario:

    # === CREAR VETERINARIO ===
    def crear_veterinario(self):

        print("\n--- REGISTRAR VETERINARIO ---")

        rut = input("RUT del veterinario: ")
        nombre = input("Nombre completo: ")
        especialidad = input("Especialidad: ")

        # Validar años de experiencia
        while True:
            try:
                anios = int(input("Años de experiencia: "))
                break
            except ValueError:
                print(" Valor inválido. Debe ingresar un número entero.")

        contacto = input("Contacto (teléfono): ")

        sql = """
        INSERT INTO veterinario(rut, nombre, especialidad, anios_experiencia, contacto)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (rut, nombre, especialidad, anios, contacto)

        try:
            cur.execute(sql, valores)
            mydb.commit()
            print(" Veterinario registrado correctamente!\n")
        except Exception as e:
            print(" Error al registrar veterinario:", e)

    # === LISTAR VETERINARIOS ===
    def listar_veterinarios(self):

        print("\n--- LISTA DE VETERINARIOS ---")
        cur.execute("SELECT * FROM veterinario")
        vets = cur.fetchall()

        if not vets:
            print("⚠ No hay veterinarios registrados.\n")
            return

        for v in vets:
            print(f"""
RUT: {v[0]}
Nombre: {v[1]}
Especialidad: {v[2]}
Años de experiencia: {v[3]}
Contacto: {v[4]}
----------------------------------------
""")

    # === ACTUALIZAR CONTACTO ===
    def actualizar_veterinario(self):

        rut = input("Ingrese RUT del veterinario a actualizar: ")
        nuevo_contacto = input("Nuevo número de contacto: ")

        sql = "UPDATE veterinario SET contacto = %s WHERE rut = %s"

        try:
            cur.execute(sql, (nuevo_contacto, rut))
            mydb.commit()

            if cur.rowcount > 0:
                print(" Veterinario actualizado correctamente!\n")
            else:
                print(" No existe un veterinario con ese RUT.\n")

        except Exception as e:
            print(" Error al actualizar veterinario:", e)

    # === ELIMINAR VETERINARIO ===
    def eliminar_veterinario(self):

        rut = input("Ingrese RUT del veterinario a eliminar: ")

        sql = "DELETE FROM veterinario WHERE rut = %s"

        try:
            cur.execute(sql, (rut,))
            mydb.commit()

            if cur.rowcount > 0:
                print(" Veterinario eliminado correctamente!\n")
            else:
                print(" No existe un veterinario con ese RUT.\n")

        except Exception as e:
            print(" Error al eliminar veterinario:", e)

    # === MENÚ DEL MÓDULO ===
    def menu_veterinario(self):

        while True:
            print("""
--- MENÚ VETERINARIOS ---
1. Registrar veterinario
2. Listar veterinarios
3. Actualizar contacto
4. Eliminar veterinario
0. Salir
""")

            opc = input("Seleccione una opción: ")

            if opc == "1":
                self.crear_veterinario()
            elif opc == "2":
                self.listar_veterinarios()
            elif opc == "3":
                self.actualizar_veterinario()
            elif opc == "4":
                self.eliminar_veterinario()
            elif opc == "0":
                print("Saliendo del menú de veterinarios...\n")
                break
            else:
                print(" Opción inválida.\n")
