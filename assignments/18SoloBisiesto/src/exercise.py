def main():
    #escribe tu código abajo de esta línea
    year = int(input("Año: "))
    if year > 0:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(True)
        else:
            print(False)
    else:
        print("Dato incorrecto")


if __name__=='__main__':
    main()
