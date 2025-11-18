from Figurasgeometricas import Figurasgeometricas
from Triangulo import Triangulo
from Cuadradro import Cuadradro
from Rectangulo import Rectangulo
from Circulo import Circulo

while True:
    print("---------- Menu de Figuras Geometricas-----------")
    print("1.Triangulo")
    print("2.Cuadradro")
    print("3.Rectangulo")
    print("4.Circulo")
    print("5.salir")

    opcion = int(input("Seleccione una opcion: "))

 
    if opcion == 1:
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        tr = Triangulo(base, altura)
        print("El area del triangulo es:", tr.area())

    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        cd = Cuadradro(lado)
        print("El area del cuadrado es:", cd.area())

    elif opcion == 3:
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        rc = Rectangulo(base, altura)
        print("El area del rectangulo es:", rc.area())
    
    elif opcion == 4:
        radio = float(input("Ingrese el radio del circulo: "))
        cr = Circulo(radio)
        print("El area del circulo es:", cr.area())


    
    elif opcion == 5:
        print("Saliendo del programa...")
        break


        print()  # Línea en blanco para que el menú se vea más limpio