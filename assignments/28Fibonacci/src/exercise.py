
def main():
    #escribe tu código abajo de esta línea
    n1 = 0
    n2 = 1
    n3 = 0
    count = 0
    num = int(input("Tecle un numero: "))

    while count < num:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1

    print("",n1)
    pass

if __name__=='__main__':
    main()
