# ejercicio 1 pasado a python /calcular capital

capitalInv = float(input("digite la Capital Invertida: "))
ganancia = capitalInv * 0.02
print(f"La Ganancia del capital es de ${ganancia:.2f}")


# ejercicio 2 /comision por ventas

salarioBas = int(input("Digite el Sueldo Base "))
venta1 = int(input("Digite el valor de la primera Venta "))
venta2 = int(input("Digite el valor de la seg unda Venta "))
venta3 = int(input("Digite el valor de la tercera Venta "))
totalVen = venta1 + venta2 + venta3
comision = totalVen * 0.10
totalPag = salarioBas + comision
print(f"El pago Total es: {totalPag:.2f}" f"y la Comision incluida es de {comision:.2f}")


# ejercicio 3 / compra con descuento

totalCom = int(input("Digite el Total de la Compra "))
descuento = totalCom * 0.15
totalPag = totalCom - descuento
print(f"El Total de la compra con descuento es: {totalPag:.2f}")


# ejercicio 4 / promedio total de notas

examenFin = float(input("Ingrese la calificacion del Examen final"))
trabajoFin = float(input("Ingrese la calificacion del Trabajo final"))
nota1 = float(input("Digite el valor de la primera Nota "))
nota2 = float(input("Digite el valor de la segunda Nota "))
nota3 = float(input("Digite el valor de la tercera Nota "))
promedio = nota1 + nota2 + nota3 / 3
promedioPar = promedio * 0.55
promedioExa = examenFin * 0.30
promedioTra = trabajoFin * 0.15
notaFin = promedioPar + promedioExa + promedioTra
print(f"La calificacion final es: {notaFin:.2f}")


# ejercicio 5 / promedio de hombre y mujeres

numeroHom = int(input("digite la cantidad de hombres "))
numeroMuj = int(input("digite la cantidad de hombres "))
total = numeroHom + numeroMuj
promHom = numeroHom * 100/total
promMuj = numeroMuj * 100/total
print(f"El promedio de Hombes es: {promHom:.2f} y El promedio de mujeres es: {promMuj:.2f}")

# ejercicio 6 / calcular la edad

fechaNac = int(input("digite el Año de Nacimiento "))
fechaAct = int(input("digite el Año Actual "))
Edad = fechaAct - fechaNac
print(f"La edad de la persona es: ", Edad)
