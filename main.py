from nodo import Nodo
from arbol_binario_busqueda import ArbolBinarioBusqueda


def agregar_nodo(arbol):
    nombre = input("Ingrese el nombre: ")
    identificacion = int(input("Ingrese el número de identificación: "))
    k = sum(int(digito) for digito in str(identificacion) if digito.isdigit())
    datos = {'nombre': nombre, 'identificacion': identificacion, 'k': k}
    arbol.insertar(datos)
    print("Nodo agregado.")


def eliminar_nodo(arbol):
    identificacion_a_eliminar = int(input("Ingrese el número de identificación a eliminar: "))
    arbol.eliminar_por_identificacion(identificacion_a_eliminar)
    print("Nodo eliminado.")


def buscar_nodo(arbol):
    identificacion_a_buscar = int(input("Ingrese el número de identificación a buscar: "))
    resultado_busqueda = arbol.buscar_por_identificacion(identificacion_a_buscar)
    if resultado_busqueda:
        print(f"Nodo encontrado: {resultado_busqueda}")
    else:
        print("Nodo no encontrado.")


def valor_maximo(arbol):
    maximo = arbol.valor_maximo()
    if maximo:
        print(f"Nodo con valor máximo: {maximo}")
    else:
        print("Árbol vacío.")


def valor_minimo(arbol):
    minimo = arbol.valor_minimo()
    if minimo:
        print(f"Nodo con valor mínimo: {minimo}")
    else:
        print("Árbol vacío.")


def mostrar_arbol(arbol):
    arbol.mostrar_arbol()


def recorrido_inorder(arbol):
    print("\nRecorrido inorder del árbol:")
    arbol.inorder()


def main():
    arbol = ArbolBinarioBusqueda()
    arbol.insertar({'nombre': 'Juan', 'identificacion': 10101013, 'k': 7})
    arbol.insertar({'nombre': 'Pablo', 'identificacion': 10001011, 'k': 4})
    arbol.insertar({'nombre': 'Maria', 'identificacion': 10101015, 'k': 9})
    arbol.insertar({'nombre': 'Ana', 'identificacion': 1010000, 'k': 2})
    arbol.insertar({'nombre': 'Diana', 'identificacion': 10111105, 'k': 10})
    arbol.insertar({'nombre': 'Mateo', 'identificacion': 10110005, 'k': 8})

    while True:
        print("\nMENÚ")
        print("1. Agregar nodo")
        print("2. Eliminar nodo")
        print("3. Buscar nodo")
        print("4. Valor máximo")
        print("5. Valor mínimo")
        print("6. Mostrar árbol")
        print("7. Mostrar recorrido inorder")
        print("8. Salir")

        opcion = input("\nIngrese una opción: ")

        if opcion == '1':
            agregar_nodo(arbol)
        elif opcion == '2':
            eliminar_nodo(arbol)
        elif opcion == '3':
            buscar_nodo(arbol)
        elif opcion == '4':
            valor_maximo(arbol)
        elif opcion == '5':
            valor_minimo(arbol)
        elif opcion == '6':
            mostrar_arbol(arbol)
        elif opcion == '7':
            recorrido_inorder(arbol)
        elif opcion == '8':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
