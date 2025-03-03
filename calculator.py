
continuar = "Y"
resultado= 0
while continuar.upper()=="Y":

    n1 = int(input("Ingrese el primer dígito: "))
    n2 = int(input("Ingrese el segundo dígito: "))
    op = int(input("Elija la operación a realizar según el numeral"
          "\n1) Suma"
          "\n2) Resta"
          "\n3) Multiplicación"
          "\n4) División\n")
          )
    
    if (op==1):
        print(f"{n1}+{n2}={n1+n2}")
    elif(op==2):
        print(f"{n1}-{n2}={n1-n2}")
    elif(op==3):
        print(f"{n1}*{n2}={n1*n2}")
    elif(op==4):
        print(f"{n1}/{n2}={n1/n2}")
    else:
        print("La operación seleccionada"+op+"no es válida")

    continuar = input("Desea realizar otra operación? (Y/N): ")
