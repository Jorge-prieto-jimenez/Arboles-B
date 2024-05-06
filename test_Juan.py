from Juan import ArbolBinarioBusqueda
def test_arbol_binario_busqueda():
    # Creamos el árbol
    arbol = ArbolBinarioBusqueda()

    # Insertamos algunos nodos
    arbol.insertar({'k': 5, 'nombre': 'Nodo 5', 'identificacion': 123})
    arbol.insertar({'k': 3, 'nombre': 'Nodo 3', 'identificacion': 456})
    arbol.insertar({'k': 7, 'nombre': 'Nodo 7', 'identificacion': 789})
    arbol.insertar({'k': 1, 'nombre': 'Nodo 1', 'identificacion': 101112})
    arbol.insertar({'k': 4, 'nombre': 'Nodo 4', 'identificacion': 131415})
    arbol.insertar({'k': 6, 'nombre': 'Nodo 6', 'identificacion': 161718})
    arbol.insertar({'k': 8, 'nombre': 'Nodo 8', 'identificacion': 192021})

    # Probamos la función inorder
    assert arbol.inorder() == [{'k': 1, 'nombre': 'Nodo 1', 'identificacion': 101112},
                               {'k': 3, 'nombre': 'Nodo 3', 'identificacion': 456},
                               {'k': 4, 'nombre': 'Nodo 4', 'identificacion': 131415},
                               {'k': 5, 'nombre': 'Nodo 5', 'identificacion': 123},
                               {'k': 6, 'nombre': 'Nodo 6', 'identificacion': 161718},
                               {'k': 7, 'nombre': 'Nodo 7', 'identificacion': 789},
                               {'k': 8, 'nombre': 'Nodo 8', 'identificacion': 192021},
                               {'k': 3, 'nombre': 'Nodo 3', 'identificacion': 456},
                               {'k': 4, 'nombre': 'Nodo 4', 'identificacion': 131415},
                               {'k': 5, 'nombre': 'Nodo 5', 'identificacion': 123},
                               {'k': 6, 'nombre': 'Nodo 6', 'identificacion': 161718},
                               {'k': 7, 'nombre': 'Nodo 7', 'identificacion': 789},
                               {'k': 8, 'nombre': 'Nodo 8', 'identificacion': 192021}]

    # Probamos la función encontrar_minimo
    assert arbol.encontrar_minimo(arbol.raiz).datos == {'k': 1, 'nombre': 'Nodo 1', 'identificacion': 101112}

    # Probamos la función encontrar_maximo
    assert arbol.encontrar_maximo(arbol.raiz).datos == {'k': 8, 'nombre': 'Nodo 8', 'identificacion': 192021}

    # Probamos la función eliminar_por_identificacion
    arbol.eliminar_por_identificacion(456)
    assert arbol.buscar_por_identificacion(456) is None

    # Probamos la función buscar_por_identificacion
    assert arbol.buscar_por_identificacion(123)['nombre'] == 'Nodo 5'

    # Probamos la función valor_maximo
    assert arbol.valor_maximo() == {'k': 8, 'nombre': 'Nodo 8', 'identificacion': 192021}

    # Probamos la función valor_minimo
    assert arbol.valor_minimo() == {'k': 1, 'nombre': 'Nodo 1', 'identificacion': 101112}

test_arbol_binario_busqueda()