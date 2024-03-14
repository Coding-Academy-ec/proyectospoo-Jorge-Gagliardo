from gestion_proyectos.usuario import Usuario

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, usuario):
        self.miembros.append(usuario)

    def listar_miembros(self):
        return self.miembros
