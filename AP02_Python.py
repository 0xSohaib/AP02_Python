import sys

"""
El módulo sys en Python proporciona acceso a varios parámetros 
y funciones del sistema, especialmente útiles para interactuar 
con el intérprete

https://docs.python.org/es/3.10/library/sys.html
"""

help(sys)

def main():
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            rectangle(x, y)
        except ValueError:
            print("Los argumentos deben ser números enteros")
    else:
        print("Uso: python main.py <ancho> <alto>")       

"""
Este bloque se asegura de que la función `main()` solo se ejecute 
cuando este archivo se ejecuta directamente desde la línea de comandos, 
y no cuando se importa como módulo en otro archivo

__name__ es una variable especial de Python:
- Si el archivo se ejecuta directamente: __name__ == "__main__"
- Si el archivo se importa desde otro archivo: __name__ == "nombre_del_modulo"
"""

if __name__ == "__main__":
    main()
