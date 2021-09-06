def main():
    #escribe tu código abajo de esta línea
    #Promedio Con Decisión
    count = 1
    a = float(input("Teclee un numero: "))
    i = a
    while a > 0:
        a = float(input("Teclee otro numero: "))
            if a > 0:
                i += a
                count += 1
    promedio = i / count
    print("El promedio es:",promedio)
    pass
if __name__=='__main__':
    main()
