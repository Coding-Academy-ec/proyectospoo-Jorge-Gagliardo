from gestion_proyectos.usuario import Usuario
from gestion_proyectos.equipo import Equipo
from gestion_proyectos.tarea import Tarea

def main():
    # Creamos algunos usuarios
    usuario1 = Usuario("Jorge")
    usuario2 = Usuario("Connie")
    usuario3 = Usuario("Pedro")

    # Creamos un equipo y agregamos miembros
    equipo1 = Equipo("Equipo A")
    equipo1.agregar_miembro(usuario1)
    equipo1.agregar_miembro(usuario2)

    # Creamos una tarea y la asignamos a un usuario
    tarea1 = Tarea("Hacer informe", "Redactar el informe mensual", usuario1)

    # Mostramos la información del equipo y la tarea
    print("Miembros del equipo:")
    for miembro in equipo1.listar_miembros():
        print(miembro)

    print("\nTarea asignada:")
    print(tarea1)


if __name__ == "__main__":
    main()