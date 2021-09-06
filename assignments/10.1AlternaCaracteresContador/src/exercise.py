def main():
    #escribe tu código abajo de esta línea
    n = int(input("Teclee un numero: "))
    count = 1
    y = 1
    while y < n+1:
        if count%2 == 0:
            print(str(count)+"#")
        else:
            print(str(count)+"%")
        count += 1
        y += 1
    pass

if __name__=='__main__':   
    main()
