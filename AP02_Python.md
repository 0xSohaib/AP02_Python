*09 / Sept / 2025*
# Ejercicio práctico 2
## Contenido

### Entendiendo import sys y sys.args

**Importar módulos:**
- Python funciona con módulos; Uno de los mas importantes y que ya viene integrado en Python es **sys**.
- Este módulo proporciona acceso a variables y funciones que están relacionadas con el intérprete de Python y el sistema. 

**Acceder a los argumentos:**
- Para acceder a los argumentos, hay que consultarlos desde la línea de comando haciendo una llamada a **args.sys**.

- En este ejercicio podemos ver que en `main()` hay definidos una lista de argumentos en `if len(sys.argv) == 3:`, mas concretamente, el programa espera 2 argumentos de 3 elementos.

Dentro de los argumentos, se convierte el input de terminal a números enteros mediante 

```python
    x = int(sys.argv[1])
    y = int(sys.argv[2])
```
Para 
