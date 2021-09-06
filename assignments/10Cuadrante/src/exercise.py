def main():
    # Escribe tu código abajo de esta línea
    grado = int(input("Introduce los grados: "))
    if (grado < 0 or grado > 360):
        print("excede")
    elif (grado == 0 or grado == 90 or grado == 180 or grado == 270 or grado == 360):
        print("eje")
    elif (grado > 0 and grado < 90):
        print("cuadrante 1")
    elif (grado < 180):
        print("cuadrante 2")
    elif (grado < 270):
        print("cuadrante 3")
    elif (grado < 360):
        print("cuadrante 4")  

if __name__ == '__main__':
    main()
