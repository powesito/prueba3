from conexion import Conexion

# Crear conexión global
conexion = Conexion()
cur, mydb = conexion.conectar()


class Cuidador:

    # === CREAR CUIDADOR ===
    def crear_cuidador(self):
        print("\n--- REGISTRAR CUIDADOR ---")

        rut = input("Ingrese RUT del cuidador: ")
        nombre = input("Ingrese nombre del cuidador: ")
        telefono = input("Ingrese teléfono del cuidador: ")
        correo = input("Ingrese correo del cuidador: ")

        sql = """
            INSERT INTO cuidador(rut, nombre, telefono, correo)
            VALUES (%s, %s, %s, %s)
        """

        valores = (rut, nombre, telefono, correo)

        try:
            cur.execute(sql, valores)
            mydb.commit()
            print(" Cuidador registrado correctamente!\n")
        except Exception as e:
            print(" Error al registrar cuidador:", e)

    # === LISTAR CUIDADORES ===
    def listar_cuidadores(self):
        print("\n--- LISTA DE CUIDADORES ---")

        try:
            cur.execute("SELECT * FROM cuidador")
            cuidadores = cur.fetchall()

            if len(cuidadores) == 0:
                print("No hay cuidadores registrados.\n")
                return

            for c in cuidadores:
                print(c)

            print()

        except Exception as e:
            print(" Error al listar cuidadores:", e)

    # === ACTUALIZAR CUIDADOR ===
    def actualizar_cuidador(self):
        print("\n--- ACTUALIZAR CUIDADOR ---")

        rut = input("Ingrese RUT del cuidador a actualizar: ")
        nuevo_nombre = input("Nuevo nombre: ")

        sql = "UPDATE cuidador SET nombre = %s WHERE rut = %s"
        valores = (nuevo_nombre, rut)

        try:
            cur.execute(sql, valores)
            mydb.commit()

            if cur.rowcount > 0:
                print(" Cuidador actualizado correctamente!\n")
            else:
                print(" No existe un cuidador con ese RUT.\n")

        except Exception as e:
            print(" Error al actualizar cuidador:", e)

    # === ELIMINAR CUIDADOR ===
    def eliminar_cuidador(self):
        print("\n--- ELIMINAR CUIDADOR ---")

        rut = input("Ingrese RUT del cuidador a eliminar: ")

        sql = "DELETE FROM cuidador WHERE rut = %s"

        try:
            cur.execute(sql, (rut,))
            mydb.commit()

            if cur.rowcount > 0:
                print(" Cuidador eliminado correctamente!\n")
            else:
                print(" No existe un cuidador con ese RUT.\n")

        except Exception as e:
            print(" Error al eliminar cuidador:", e)

    # === MENÚ CUIDADOR ===
    def menu_cuidador(self):

        while True:
            print("""
--- MENÚ CUIDADORES ---
1. Agregar cuidador
2. Listar cuidadores
3. Actualizar cuidador
4. Eliminar cuidador
0. Salir
""")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_cuidador()
            elif opcion == "2":
                self.listar_cuidadores()
            elif opcion == "3":
                self.actualizar_cuidador()
            elif opcion == "4":
                self.eliminar_cuidador()
            elif opcion == "0":
                print("Saliendo del menú...")
                break
            else:
                print(" Opción inválida.\n")
