import sys

def rectange(width, height):
    if width 
    if height 



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
