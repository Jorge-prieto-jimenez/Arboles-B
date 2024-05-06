class Nodo:
    def __init__(self, datos, izquierda=None, derecha=None):
        self.datos = datos
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"{self.datos['nombre']}, {self.datos['identificacion']}, {self.datos['k']}"