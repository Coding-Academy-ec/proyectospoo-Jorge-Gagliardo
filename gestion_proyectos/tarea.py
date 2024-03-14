class Tarea:
    def __init__(self, nombre, descripcion, asignado_a):
        self.nombre = nombre
        self.descripcion = descripcion
        self.asignado_a = asignado_a

    def __str__(self):
        return f"{self.nombre}: {self.descripcion}, asignado a: {self.asignado_a}"
