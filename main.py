from Figurasgeometricas import Figurasgeometricas
from Triangulo import Triangulo
from Cuadradro import Cuadradro
from Rectangulo import Rectangulo
from Circulo import Circulo
from Cilindro import Cilindro
from Paralelograma import Paralelograma 
from Trapecio import Trapecio
from Esfera import Esfera


while True:
    print("---------- Menu de Figuras Geometricas-----------")
    print("1.Triangulo")
    print("2.Cuadradro")
    print("3.Rectangulo")
    print("4.Circulo")
    print("5.Cilindro")
    print("6,Paralelograma")
    print("7.Trapecio")
    print("8.Esfera")
    print("9.salir")

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
        radio = float(input("Digite el radio del Cilindro: "))
        altura = float(input("Digite la altura del Cilindro: "))

        ci = Cilindro("Cilindro")
        ci.radio = radio
        ci.altura = altura
        print("El area del Cilindro es:",opcion, "es",ci.area())

    elif opcion == 6:
        base = float(input("Digite la base del Paralelograma: "))
        altura = float(input("Digite la altura del Paralelogrma: "))
        pr= Paralelograma("Paralelograma")
        pr.base = base
        pr.altura = altura
        print("El area del Paralelograma es:",opcion, "es",pr.area())


    elif opcion == 7:
         b_mayor = float(input("Ingrese la base mayor del Trapecio: "))
         b_menor = float(input("Ingrese la base menor del Trapecio: "))
         altura = float(input("Ingrese la altura del Trapecio: "))
         figura = Trapecio(b_mayor, b_menor, altura)     
         print("El área del Trapecio es:", figura.area())

    elif opcion == 8:
         radio = float(input("Ingrese el radio de la Esfera: "))
         figura = Esfera(radio)
         print("El área de la Esfera es:", figura.area())

    elif opcion == 9:
        print("Saliendo del programa...")
        break


        print()  # Línea en blanco para que el menú se vea más limpio