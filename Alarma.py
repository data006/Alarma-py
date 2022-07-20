
hora = input("Ingresa la hora actual: ")
hora = int(hora)
alarma = input("Ingresa la cantidad que deseas que transcurran: ")
alarma = int(alarma)

for i in range(0,alarma):
    if hora < 24:
        hora += 1
    if hora == 24:
        hora = 0

print('Sonara a las: ',hora,'hrs')
