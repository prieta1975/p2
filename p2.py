# Ejemplos de uso de ficheros

import sys                  # Permite utilizar la variable __name__





if __name__ == "__main__":  # Determina si estamos en el espacio de nombres principal
    print("En main")
    imprimir_parametros_entrada(*sys.argv)    # Para lista con los argumentos de entrada

    # Cuerpo de programa
    listas()
    diccionarios()
    funciones()
    funciones(1, 1)
    funciones(1, 1, 2, 3)
    diccionarioEntrada = {(1, 1), (2, 2)}
    funciones(1, 1, 2, diccionarioEntrada)
    funciones(1, 1, 2, diccionarioEntrada, diccionarioEntrada)
else:
    print("Fuera de main")

print()
print("--------------------")
print("Fin de Programa")

