from conexion import Conexion

# Conexión global
conexion = Conexion()
cur, mydb = conexion.conectar()


class Procedimiento:

    # === CREAR PROCEDIMIENTO ===
    def crear_procedimiento(self):

        print("\n--- REGISTRAR PROCEDIMIENTO ---")

        nombre = input("Nombre del procedimiento: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        tipo = input("Tipo de procedimiento: ")
        rut_veterinario = input("RUT del veterinario responsable: ")
        indicaciones = input("Indicaciones / Notas: ")

        # Validar costo
        while True:
            try:
                costo = int(input("Costo: "))
                break
            except ValueError:
                print(" Costo inválido. Debe ser un número entero.")

        # Validar veterinario existente
        cur.execute("SELECT rut FROM veterinario WHERE rut = %s", (rut_veterinario,))
        if cur.fetchone() is None:
            print(" El veterinario no existe. No se puede registrar el procedimiento.\n")
            return

        sql = """
        INSERT INTO procedimiento(nombre, fecha_creacion, tipo_procedimiento, 
                                  veterinario_responsable, indicaciones, costo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (nombre, fecha, tipo, rut_veterinario, indicaciones, costo)

        try:
            cur.execute(sql, valores)
            mydb.commit()
            print("✔ Procedimiento registrado correctamente!\n")
        except Exception as e:
            print(" Error al registrar procedimiento:", e)

    # === LISTAR PROCEDIMIENTOS ===
    def listar_procedimientos(self):

        print("\n--- LISTA DE PROCEDIMIENTOS ---")
        cur.execute("""
            SELECT p.id_procedimiento, p.nombre, p.fecha_creacion, 
                   p.tipo_procedimiento, v.nombre AS veterinario,
                   p.indicaciones, p.costo
            FROM procedimiento p
            LEFT JOIN veterinario v ON p.veterinario_responsable = v.rut
        """)
        procedimientos = cur.fetchall()

        if not procedimientos:
            print(" No hay procedimientos registrados.\n")
            return

        for p in procedimientos:
            print(f"""
ID: {p[0]}
Nombre: {p[1]}
Fecha: {p[2]}
Tipo: {p[3]}
Veterinario: {p[4]}
Indicaciones: {p[5]}
Costo: ${p[6]}
-------------------------------------------
""")

    # === ACTUALIZAR COSTO DEL PROCEDIMIENTO ===
    def actualizar_procedimiento(self):

        id_proc = input("Ingrese ID del procedimiento a actualizar: ")

        # Validar existencia
        cur.execute("SELECT id_procedimiento FROM procedimiento WHERE id_procedimiento = %s", (id_proc,))
        if cur.fetchone() is None:
            print(" No existe un procedimiento con ese ID.\n")
            return

        print("\n--- ACTUALIZAR PROCEDIMIENTO ---")

        while True:
            try:
                nuevo_costo = int(input("Nuevo costo: "))
                break
            except ValueError:
                print(" Valor inválido. Debe ser un número entero.")

        sql = "UPDATE procedimiento SET costo = %s WHERE id_procedimiento = %s"
        valores = (nuevo_costo, id_proc)

        try:
            cur.execute(sql, valores)
            mydb.commit()
            print("✔ Procedimiento actualizado correctamente!\n")
        except Exception as e:
            print(" Error al actualizar procedimiento:", e)

    # === ELIMINAR PROCEDIMIENTO ===
    def eliminar_procedimiento(self):

        id_proc = input("Ingrese ID del procedimiento a eliminar: ")

        # Validar existencia
        cur.execute("SELECT id_procedimiento FROM procedimiento WHERE id_procedimiento = %s", (id_proc,))
        if cur.fetchone() is None:
            print(" No existe un procedimiento con ese ID.\n")
            return

        sql = "DELETE FROM procedimiento WHERE id_procedimiento = %s"

        try:
            cur.execute(sql, (id_proc,))
            mydb.commit()
            print(" Procedimiento eliminado correctamente!\n")

        except Exception as e:
            print(" Error al eliminar procedimiento:", e)

    # === MENÚ DEL MÓDULO ===
    def menu_procedimiento(self):

        while True:
            print("""
--- MENÚ PROCEDIMIENTOS ---
1. Registrar procedimiento
2. Listar procedimientos
3. Actualizar costo
4. Eliminar procedimiento
0. Salir
""")

            opc = input("Seleccione una opción: ")

            if opc == "1":
                self.crear_procedimiento()
            elif opc == "2":
                self.listar_procedimientos()
            elif opc == "3":
                self.actualizar_procedimiento()
            elif opc == "4":
                self.eliminar_procedimiento()
            elif opc == "0":
                print("Saliendo del menú...")
                break
            else:
                print(" Opción inválida.\n")
