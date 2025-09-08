import sys

def rectange(width, height):
if width <= 0 or height <= 0:
        return
    if height >= 1:
        if width == 1:
            print("o")



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
