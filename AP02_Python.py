import sys

def rectange(width, height):
    """
    Primera acción: Revisa si width <= 0 o height <= 0. No hace nada.
    Segunda acción: Revisa si el borde superior height >= 1, en ese caso Si width == 1, imprime "o". De lo contrario, imprime "o" + "-"*(width-2) + "o".
    Tercera acción: Repite (height-2) veces si width == 1, imprime "|", de lo contrario imprime "|" + " "*(width-2) + "|".
    Última: Si heigth > 1 y width == 1: imprime "o". De lo contrairo imprime "o" + "-"*(width-2) + "o".
    """
    if width <= 0 or height <= 0:
        return
    if height >= 1:
        if width == 1:
            print("o")
        else:
            print("o" + "-" * (width - 2) + "o")
    for i in range(height - 2):
        if width == 1:
            print("|")
        else:
            print("|" + " " * (width - 2) + "|")
    if height > 1:
        if width == 1:
            print("o")
        else:
            print("o" + "-" * (width - 2) + "o")

def main():
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            rectangle(x, y)
        except ValueError:
            print("Los argumentos deben ser números enteros")
    else:
        print("Uso: python AP02_Python.py <ancho> <alto>")       

if __name__ == "__main__":
    main()
