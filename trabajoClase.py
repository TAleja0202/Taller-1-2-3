#primer ejemplo

lista1 = [1, 2, 3, 4, "hola", 2, 2]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, "listo", 9, 2]
conjunto = set(lista1)
conjunto = set(lista2)
lista1 = list(conjunto)
print(conjunto)

#segundo ejemplo

class persona():
    nombre = "felipe"
    apellido = "rivera cardenas"
    pass
persona1 = persona()
print(f"el nombre de la persona es: {persona1.nombre}  y su apellidos son: {persona1.apellido}")




