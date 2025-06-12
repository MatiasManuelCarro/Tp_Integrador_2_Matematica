#Poniendo En Orden

# Trabajo para la Semana de Integración II de Matemáticas.

# Grupo II: Matías Carro, Hugo Catalán; Gaspar Compagnucci, Gabriel Carbajal, Diego Carrizo e Ignacio Carné.

#### FUNCIONES ####

import os       #para limpiar la pantalla entre operaciones


def conj_dni(nro): # Funcion que toma el número que devuelve ingresar_dni() y genera los conjuntos con los digitos de cada DNI:
    letras = ["A","B","C","D","E","F"] # Lista de letas para el nombre de cada conjunto.
    numero_string = str(nro)
    conjunto = {int(i) for i in numero_string} # Aquí se itera sobre la variable a, que es un strig, pero guarda el entero en el conjunto, sin repetir.
    print(f"Conjunto {letras[suma]} = {conjunto}")



#funcion para obtener el conjunto de digitos unicos de un DNI
def conjunto_digitos(dni):
    conjunto = set()
    for digito in dni:
        if digito.isdigit():  # Verifica si el carácter es un dígito
            conjunto.add(digito)
    return conjunto  # Devuelve el conjunto de dígitos únicos

#funcion para mosotrar operaciones entre conjuntos
def mostrar_operaciones(conj1, conj2):
    print(f"\nOperaciones entre conjuntos: Conjunto A = {conj1} y Conjunto B = {conj2}:")
    print(f"Unión: {conj1 | conj2}")
    print(f"Intersección: {conj1 & conj2}")
    print(f"Diferencia  {conj1 - conj2}")
    print(f"Diferencia {conj2 - conj1}")
    print(f"Diferencia simétrica: {conj1 ^ conj2}")

    #pausa, vuelve al menu presionando enter
    input("\nPresione enter para volver al menu...")
    os.system('cls')        #Limpia la pantalla


def ingresar_dni(): # Esta función pide que se ingrese el numero de dni y verifica el ingreso correcto
    print("\nIngrese numero de Dni, para Salir, ingrese \"S\"")
    nro = input("\n""Ingrese su número de DNI: ")
    if str(nro).upper() == "S":      #Si se ingresa "S" se frena el ingreso y vuelve al menu
        os.system('cls')        #se limpia la pantalla
        menu()

    while len(nro) != 8 or int(nro) < 0: # Aquí se valida que el número tenga 8 cifras y que sea positivo
        print("El número ingresado no tiene 8 dígitos o es negativo")
        nro = input("Ingrese su número de DNI o \"S\" para salir:\n")
        if str(nro).upper() == "S":      #Si se ingresa "S" se frena el ingreso y vuelve al menu
            os.system('cls')        #se limpia la pantalla
            menu()
    return nro


# Función para formar los conjuntos a partir de los números de DNI
def conjunto_digitos(dni):
    conjunto = set()
    for digito in dni:
        if digito.isdigit():  # Verifica si el carácter es un dígito
            conjunto.add(digito)
    return conjunto  # Devuelve el conjunto de dígitos únicos


# Función suma las veces que un dígito aparece en un DNI y los muestra por consola.
def contador_cifras(): # Función que cuenta las veces que un dígito aparece en un número en un DNI.
    dni = input("\n""Ingrese el número de DNI: ")
    while len(dni) != 8 or int(dni) < 0: # Aquí se valida que el número tenga 8 cifras y que sea positivo
        print("El número ingresado no tiene 8 dígitos o es negativo")
        dni = input("Ingrese su número de DNI: ")

    print(f"En el DNI {dni}: ")
    for i in range(10):  #se itera de 0 a 9
        numero = i
        contador = str(dni).count(str(i)) #cuenta cuantas veces i se encuentra dentro del string DNI, se guarda en contador
        if contador > 1:
            print(f" el numero {numero} esta {contador} veces")
        elif contador == 1:
            print(f" el numero {numero} esta {contador} vez")
    #pausa, vuelve al menu presionando enter
    input("\nPresione enter para volver al menu...")
    os.system('cls')        #Limpia la pantalla


# Función recursiva que suma números que forman el DNI y muestra el resultado por pantalla.
def suma_digitos(lista_dni):
    if len(lista_dni) == 0: # Caso base
        return 0
    else:
        return lista_dni[0] + suma_digitos(lista_dni[1:]) #Retorna un valor mas un llamado a sí misma con una lista de longitud menor.

# MENU #
lista_conjuntos = []

def menu():
    salida = "S"
    opcion = "A"

    while opcion != salida:

        print("\n""# OPCIONES #")
        print("A- Ingreso de DNIs y generación de conjuntos de dígitos únicos.")
        print("B- Mostrar operaciones con conjuntos.")
        print("C- Mostrar cuántas veces aparece un número en un DNI.")
        print("D- Mostrar la suma de los números que forman de DNI.")
        print("S- Salir del programa.")

        opcion = input("\n""Ingrese una opción A, B, C, D o S ( S para salir del programa): ").upper()

        if opcion == "A":
            print("Generación de conjuntos de dígitos únicos")
            global suma
            suma = 1
            while suma < 7:
                conj_dni(ingresar_dni())
                suma += 1
            
        elif opcion == "B":
            print("\nIngrese un par de DNIs para realizar las operaciones con conjuntos")
            print("Ingrese el primer DNI:")
            dni1 = ingresar_dni()
            print("Conjunto A = ", conjunto_digitos(dni1)) # Muestra el conjunto de dígitos únicos del primer DNI.
            print("Ingrese el segundo DNI:")
            dni2 = ingresar_dni()
            print("Conjunto B = ", conjunto_digitos(dni2))  # Muestra el conjunto de dígitos únicos del segundo DNI."""
            mostrar_operaciones(conjunto_digitos(dni1), conjunto_digitos(dni2)) # Composisión de funciones. Se llama a la funcion mostrar_operaciones que toma como argumento lo que devuelve la funcione conjunto_digitos(dni).
        
        elif opcion == "C": 
            contador_cifras() # Llamada a la función contador_cifras().

        elif opcion == "D":
            print("suma de los números que forman de DNI")
            dni = ingresar_dni()
            lista_dni = [int(i) for i in dni]
            print(f"La suma de los dígitos del DNI ingresado es: {suma_digitos(lista_dni)}")  # Llamada a la funcion suma_digitos().
            #pausa, vuelve al menu presionando enter
            input("\nPresione enter para volver al menu...")
            os.system('cls')        #Limpia la pantalla

        elif opcion == "S":
            print("Cerrando programa")
            opcion == salida

        else:
            print("Ingrese una opción válida.")

menu()
