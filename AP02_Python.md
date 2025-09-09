*09 / Sept / 2025*
# Ejercicio práctico 2
## Contenido

- [1 - Import sys y sys.args](#1---entendiendo-import-sys-y-sysargs)  
- [2 - Definir funciones](#2---definir-funciones)
- [3 - Main](#3---main) 
- [4 - Código fuente y uso](#4---código-fuente-y-uso)   

### 1 - Entendiendo import sys y sys.args

**Importar módulos:**
- Python funciona con módulos; Uno de los mas importantes y que ya viene integrado en Python es **sys**.
- Este módulo proporciona acceso a variables y funciones que están relacionadas con el intérprete de Python y el sistema. 

**Acceder a los argumentos:**
- Para acceder a los argumentos, hay que consultarlos desde la línea de comando haciendo una llamada a **args.sys**.

- En este ejercicio podemos ver que en `main()` hay definidos una lista de argumentos en `if len(sys.argv) == 3:`, mas concretamente, el programa espera 2 argumentos de 3 elementos.

Los dos argumentos que espera son para definir X e Y. Dentro de los argumentos, se convierte el input de terminal a números enteros mediante 

```python
    x = int(sys.argv[1])
    y = int(sys.argv[2])
```
Se usa `try` para probar si se cumple con los argumentos solicitados, en caso que no sean correctos, mediante `except ValueError:` se especifica qué queremos hacer o mostar en terminal qué ha fallado. En este ejercicio muestra por terminal el siguiente mensaje: `print("Los argumentos deben ser números enteros")`

Si se ejecuta el script sin facilitar argumentos, mediante 
```python
else:
    print("Uso: python main.py <ancho> <alto>")
```
mostramos por pantalla el uso del script, o en este caso, los argumentos que se pueden introducir.

*Nota: argv[0] por defecto es el nombre del script*.

**Código completo:**
```python
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
```
### 2 - Definir funciones

**def:**
- Mediante **def** creamos la función que se va a encargar de dibujar el cuadrado, en este caso es `rectangle`. Dentro de la funcion facilitamos los argumentos que debe aplicar para dibujar el cuadro correctamente.
```python
def rectangle(width, height):
```

**Definición de argumentos (según las reglas):**
- Si `x < 1` o `y < 1`, no se debe imprimir nada
- No se permiten bucles infinitos ni errores
- Solo imprime lo que se indica (nada extra)
- No toques la función `main()`
- Añadir un DocString a la función `rectangle()`.

Así que habría que dividir el cuadrado en 3 partes: Superior, intermedio e inferior.

```python
def rectangle(width, height):
    """
    Primera acción: Revisa si width <= 0 o height <= 0. No hace nada.
    Segunda acción: Revisa si el borde superior height >= 1, en ese caso Si width == 1, imprime "o". De lo contrario, imprime "o" + "-"*(width-2) + "o".
    Tercera acción: Repite (height-2) veces si width == 1, imprime "|", de lo contrario imprime "|" + " "*(width-2) + "|".
    Última: Si heigth > 1 y width == 1: imprime "o". De lo contrairo imprime "o" + "-"*(width-2) + "o".
    """
    if width <= 0 or height <= 0:
        return
```
```python
    if height >= 1:
        if width == 1:
            print("o")
        else:
            print("o" + "-" * (width - 2) + "o")
```
```python
    for i in range(height - 2):
        if width == 1:
            print("|")
        else:
            print("|" + " " * (width - 2) + "|")
```
```python
    if height > 1:
        if width == 1:
            print("o")
        else:
            print("o" + "-" * (width - 2) + "o")
```

### 3 - Main

- Tal y como se indica en la DocString que se nos facilita, `__main__` es una variable especial que se encarga de revisar que únicamente se ejecuta el script desde la línea de comandos/terminal *(python AP02_Python.py)*.

```python

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
```

### 4 - Código fuente y uso

*Disponible también en [Github](https://github.com/0xSohaib/AP02_Python/).*

```python
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
```
**Uso:**

```bash
0x@Sohaib: python3 AP02_Python.py <ancho> <alto>
```
EOF - [Volver al principio](#contenido) 
