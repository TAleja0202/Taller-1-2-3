# ejercicio 1 pasado a python

dolar = 0.00027
pesos = float(input("Digite la cantidad de pesos a comvertir "))
comvercion: float = pesos * dolar
print(f"El valor en dolares es: {comvercion:.2f}")


# ejercicio 2 pasado a python

numero = int(input("Ingrese un numero Entero: "))
print(type(numero))
print(f"El Numero Igresado es: ", numero)


# ejercicio 3 pasado a python

presion = float(input("Ingrese la cantidad de la Precion: "))
volumen = float(input("Ingrese la cantidad de la volumen: "))
temperatura = float(input("Ingrese la cantidad de la temperatura: "))
masaAire = (presion * volumen)/(0.37*(temperatura + 460))
print(f"La masa de Aire es de: ", masaAire)


# ejercicio 4 pasado a python

numPulsacion = 220
Edad = int(input("Ingrese su edad: "))
totalPulso = (220 - Edad)/10
print(f"Su pulso por el Ejercicio es: ", totalPulso)


# ejercicio 5 pasado a python

salario = int(input("Ingrese su Salario Actual: "))
nuevoSal = salario + (salario * 0.25)
print(f"Su nuevo Salario es: ", nuevoSal)


# ejercicio 6 pasado a python

presupuesto = float(input("Ingrese el Valor del Presupuesto Anual "))
ginecologia = presupuesto * 0.40
traumatologia = presupuesto * 0.30
pediatria = presupuesto * 0.30
print(f"El presupuesto para Ginecologia es de: {ginecologia:.2f}")
print(f"El presupuesto para Traumatologia es de: {traumatologia:.2f}")
print(f"El presupuesto para Pediatria es de: {pediatria:.2f}")


# ejercicio 7 pasado a python

compra = float(input("Ingrese el Valor de la Compra "))
nuevoVal = compra + 3500
ganancia = nuevoVal * 0.30
print(f"Valor al cual lo debe Vender: {nuevoVal:.2f}")
print(f"y la ganancia es de: {ganancia:.2f}")
