![Tec de Monterrey](../../images/logotecmty.png)
# Next day
Decisiones - Determina cual es el siguiente día en el calendario después
de la fecha provista por el usuario

**NOTA:** Este ejercicio requiere el uso de funciones.
Los casos de prueba verifican que las funciones regresen los valores correctos.

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def is_leap(year):
    # Write your code here
    pass


def month_days(month, year):
    # Write your code here
    pass


def next_day(day, month, year):
    # Write your code here
    pass


def main():
    day = int(input("Enter the day: "))
    month = int(input("Enter the day: "))
    year = int(input("Enter the day: "))
    n_day, n_month, n_year = next_day(day, month, year)
    print(f"Next day: {n_day}/{n_month}/{n_year}")


if __name__ == '__main__':
    main()
```

Los meses del año tienen diferente número de días, y en particular el mes de
Febrero varía en sus días según los años bisiestos. Por lo tanto hay varias
decisiones involucradas al solicitar el día siguiente a una fecha.

Cómo referencia, los meses de enero, marzo, mayo, julio, agosto, octubre y
diciembre tienen 31 días. Mientras que abril, junio, septiembre y noviembre
tienen 30 días. Febrero puede tener 28 o 29, según el año.

Los años bisiestos son aquellos que son divisibles entre 4, pero hay algunos
[casos especiales](https://www.timeanddate.com/date/leapyear.html#rules).
Los años que son divisibles entre 100 **no** son bisiestos, a menos que sean
divisibles entre 400.

El programa va a preguntar por tres números, el día, mes y año actual,
y debe imprimir la fecha del día siguiente.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter the day: 28
Enter the month: 2
Enter the year: 2020
Next day: 29/2/2020
```

```plaintext
Enter the day: 31
Enter the month: 12
Enter the year: 2021
Next day: 1/1/2022
```

Debes modificar varias funciones para este ejercicio. Cada una debe regresar
un valor, según la siguiente lista:
- **is_leap**: recibe un año y regresa un booleano, indicando si es un
año bisiesto o no
- **month_days**: recibe un mes y un año, y regresa el número de días en
ese mes
- **next_day**: recibe el día, mes y año, y regresa 3 valores, correspondientes
al día siguiente (día, mes y año)

Una vez que termines tu actividad y la hayas probado con `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
