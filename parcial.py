alido = True
while valido:
    try:
        num=int(input("Ingresa numero"))
        if num<=0:
            print ("ingresaste un numero negativo o el 0")
        elif num==1:
            print ("ingresaste el numero 1 y no es primo")
        else:
            es_primo = True
            for divisor in range(2, num):
                if num % divisor == 0:
                    print("el numero",num,"no es primo")
                    es_primo = False
                    break
            if es_primo:
                suma = 0
                lista = []

                for numero in range (2,num+1):
                    es_primo2 = True
                    for divisor2 in range(2, numero):
                        if numero % divisor2 == 0:
                            es_primo2 = False
                            break

                    if es_primo2:
                        suma = suma + numero
                        lista.append(numero)

                print ("el nummero ",num,"es primo y la suma de todos los primos desde 2 hasta ",num, "es", suma)
                print ("la lista de numero es", lista)
            valido = False

    except ValueError:
        print("Ingresa un valor correcto")
