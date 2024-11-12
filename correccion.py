def crear_inicial():
    while True: 
        cantidad = int(input("Ingrese la cantidad de palabras: "))
        if cantidad > 0:
            break
        else:
            print("Ingrese nuevamente, debe ser mayor a 0")
    
    lista_p = []
    for i in range(cantidad):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        lista_p.append(palabra)
    return lista_p

lista_palabras = crear_inicial()

def contar_palabras(lista):
    p_contar = 0
    for i in lista:
        p_contar += 1
    return p_contar

contador = contar_palabras(lista_palabras)

def Eliminacion(lista_palabras):    
    while True:
        pregunta2 = input("Desea eliminar una palabra? S/N: ")
        if pregunta2 in ["S", "N"]:
            break
        else:
            print("Ingrese nuevamente, solo S o N")
                
    if pregunta2 == "N":
        print("Ok")
        return lista_palabras
    else:
        while True:
            num_palabras = int(input("Ingrese el número de palabras a eliminar: "))
            if 1 <= num_palabras < len(lista_palabras):
                break
            else:
                print("Ingrese nuevamente, debe ser mayor a 1 o menor a la cantidad de la lista")
            
    palabras_eliminar = []
    for i in range(num_palabras):
        palabra = input(f"Ingrese la palabra a eliminar {i+1}: ")
        palabras_eliminar.append(palabra)
        
    palabras_ei = lista_palabras.copy()  # Crear una copia para evitar modificar el original
    # Eliminar las palabras de la lista inicial
    for palabra_a_eliminar in palabras_eliminar:
        for i in range(len(palabras_ei) - 1, -1, -1):
            if palabras_ei[i] == palabra_a_eliminar:
                del palabras_ei[i]
    return palabras_ei

palabras_eliminadas = Eliminacion(lista_palabras)            
lista_inversa = lista_palabras[::-1]  # Crear la lista inversa

print(f"La lista de palabras creadas es: {lista_palabras}")     
print(f"El total de palabras es: {contador}") 
print(f"La lista de palabras aplicando eliminación es: {palabras_eliminadas}") 
print(f"La lista inversa es: {lista_inversa}")
