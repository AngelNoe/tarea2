![Tec de Monterrey](../../images/logotecmty.png)
# Número más grande
Decisiones - Elegir entre 3 números el más grande

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def largest_of_three(a, b, c):
    # Write your code here
    pass


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(check_grade(a, b, c))


if __name__ == '__main__':
    main()
```

El programa va a preguntar por tres números, y al final debe imprimir sólo
el número que es mayor que los demás.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter first number: 6
Enter second number: 9
Enter third number: 4
9
```

```plaintext
Enter first number: 4
Enter second number: 3
Enter third number: 1
4
```

Únicamente necesitas modificar la función **largest_of_three**.
Elimina la palabra __pass__ y escribe el código necesario.
Asegurarte de que la función regrese el valor correcto.

Una vez que termines tu actividad y la hayas probado con `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
