def mas_larga(lg):
    palabra = ""
    largo = 0
    for i in lg:
        if len(i) > largo:
            palabra = i
            largo = len(i)
    return palabra

print("A) Calcular palabra mas larga")
print("")
op= input("Ingrese Opcion: ")
print("")

lista = []

if op == "A" or op == "a":
    largo = int(input("Ingrese largo de la lista"))
    print("")
    for i in range(largo):
        lista.append(input("Ingrese Palabra"))
        print("")
    print("La palabra mas larga es: ",mas_larga(lista))

for i in lista:
    invertido = i[::-1]
    print(invertido)
    
    






