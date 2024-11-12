"""Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero."""

def MesesAño():
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    salir = False
    while not salir:
        numero = int(input("Ingrese el número que desees: "))
        if numero == 0:
            salir = True
        else:
            if 1 <= numero <= len(meses):
                print(meses[numero - 1])
            else:
                print(f"Inserta un número entre 1 y {len(meses)}")



"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

def Fechas():
    meses = {
        "01": "Enero", "02": "Febrero", "03": "Marzo",
        "04": "Abril", "05": "Mayo", "06": "Junio",
        "07": "Julio", "08": "Agosto", "09": "Septiembre",
        "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
    }

    while True:
        fecha = input("Introduce la fecha en formato dd/mm/aaaa: ")
        
        try:
            dia, mes, año = fecha.split("/")
            
            # Verificar longitud de cada parte de la fecha
            if len(dia) != 2:
                print("Error: el día debe tener exactamente 2 dígitos.")
                continue
            
            if len(mes) != 2:
                print("Error: el mes debe tener exactamente 2 dígitos.")
                continue
            
            if len(año) != 4:
                print("Error: el año debe tener exactamente 4 dígitos.")
                continue
            
            # Verificar que el día y el año sean números válidos
            dia = int(dia)
            año = int(año)
            
            # Verificar rangos de día y mes
            if dia < 1 or dia > 31:
                print("Error: el día debe estar entre 01 y 31.")
                continue
            
            if mes not in meses:
                print("Error: el mes debe estar entre 01 y 12.")
                continue

            # Mostrar la fecha en el formato deseado
            print(f"{dia:02d} de {meses[mes]} de {año}")
            break  # Salir del bucle después de una entrada válida

        except ValueError:
            print("Error: el formato debe ser dd/mm/aaaa.")


"""1. Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
Spoiler
"""
def Multiplicacion():
    numero = int(input("Ingrese un número: "))
    tabla = []

    for i in range (1,11):
        tabla.append(numero * i)
        
    print(f"Resultado: {tabla}") 



"""2. pide una cadena por teclado, mete los caracteres en una lista sin espacios."""
def Caracter8():
    # Pedir una cadena al usuario
    cadena = input("Ingresa una cadena de palabras: ")
    # Crear la lista de caracteres sin espacios
    lista_caracteres = [caracter for caracter in cadena if caracter != " "]

    print("Lista de caracteres sin espacios:", lista_caracteres)


"""3. Crea una tupla con números e indica el numero con mayor valor y el que menor tenga."""
def MaxMin():
    tupla = (1, 4, 8, 7, 6, 2, 1, 9, 7)

    mayor = max(tupla)
    menor = min(tupla)

    print(f"El numero mayor es: {mayor} y en numero menor es: {menor}")


"""4. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite."""
def RepNumero():
    tupla2 = (1, 4, 8, 7, 6, 2, 1, 9, 7, 1, 4, 8, 7, 6, 2, 1, 9, 7)
    numero = int(input("Ingrese un numero: "))

    rep = tupla2.count(numero)

    print(f"El numero {numero} se repite {rep} veces en la tupla")


def Divisa():
    monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    while True:
        divisa = input('\nIntroduce una divisa: ').capitalize()
        if divisa in monedas:
            print(monedas[divisa])
            break
        else:
            print('Divisa no encontrada')



def JuegoPalabras():
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



"""Calcular el area de un triangilo A= b*h/2"""
def Areatriangulo():
    base= float(input("Ingrese la base del triangulo: "))
    altura= float(input("Ingrese la altura del triangulo: "))

    resultado = (base*altura)/2

    print("El resultado es: ", resultado)



""""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística 
les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.0
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un 
programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado. """   
def Jugueteria():
    PESO_P: float= 112
    PESO_M: float = 75

    cantidad_p = float(input("Ingrese la cantidad de payasos a enviar: "))
    cantidad_m = float(input("Ingrese la cantidad de muñecas a enviar: "))

    resultado = (PESO_P*cantidad_p) + (PESO_M*cantidad_m)
    conversion = resultado/1000

    print("El peso totl del envío es de: ", conversion, " kg")
    
    
"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos"""

def Cuentabancaria():
    dinero_inicial = float(input("Ingrese el la cantidad de dinero a depositar: "))

    INTERES_ANUAL: float = 0.04

    primer_a = round((dinero_inicial * INTERES_ANUAL) + dinero_inicial, 2)
    segundo_a = round((primer_a * INTERES_ANUAL) + primer_a, 2)
    tercer_a = round((segundo_a * INTERES_ANUAL) + segundo_a, 2)

    print("----------------------------------------------------------------------------")
    print("Ahorros al año 1: ", primer_a, "\n" "Ahorros al año 2: ", segundo_a, "\n" "Ahorros al año 3: ", tercer_a  )


