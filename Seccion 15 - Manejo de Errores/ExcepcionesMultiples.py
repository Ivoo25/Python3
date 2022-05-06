try:
    Num=float(input("Ingresa un numero: "))
    print('Tu numero es: ',Num)
except:
    print("No has ingresado un numero")

while(True):
    try:
        Num=float(input("Ingresa un numero: "))
        print('Tu numero es: ',Num)
        break
    except:
        print("No has ingresado un numero")
        
        
while True:
    try:
        num1 = int(input("Introduce un numero: "))
        resultado = 100 / num1
        print(resultado)
        break;  
    except ZeroDivisionError:
        print("No se puede dividir entre cero")       



while True:
    try:
        num1 = int(input("Introduce un numero: "))
        resultado = 100 + num1
        print(resultado)
      
    except KeyboardInterrupt:
        print("\nHas cancelado el programa")
        break               