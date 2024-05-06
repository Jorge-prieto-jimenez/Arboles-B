from nodo import Nodo

class ArbolBinarioBusqueda:
    """
    Clase que representa un árbol binario de búsqueda.

    Atributos:
    - raiz: Nodo raíz del árbol.

    Métodos:
    - insertar: Inserta un nuevo nodo en el árbol.
    - eliminar_por_identificacion: Elimina un nodo del árbol por su identificación.
    - buscar_por_identificacion: Busca un nodo en el árbol por su identificación.
    - valor_maximo: Retorna el valor máximo del árbol.
    - valor_minimo: Retorna el valor mínimo del árbol.
    - mostrar_arbol: Muestra el árbol en consola.
    - inorder: Recorre el árbol en orden.
    - encontrar_minimo: Encuentra el nodo con el valor mínimo en el árbol.
    - encontrar_maximo: Encuentra el nodo con el valor máximo en el árbol.
    """
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

    def eliminar_por_identificacion(self, identificacion):
        clave_a_eliminar = sum(int(digito) for digito in str(identificacion) if digito.isdigit())
        self.raiz = self._eliminar_recursivo_por_clave(self.raiz, clave_a_eliminar)

    def _eliminar_recursivo_por_clave(self, nodo_actual, clave):
        if not nodo_actual:
            return nodo_actual

        if clave < nodo_actual.datos['k']:
            nodo_actual.izquierda = self._eliminar_recursivo_por_clave(nodo_actual.izquierda, clave)
        elif clave > nodo_actual.datos['k']:
            nodo_actual.derecha = self._eliminar_recursivo_por_clave(nodo_actual.derecha, clave)
        else:
            # Caso 1: Nodo hoja o caso 2: Nodo con un hijo
            if not nodo_actual.izquierda:
                return nodo_actual.derecha
            elif not nodo_actual.derecha:
                return nodo_actual.izquierda

            # Caso 3: Nodo con dos hijos
            sucesor = self.encontrar_minimo(nodo_actual.derecha)
            nodo_actual.datos = sucesor.datos
            nodo_actual.derecha = self._eliminar_recursivo_por_clave(nodo_actual.derecha, sucesor.datos['k'])

        return nodo_actual

    def buscar_por_identificacion(self, identificacion, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        clave_a_buscar = sum(int(digito) for digito in str(identificacion) if digito.isdigit())

        while nodo_actual:
            if clave_a_buscar == nodo_actual.datos['k']:
                return nodo_actual
            elif clave_a_buscar < nodo_actual.datos['k']:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

        return None

    def valor_maximo(self):
        maximo = self.encontrar_maximo(self.raiz)
        return maximo if maximo else None

    def valor_minimo(self):
        minimo = self.encontrar_minimo(self.raiz)
        return minimo if minimo else None

    def mostrar_arbol(self):
        self._mostrar_arbol_recursivo(self.raiz, 0)
    
    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)
            print("\t" * nivel + f"├───{nodo.datos['nombre']}")
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)

    def inorder(self, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        if nodo_actual.izquierda:
            self.inorder(nodo_actual.izquierda)

        print(nodo_actual)

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