"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales."""

def IMC():
    altura = float(input("Ingrese su altura en mts: "))
    peso = float(input("Ingrese su peso en kg: "))

    IMC = round(peso/(altura**2), 2)
    print("Tu índice de masa corporal es: ", IMC)

"""Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista"""


def ContPalabras():
    numero= int(input("Cantidad de palabras: "))
    
    if numero <1:
        print("Error, debe ingresar un número mayor a 0")
    else:
        lista=[]
        for i in range(numero):
            palabra=input("Ingrese la palabra: ")
            lista+= [palabra]
            
            print(f"Lista: {lista}")

def Diccionario():
    import string  
    palabras = {
        "carro": "car",
        "bicicleta": "bicycle",
        "camión": "truck",
        "tren": "train",
        "avión": "plane",
        "barco": "ship",
        "ciudad": "city",
        "montaña": "mountain",
        "río": "river",
        "lago": "lake",
        "playa": "beach",
        "jardín": "garden",
        "árbol": "tree",
        "flor": "flower",
        "camino": "road",
        "puente": "bridge",
        "escuela": "school",
        "universidad": "university",
        "hospital": "hospital",
        "hotel": "hotel",
        "tienda": "store",
        "mercado": "market",
        "restaurante": "restaurant",
        "cocina": "kitchen",
        "silla": "chair",
        "mesa": "table",
        "ventana": "window",
        "puerta": "door"
    }
    txt = input("Escriba la oración: ")
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    convert_Text = txt.lower().split()
    traduccion = []
    for index in convert_Text:
        traduccion.append(palabras.get(index, f"[{index} not found]"))
    print("Traducción:", " ".join(traduccion))



def exception():
    def excepcion():
        lista = [1, 5, 7, 8, 2, 4, 2]
        try:
            numeros = int(input("Ingrese un número para el índice: "))
            
            # Intentar acceder al índice
            print(f"El valor en el índice {numeros} es: {lista[numeros]}")
        
        except IndexError:
            # Índice fuera de rango
            print("El índice indicado es incorrecto, está fuera de rango.")
            print(f"La lista solo tiene {len(lista)} elementos, con índices del 0 al {len(lista) - 1}.")
        
        except ValueError:
            # Entrada no válida
            print("Debes ingresar un número válido.")
    
    excepcion()

def ListaExcept():
    def Ingreso(primer, verificar):
        try:
            if verificar in primer:
                raise ValueError(f"Error: No se permiten duplicados => [{verificar}]")
            primer.append(verificar)
        except ValueError as e:
            print(e)
    
    lista = [1, 2, 3, 4]
    while True:
        numero = int(input("Ingrese un número a agregar: "))
        Ingreso(lista, numero)
        print("Lista Nueva:", lista)
        repetir = input("¿Desea agregar otro valor? (s/n): ").lower()
        if repetir != "s":
            break
        print("------------------------------------------------------------")




def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Meses del año")
        print("2. Formato de fecha")
        print("3. Tabla de multiplicar")
        print("4. Lista de caracteres sin espacios")
        print("5. Máximo y mínimo en tupla")
        print("6. Repeticiones en una tupla")
        print("7. Símbolo de moneda")
        print("8. Juego de palabras")
        print("9. Área de un triángulo")
        print("10. Peso de un paquete (juguetería)")
        print("11. Ahorros bancarios")
        print("12. Índice de masa corporal (IMC)")
        print("13. Crear lista de palabras")
        print("14. Traducción de oraciones")
        print("15. Excepciones en listas")
        print("16. Excepciones con duplicados")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            MesesAño()
        elif opcion == "2":
            Fechas()
        elif opcion == "3":
            Multiplicacion()
        elif opcion == "4":
            Caracter8()
        elif opcion == "5":
            MaxMin()
        elif opcion == "6":
            RepNumero()
        elif opcion == "7":
            Divisa()
        elif opcion == "8":
            JuegoPalabras()
        elif opcion == "9":
            Areatriangulo()
        elif opcion == "10":
            Jugueteria()
        elif opcion == "11":
            Cuentabancaria()
        elif opcion == "12":
            IMC()
        elif opcion == "13":
            ContPalabras()
        elif opcion == "14":
            Diccionario()
        elif opcion == "15":
            exception()
        elif opcion == "16":
            ListaExcept()
        elif opcion == "0":
            print("Saliendo del programa... ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar el menú principal
menu()
