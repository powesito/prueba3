from conexion import Conexion

# Crear conexión global
conexion = Conexion()
cur, mydb = conexion.conectar()


class FichaClinica:

    # === CREAR FICHA ===
    def crear_ficha(self):

        print("\n--- CREAR FICHA CLÍNICA ---")

        id_mascota = input("ID Mascota: ")
        rut_cuidador = input("RUT Cuidador: ")
        rut_veterinario = input("RUT Veterinario: ")
        id_procedimiento = input("ID Procedimiento: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        notas = input("Notas: ")

        sql = """
            INSERT INTO ficha_clinica(id_mascota, rut_cuidador, rut_veterinario, id_procedimiento, fecha, notas)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (id_mascota, rut_cuidador, rut_veterinario, id_procedimiento, fecha, notas)

        try:
            cur.execute(sql, valores)
            mydb.commit()
            print(" Ficha clínica registrada correctamente!\n")
        except Exception as e:
            print(" Error al crear ficha clínica:", e)

    # === LISTAR FICHAS ===
    def listar_fichas(self):

        print("\n--- LISTA DE FICHAS CLÍNICAS ---")

        try:
            cur.execute("SELECT * FROM ficha_clinica")
            fichas = cur.fetchall()

            if len(fichas) == 0:
                print("No hay fichas clínicas registradas.\n")
                return

            for f in fichas:
                print(f)

            print()

        except Exception as e:
            print(" Error al listar fichas:", e)

    # === ACTUALIZAR FICHA ===
    def actualizar_ficha(self):

        print("\n--- ACTUALIZAR FICHA ---")

        id_ficha = input("Ingrese ID de la ficha a actualizar: ")
        nueva_nota = input("Nueva nota: ")

        sql = "UPDATE ficha_clinica SET notas = %s WHERE id_ficha = %s"
        valores = (nueva_nota, id_ficha)

        try:
            cur.execute("SELECT id_ficha FROM ficha_clinica WHERE id_ficha = %s", (id_ficha,))
            if cur.fetchone() is None:
                print(" No existe una ficha con ese ID.\n")
                return

            cur.execute(sql, valores)
            mydb.commit()
            print(" Ficha clínica actualizada correctamente!\n")

        except Exception as e:
            print(" Error al actualizar ficha:", e)

    # === ELIMINAR FICHA ===
    def eliminar_ficha(self):

        print("\n--- ELIMINAR FICHA ---")

        id_ficha = input("Ingrese ID de la ficha a eliminar: ")

        try:
            cur.execute("SELECT id_ficha FROM ficha_clinica WHERE id_ficha = %s", (id_ficha,))
            if cur.fetchone() is None:
                print(" No existe una ficha con ese ID.\n")
                return

            cur.execute("DELETE FROM ficha_clinica WHERE id_ficha = %s", (id_ficha,))
            mydb.commit()
            print(" Ficha clínica eliminada correctamente!\n")

        except Exception as e:
            print(" Error al eliminar ficha:", e)

    # === MENÚ FICHA CLÍNICA ===
    def menu_ficha(self):

        while True:
            print("""
--- MENÚ FICHA CLÍNICA ---
1. Crear ficha clínica
2. Listar fichas clínicas
3. Actualizar ficha clínica
4. Eliminar ficha clínica
0. Salir
""")

            opc = input("Seleccione una opción: ")

            if opc == "1":
                self.crear_ficha()

            elif opc == "2":
                self.listar_fichas()

            elif opc == "3":
                self.actualizar_ficha()

            elif opc == "4":
                self.eliminar_ficha()

            elif opc == "0":
                print("Saliendo del menú...")
                break

            else:
                print("⚠ Opción inválida.\n")
