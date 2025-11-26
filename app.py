# app.py — Punto de entrada del sistema

from usuario import Usuario
from cuidador import Cuidador
from mascota import Mascota
from veterinaria import Veterinario
from procedimiento import Procedimiento
from fichaclinica import FichaClinica
from conexion import Conexion


class App:

    def __init__(self):
        self.conexion = Conexion()
        self.usuario = Usuario()

    # === INICIO DE SESIÓN ===
    def login(self):
        print("""
=============================
   SISTEMA DE GESTIÓN VETERINARIA
=============================
        """)

        print("💠 INICIO DE SESIÓN 💠")

        # Repetir hasta que logre iniciar sesión correctamente
        while True:
            if self.usuario.login():
                break
            print("Intente nuevamente...\n")

    # === MENÚ PRINCIPAL ===
    def menu_principal(self):

        while True:
            print("""
=============================
     MENÚ PRINCIPAL
=============================
1. Gestión de Cuidadores
2. Gestión de Mascotas
3. Gestión de Veterinarios
4. Gestión de Procedimientos
5. Gestión de Fichas Clínicas
6. Gestión de Usuarios
7. Salir
""")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Cuidador().menu_cuidador()

            elif opcion == "2":
                Mascota().menu_mascota()

            elif opcion == "3":
                Veterinario().menu_veterinario()

            elif opcion == "4":
                Procedimiento().menu_procedimiento()

            elif opcion == "5":
                FichaClinica().menu_ficha()

            elif opcion == "6":
                Usuario().menu_usuario()

            elif opcion == "7":
                print("Saliendo del sistema... ¡Hasta luego!")
                break

            else:
                print(" Opción inválida, intente nuevamente.\n")


# ==== EJECUCIÓN DEL SISTEMA ====
if __name__ == "__main__":
    app = App()
    app.login()
    app.menu_principal()
