from conexion import Conexion

# Crear conexión global
conexion = Conexion()
cur, mydb = conexion.conectar()


class Mascota:

    # === CREAR MASCOTA ===
    def crear_mascota(self):
        print("\n--- REGISTRAR MASCOTA ---")

        nombre = input("Ingrese nombre de la mascota: ")
        especie = input("Ingrese especie de la mascota: ")
        raza = input("Ingrese raza de la mascota: ")
        edad = input("Ingrese edad de la mascota: ")
        peso = input("Ingrese peso de la mascota: ")
        sexo = input("Ingrese sexo (M/F/Desconocido): ")
        rut_cuidador = input("Ingrese rut del cuidador: ")

        sql = """
            INSERT INTO mascota(nombre, especie, raza, edad, peso, sexo, rut_cuidador)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (nombre, especie, raza, edad, peso, sexo, rut_cuidador)

        try:
            cur.execute(sql, valores)
            mydb.commit()
            print(" Mascota registrada correctamente!\n")
        except Exception as e:
            print(" Error al registrar mascota:", e)

    # === LISTAR MASCOTAS ===
    def listar_mascota(self):

        print("\n--- LISTA DE MASCOTAS ---")

        try:
            cur.execute("SELECT * FROM mascota")
            mascotas = cur.fetchall()

            if len(mascotas) == 0:
                print("No hay mascotas registradas.\n")
                return

            for m in mascotas:
                print(m)

            print()

        except Exception as e:
            print(" Error al listar mascotas:", e)

    # === ACTUALIZAR MASCOTA ===
    def actualizar_mascota(self):
        print("\n--- ACTUALIZAR MASCOTA ---")

        id_mascota = input("Ingrese ID de la mascota a actualizar: ")
        nuevo_nombre = input("Nuevo nombre: ")

        try:
            # Verificar existencia
            cur.execute("SELECT id_mascota FROM mascota WHERE id_mascota = %s", (id_mascota,))
            if cur.fetchone() is None:
                print(" No existe una mascota con ese ID.\n")
                return

            sql = "UPDATE mascota SET nombre = %s WHERE id_mascota = %s"
            valores = (nuevo_nombre, id_mascota)

            cur.execute(sql, valores)
            mydb.commit()
            print(" Mascota actualizada correctamente!\n")

        except Exception as e:
            print(" Error al actualizar mascota:", e)

    # === ELIMINAR MASCOTA ===
    def eliminar_mascota(self):
        print("\n--- ELIMINAR MASCOTA ---")

        id_mascota = input("Ingrese ID de la mascota a eliminar: ")

        try:
            cur.execute("SELECT id_mascota FROM mascota WHERE id_mascota = %s", (id_mascota,))
            if cur.fetchone() is None:
                print(" No existe una mascota con ese ID.\n")
                return

            cur.execute("DELETE FROM mascota WHERE id_mascota = %s", (id_mascota,))
            mydb.commit()
            print(" Mascota eliminada correctamente!\n")

        except Exception as e:
            print(" Error al eliminar mascota:", e)

    # === MENÚ MASCOTAS ===
    def menu_mascota(self):

        while True:
            print("""
--- MENÚ MASCOTAS ---
1. Agregar mascota
2. Listar mascotas
3. Actualizar mascota
4. Eliminar mascota
0. Salir
""")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_mascota()
            elif opcion == "2":
                self.listar_mascota()
            elif opcion == "3":
                self.actualizar_mascota()
            elif opcion == "4":
                self.eliminar_mascota()
            elif opcion == "0":
                print("Saliendo del menú...")
                break
            else:
                print(" Opción inválida.\n")