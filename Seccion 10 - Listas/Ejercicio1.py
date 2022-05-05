'''En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", 'Python', 3.14]
print(lista)

item1 = (input("Ingrese un valor: "))
item2 = (input("Ingrese otro valor: "))

lista[0] = item1
lista[1] = item2

print(lista)