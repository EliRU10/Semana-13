import random
Cuadrado = int(input("Ingresar el lado del cuadrado: "))
Radio = int(input("Ingresar el radio del circulo: "))
intentosT = int(input("Ingresar Intentos Totales: "))
Acertaron = 0
for i in range (intentosT):
    x = random.random()*2-1
    y = random.random()*2-1
    radio = (x**2+y**2)**0.5
    if radio <= 1:
        Acertaron += 1
AreaC = Cuadrado**2
print("Area del cuadrado: ", AreaC)
print("Area del circulo: ", (AreaC/intentosT)*Acertaron )