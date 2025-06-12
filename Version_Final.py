# Trabajo para la Semana de Integración II de Matemáticas.

# Grupo II: Matías Carro, Hugo Catalán; Gaspar Compagnucci, Gabriel Carbajal, Diego Carrizo e Ignacio Carné.

#### FUNCIONES ####

import os       #para limpiar la pantalla entre operaciones
from datetime import date       
# utilizamos datetime para consegui la fecha actual
fecha_actual = date.today()
# utilizamos la fecha_actual para conseguir el año
año_actual = fecha_actual.year

#Inicializacion de listas y variables 
años_nacimiento = []
edad_integrantes = []
año_par = int(0)
año_impar = int(0)
grupo_z = True          #Comienza en True la funcion
hay_bisiesto = False
cantidad_años = int(0)      
producto_cartesiano = []


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
        menu()          #vuelve al menu

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
    
def funcion_ingreso_años():
    global cantidad_años
    print("\n Ingrese los años de nacimiento de los integrantes del grupo, deben ser al menos dos\n para finalizar ingrese cualquier letra o simbolo")
    año = input("Ingrese el año de nacimiento:\n")
    while año.isdigit():        #Verifica que se hayan ingresado numeros solamente
        año = int(año)  
        if año <= 2025:         #verifica si el año es menor o igual a 2025
            cantidad_años += 1
            años_nacimiento.append(año)         #se agrega a la lista de años
            año = input("Ingrese otro año, recuerdo que para finalizar debe ingresar cualquier letra\n")
        else:
            año = input("Ingrese un año correcto:\n")
    #pausa antes de volver al menu
    input("Ingreso de años finalizado, presione enter para volver al menu")
    os.system('cls')        #Limpia la pantalla
    menu()


def funcion_años_par_impar(año, año_par, año_impar):        #Funcion que cuenta años pares e impares
    if año % 2 == 0:
        año_par += 1
    else:
        año_impar += 1
    return año_par, año_impar

def funcion_grupo_z(año, grupo_z):
    if año < 2000:      #si alguno de los años es menor a 2000, el grupo no es Z
        grupo_z = False     #Grupo z pasa a falso, esta variable inicia en True. Si uno solo es menor a 2000, pasa a falso
    return grupo_z

def funcion_es_bisiesto(año, hay_bisiesto):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):         #verifica que el año es bisiesto
        hay_bisiesto = True         #Si al menos un año es bisiesto, pasa a True     
    return hay_bisiesto

def funcion_producto_cartesiano(años_nacimiento, año_actual, edad_integrantes):
    #ordenamos la lista ingresada de años
    años_nacimiento.sort()         
    #calculamos la edad de los integrantes
    for año in años_nacimiento:
        edad_integrantes.append(año_actual - año)

    #mostramos las listas de años y edades
    print(f"La lista de años de nacimiento es: {años_nacimiento}")
    print(f"La lista de las edades de los integrantes es: {edad_integrantes}")
    
    #ciclo que genera los conjuntos cartesiano
    for año in años_nacimiento:
        for edad in edad_integrantes:
            producto_cartesiano.append((año, edad))
    
    #mostralos los productos
    print("\nLos productos cartesianos entre los años y las edades son:")
    for producto in producto_cartesiano:
        print(producto)

def funcion_operaciones_años(años_nacimiento, grupo_z, hay_bisiesto, año_par, año_impar, año_actual, edad_integrantes):
    for año in años_nacimiento:           #recorre la lista de años y las carga en las funciones
        año_par, año_impar = funcion_años_par_impar(año, año_par, año_impar)
        grupo_z = funcion_grupo_z(año, grupo_z)
        hay_bisiesto = funcion_es_bisiesto(año, hay_bisiesto)

    funcion_producto_cartesiano(años_nacimiento, año_actual, edad_integrantes)   #llama a la funcion de producto cartesiano

    #Devuelve los resultados
    print(f"\nEn el grupo tenemos {año_par} integrantes que nacieron en año par y {año_impar} integrantes que nacieron en año impar")
    if grupo_z:
        print(f"el Grupo es \"Grupo Z\" ")
    else:
        print(f"el Grupo No es \"Grupo Z\" ")
    if hay_bisiesto:
        print("Tenemos un año especial")
    #pausa antes de volver al menu    
    input("\nPresione enter para volver al menu...")
    os.system('cls')        #Limpia la pantalla
    menu()


