
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad > 0:
        if edad >= 18:
            credencial=input("¿Tienes identificación oficial? (s/n): ")
            if credencial=="s" or credencial=="S":
                print("Trámite de licencia concedido")
            elif credencial=="n" or credencial=="N":
                print("No cumples requisitos")
            else:
                print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")


if __name__ == '__main__':
    main()
