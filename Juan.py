class Nodo:
    def __init__(self, datos, izquierda=None, derecha=None):
        self.datos = datos
        self.izquierda = izquierda
        self.derecha = derecha

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, datos):
        if not self.raiz:
            self.raiz = Nodo(datos)
        else:
            self._insertar_recursivo(datos, self.raiz)

    def _insertar_recursivo(self, datos, nodo_actual):
        if datos['k'] < nodo_actual.datos['k']:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(datos)
            else:
                self._insertar_recursivo(datos, nodo_actual.izquierda)
        elif datos['k'] >= nodo_actual.datos['k']:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(datos)
            else:
                self._insertar_recursivo(datos, nodo_actual.derecha)

    def inorder(self, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        if nodo_actual.izquierda:
            self.inorder(nodo_actual.izquierda)

        print(nodo_actual.datos)

        if nodo_actual.derecha:
            self.inorder(nodo_actual.derecha)

    def encontrar_minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def encontrar_maximo(self, nodo):
        while nodo.derecha:
            nodo = nodo.derecha
        return nodo

    def eliminar_por_identificacion(self, identificacion):
        self.raiz = self._eliminar_recursivo_por_identificacion(self.raiz, identificacion)

    def _eliminar_recursivo_por_identificacion(self, nodo_actual, identificacion):
        if not nodo_actual:
            return nodo_actual

        if identificacion < nodo_actual.datos['identificacion']:
            nodo_actual.izquierda = self._eliminar_recursivo_por_identificacion(nodo_actual.izquierda, identificacion)
        elif identificacion > nodo_actual.datos['identificacion']:
            nodo_actual.derecha = self._eliminar_recursivo_por_identificacion(nodo_actual.derecha, identificacion)
        else:
            # Caso 1: Nodo hoja o caso 2: Nodo con un hijo
            if not nodo_actual.izquierda:
                return nodo_actual.derecha
            elif not nodo_actual.derecha:
                return nodo_actual.izquierda

            # Caso 3: Nodo con dos hijos
            sucesor = self.encontrar_minimo(nodo_actual.derecha)
            nodo_actual.datos = sucesor.datos
            nodo_actual.derecha = self._eliminar_recursivo_por_identificacion(nodo_actual.derecha, sucesor.datos['identificacion'])

        return nodo_actual

    def buscar_por_identificacion(self, identificacion, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        while nodo_actual:
            if identificacion == nodo_actual.datos['identificacion']:
                return nodo_actual.datos
            elif identificacion < nodo_actual.datos['identificacion']:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

        return None

    def valor_maximo(self):
        maximo = self.encontrar_maximo(self.raiz)
        return maximo.datos if maximo else None

    def valor_minimo(self):
        minimo = self.encontrar_minimo(self.raiz)
        return minimo.datos if minimo else None

    def mostrar_arbol(self):
        self._mostrar_arbol_recursivo(self.raiz, "")

    def _mostrar_arbol_recursivo(self, nodo, prefijo):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, prefijo + "    ")
            print(prefijo + f"|__ {nodo.datos['nombre']}")
            self._mostrar_arbol_recursivo(nodo.izquierda, prefijo + "    ")



# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    arbol.insertar({'nombre': 'Juan', 'identificacion': 10101013, 'k': 7})
    arbol.insertar({'nombre': 'Pablo', 'identificacion': 10001011, 'k': 4})
    arbol.insertar({'nombre': 'Maria', 'identificacion': 10101015, 'k': 9})
    arbol.insertar({'nombre': 'Ana', 'identificacion': 1010000, 'k': 2})
    arbol.insertar({'nombre': 'Diana', 'identificacion': 10111105, 'k': 10})
    arbol.insertar({'nombre': 'Mateo', 'identificacion': 10110005, 'k': 8})


    while True:
        opcion = input("\nIngrese la opción\n"
                       "'a' para agregar\n"
                       "'e' para eliminar\n"
                       "'b' para buscar\n"
                       "'m' para valor máximo\n"
                       "'n' para valor mínimo\n"
                       "'d' para mostrar árbol\n"
                       "'i' para mostrar recorrido inorder\n"
                       "'s' para salir\n")

        if opcion.lower() == 's':
            break
        elif opcion.lower() == 'a':
            nombre = input("Ingrese el nombre: ")
            identificacion = int(input("Ingrese el número de identificación: "))
            k = sum(int(digito) for digito in str(identificacion) if digito.isdigit())
            datos = {'nombre': nombre, 'identificacion': identificacion, 'k': k}
            arbol.insertar(datos)
            print("Nodo agregado.")
        elif opcion.lower() == 'e':
            identificacion_a_eliminar = int(input("Ingrese el número de identificación a eliminar: "))
            arbol.eliminar_por_identificacion(identificacion_a_eliminar)
            print("Nodo eliminado.")
        elif opcion.lower() == 'b':
            identificacion_a_buscar = int(input("Ingrese el número de identificación a buscar: "))
            resultado_busqueda = arbol.buscar_por_identificacion(identificacion_a_buscar)
            if resultado_busqueda:
                print(f"Nodo encontrado: {resultado_busqueda}")
            else:
                print("Nodo no encontrado.")
        elif opcion.lower() == 'm':
            maximo = arbol.valor_maximo()
            if maximo:
                print(f"Nodo con valor máximo: {maximo}")
            else:
                print("Árbol vacío.")
        elif opcion.lower() == 'n':
            minimo = arbol.valor_minimo()
            if minimo:
                print(f"Nodo con valor mínimo: {minimo}")
            else:
                print("Árbol vacío.")

        elif opcion.lower() == 'd':
            arbol.mostrar_arbol()
        elif opcion.lower() == 'i':
            print("\nRecorrido inorder del árbol:")
            arbol.inorder()
        else:
            print("Opción no válida. Inténtelo de nuevo.")

    print("\nRecorrido inorder del árbol:")
    arbol.inorder()