def funcion_expresiones_logicas():

    # conjuntos de dígitos sin repetir para cada DNI
    A = {0, 2, 3, 4, 6}       # Diego
    B = {1, 3, 7, 8, 9}       # Hugo
    C = {0, 2, 3, 6, 7}       # Matías
    D = {0, 2, 5, 7}          # Ignacio
    E = {2, 3, 5, 9}          # Gabriel
    F = {0, 2, 3, 5, 7, 9}    # Gaspar

    print("Expresiones logicas\n")

    print("DNIs de los integrantes del grupo y conjuntos de digitos unicos: \n")

    print(f"Diego: 32020446, conjunto A {A}")         	
    print(f"Hugo: 31879389, conjunto B {B}")     	
    print(f"Matías: 37362003, conjunto C {C}")           	
    print(f"Ignacio: 25002007, conjunto D {D}")   
    print(f"Gabriel:  39352395, conjunto E{E}")                     
    print(f"Gaspar:  37050279, conjunto F {F}\n")  

    #Se crean listas de conjuntos y nombres para poder usar un bucle for.
    conjuntos = [A, B, C, D, E, F] 
    nombres = ['A', 'B', 'C', 'D', 'E', 'F']
    # Expresión 1: Todos tienen al menos el dígito 2 o 3
    print("Evaluando expresión 1: 'Todos los conjuntos contienen al menos el dígito 2 o el dígito 3.'\n")

    #Evaluamos si cada conjunto contiene 2 o 3.
    condiciones_digito2o3 = [(2 in conj or 3 in conj) for conj in conjuntos]

    #Muestra por pantalla si cada conjunto contiene un 2 o un 3.
    for nombre, conj, cumple in zip(nombres, conjuntos, condiciones_digito2o3):
        tiene = []
        if 2 in conj:
            tiene.append("2")
        if 3 in conj:
            tiene.append("3")
        descripcion = " y ".join(tiene) if tiene else "ninguno"
        print(f"Conjunto {nombre} contiene: {descripcion} → {'cumple' if cumple else 'NO cumple'}") # Indica si CUMPLE la condición.

    resultado1 = all(condiciones_digito2o3) 
    print("\n¿Todos contienen al menos 2 o 3?:", resultado1)#Devuelve True solo si todos los elementos de la lista son Verdadero.

    #----------------------------------------------------------------------------------------------------------------------------------

    # Expresión 2: Al menos un conjunto tiene más de 5 elementos

    print("\nEvaluando expresión 2: 'Al menos un conjunto contiene más de 5 elementos.'\n")

    #Creamos una lista con True o False, dependiendo si cada conjunto tiene más de 5 elementos.
    condiciones_mayor5 = [len(conj) > 5 for conj in conjuntos] 

    for nombre, conj, cumple in zip(nombres, conjuntos, condiciones_mayor5): #Muestra cuántos elementos tiene cada conjunto.
        print(f"Conjunto {nombre} tiene {len(conj)} elementos → {'cumple' if cumple else 'no cumple'}") #Indica si al menos uno tiene más de 5 dígitos. 

    resultado2 = any(condiciones_mayor5) 
    print("\n¿Al menos uno tiene más de 5 elementos?:", resultado2)
    #pausa antes de volver al menu
    input("\nIngreso de años finalizado, presione enter para volver al menu")
    os.system('cls')        #Limpia la pantalla
    menu()

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
        print("E - Ingresar años de nacimiento")
        print("F - Operaciones con los años de los integrantes")
        print("G - Mostrar evaluacion de condiciones logicas, con los DNIs de los integrantes del grupo")
        print("S- Salir del programa.")

        opcion = input("\n""Ingrese una opción A, B, C, D o S ( S para salir del programa): ").upper()

        if opcion == "A":
            os.system('cls')        #Limpia la pantalla 
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
        
        elif opcion == "E":
            os.system('cls')        #Limpia la pantalla 
            funcion_ingreso_años()
        
        elif opcion == "F":
            if cantidad_años >= 2:
                os.system('cls')        #Limpia la pantalla
                print("Mostrando operaciones con los años:")
                funcion_operaciones_años(años_nacimiento, grupo_z, hay_bisiesto, año_par, año_impar, año_actual, edad_integrantes)
            else:
                print("Por favor ingrese mas años para poder realizar las operaciones")
                print("Puede ingresarlas desde la opcion E")
                input("\nPresione enter para volver al menu...")
                os.system('cls')        #Limpia la pantalla
            
        elif opcion == "G":
            os.system('cls')        #Limpia la pantalla
            funcion_expresiones_logicas()

        elif opcion == "S":
            print("Cerrando programa")
            exit()

        else:
            print("Ingrese una opción válida.")

menu()
