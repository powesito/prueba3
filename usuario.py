from conexion import Conexion

conexion = Conexion()
cur, mydb = conexion.conectar()


class Usuario:

    def __init__(self):
        pass

    def login(self) -> bool:
        """
        Pide username + password. Verifica en DB usando SHA2.
        Devuelve True si login ok, False si no.
        """
        print("\n--- LOGIN ---")
        username = input("Usuario: ")
        password = input("Contraseña: ")

        try:
            sql = "SELECT id_usuario FROM usuario WHERE username = %s AND password = SHA2(%s, 256)"
            cur.execute(sql, (username, password))
            row = cur.fetchone()
            if row:
                print(" Inicio de sesión correcto. Bienvenido/a.\n")
                return True
            else:
                print(" Usuario o contraseña incorrectos.")
                return False
        except Exception as e:
            print(" Error al intentar iniciar sesión:", e)
            return False

    # CRUD básico de usuarios (para el requisito "Gestión de Usuarios")
    def crear_usuario(self):
        print("\n--- CREAR USUARIO ---")
        username = input("Nuevo username: ")
        password = input("Contraseña: ")

        try:
            sql = "INSERT INTO usuario(username, password) VALUES (%s, SHA2(%s,256))"
            cur.execute(sql, (username, password))
            mydb.commit()
            print(" Usuario creado correctamente.\n")
        except Exception as e:
            print(" Error al crear usuario:", e)

    def listar_usuarios(self):
        print("\n--- LISTA DE USUARIOS ---")
        try:
            cur.execute("SELECT id_usuario, username FROM usuario")
            rows = cur.fetchall()
            for r in rows:
                print(r)
            print()
        except Exception as e:
            print(" Error al listar usuarios:", e)

    def eliminar_usuario(self):
        print("\n--- ELIMINAR USUARIO ---")
        uid = input("Ingrese id_usuario a eliminar: ")
        try:
            cur.execute("DELETE FROM usuario WHERE id_usuario = %s", (uid,))
            mydb.commit()
            if cur.rowcount > 0:
                print(" Usuario eliminado.\n")
            else:
                print(" No existe ese id_usuario.\n")
        except Exception as e:
            print(" Error al eliminar usuario:", e)

    def menu_usuario(self):
        while True:
            print("""
--- MENÚ USUARIOS ---
1. Crear usuario
2. Listar usuarios
3. Eliminar usuario
0. Salir
""")
            opc = input("Seleccione opción: ")
            if opc == "1":
                self.crear_usuario()
            elif opc == "2":
                self.listar_usuarios()
            elif opc == "3":
                self.eliminar_usuario()
            elif opc == "0":
                break
            else:
                print(" Opción inválida.\n")
