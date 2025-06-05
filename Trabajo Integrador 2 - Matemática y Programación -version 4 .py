
from datetime import date
# utilizamos datetime para consegui la fecha actual
fecha_actual = date.today()
año_actual = fecha_actual.year
#iniciamos las listas:
años_nacimiento = []
edad_integrantes = []
año_par = int(0)
año_impar = int(0)
grupo_z = True          #Comienza en True la funcion
hay_bisiesto = False
#cantidad_años = int(6)         #solo para testeo
cantidad_años = int(0)      #version que tiene que ir 
producto_cartesiano = []
edad = int(0)
contador_grupos = 0

#Se crea un diccionario vacio para los DNI
indices = ["A", "B", "C", "D", "E", "F"]
#diccionario_dnis = {indice: None for indice in indices}
diccionario_dnis = {}


def conjuntos_dni(numero): # Esta función toma los nombres y nros de DNI y los traasforma a ConjuntoA = {1, 2, 3, 4, 5, 6, 7, 8}, que es lo que pide la consigna.
    global contador_grupos, diccionario_dnis
    a = str(numero)
    conjunto = {int(i) for i in a} # Aquí se itera sobre la variable a que es un strig pero guarda el entero en el conjunto, sin repetir.
    clave = indices[contador_grupos]
    diccionario_dnis[clave] = conjunto
    contador_grupos += 1 # este contador está para que a partir de 2 se habiliten las operaciones, ya que debe haber por lo menos 2 conjuntos


#Esta funcion ingresa los datos de los integrantes del grupo de manera automatica
def ingreso_automatico():
    global años_nacimiento
    i = int(0)
    print("Ingreso automatico de los integrantes del grupo:\n")
    print("Integrantes del grupo:\n")
    print("DNI Diego: 32020446 - Año nacimiento 1986 ")        	
    print("DNI Hugo: 31879389 - Año nacimiento 1987")     	
    print("DNI Matias: 37362003 - Año nacimiento: 1993")         	
    print("DNI Ignacio: 25002007 - Año nacimiento: 1975")
    print("DNI Gabriel: 39352395 - Año nacimiento: 1996")                
    print("DNI Gaspar: 37050279 - Año nacimiento: 1992")

    #nombres_integrantes = ["Diego", "Hugo", "Matias", "Ignacio", "Gabriel", "Gaspar"]
    dni_integrantes = [32020446, 31879389, 37362003, 25002007, 39352395, 37050279]
    #años_nacimiento = [1975, 1986, 1987, 1992, 1993, 1996]
    print("\nConjuntos de los digitos unidos del DNI:\n")
    #ingreso de los datos: nombre y dni
    #carga todos los datos en la funcion de conjuntos
    for dni in dni_integrantes:
        conjuntos_dni(dni)

    print(diccionario_dnis)

    menu()



#def union(): # Funcion que dá el conjunto unión de todos los conjuntos
#    if cont >= 2: # Valida que haya 2 o mas conjuntos para hacer la operación
#        pass # Hacer la lógica
#    else:
#        print("No hay suficientes conjuntos para hacer la operación.")

#def ingresar_nombre(): # Función que pide el nombre de los integrantes del grupo II
#    nombre = input("\n""Ingrese su nombre: ").upper()
#    return nombre

def ingresar_dni(): # Esta función pide el número de DNI del integrante que ya ingresó su nombre
    numero_dni = input("\n""Ingrese su número de DNI: ")
    while len(numero_dni) != 8 or int(numero_dni) < 0: # Aquí se valida que el número tenga 8 cifras y que sea positivo
        print("El número ingresado no tiene 8 dígitos o es negativo")
        numero_dni = input("Ingrese su número de DNI: ")
    return numero_dni

#Aqui comienza la parte del programa que maneja las operacion con los años

def funcion_ingreso_años():
    global cantidad_años        #contador de la cantidad de años ingresados
    print("\n Ingrese los años de nacimiento de los integrantes del grupo, deben ser al menos dos\n para finalizar ingrese cualquier letra")
    año = input("Ingrese el año de nacimiento:\n")
    while año.isdigit():        #Verifica que se hayan ingresado numeros solamente
        año = int(año)  
        if año <= 2025:         #verifica si el año es menor o igual a 2025
            cantidad_años += 1
            años_nacimiento.append(año)         #se agrega a la lista de años
            año = input("Ingrese otro año, recuerdo que para finalizar debe ingresar cualquier letra\n")
        else:
            año = input("Ingrese un año correcto:\n")
    print("Ingreso de años finalizado, volviendo al menu")
    menu()

#funcion que llama a todas las funciones de operaciones con los años y muestra los resultados
def funcion_operaciones_años():
    global años_nacimiento, grupo_z, hay_bisiesto, cantidad_años, año_par, año_impar, años_nacimiento, edad_integrantes, año_actual, producto_cartesiano
    if len(años_nacimiento) < 2:
        print("No hay suficientes años ingresados para realizar las operaciones, por favor ingrese mas. \nvolviendo al menu")
        menu()
        
    for año in años_nacimiento:           #recorre la lista de años y las carga en las funciones
        año_par, año_impar = funcion_años_par_impar(año, año_par, año_impar)
        grupo_z = funcion_grupo_z(año, grupo_z)
        hay_bisiesto = funcion_es_bisiesto(año, hay_bisiesto)
    #llama a la funcion producto cartesiano
    producto_cartesiano = funcion_producto_cartesiano()

    #mostramos los resultados
    print(f"\nEn el grupo tenemos {año_par} integrantes que nacieron en año par y {año_impar} integrantes que nacieron en año impar")
    if grupo_z:
        print(f"el Grupo es \"Grupo Z\" ")
    else:
        print(f"el Grupo No es \"Grupo Z\" ")
    if hay_bisiesto:
        print("Tenemos un año especial")
    menu()

def funcion_años_par_impar(año, año_par, año_impar):
    if año % 2 == 0:
        año_par += 1
    else:
        año_impar += 1
    return año_par, año_impar

def funcion_grupo_z(año, grupo_z):
    if año < 2000:      #si alguno de los años es menor a 2000, el grupo no es Z
        grupo_z = False     #Grupo z pasa a falso
    return grupo_z

def funcion_es_bisiesto(año, hay_bisiesto):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):         #verifica que el año es bisiesto
        hay_bisiesto = True         #Si al menos un año es bisiesto, pasa a True     
    return hay_bisiesto

def funcion_producto_cartesiano():
    global años_nacimiento, año_actual, edad_integrantes
    #ordenamos la lista ingresada de años
    años_nacimiento.sort()         
    #calculamos la edad de los integrantes
    for año in años_nacimiento:
        edad_integrantes.append(año_actual - año)
    #mostramos las listas de años y edades
    print(f"La lista de años de nacimiento es: {años_nacimiento}")
    print(f"La lista de las edades de los integrantes es: {edad_integrantes}")    

    #ciclo que genera los conjuntos cartesiano
    producto_cartesiano = [] #vaciamos la variable para que se vuelva a cargar nuevamente los productos, si es que la funcion se corre de nuevo
    for año in años_nacimiento:
        for edad in edad_integrantes:
            producto_cartesiano.append((año, edad))
    
    #mostramos los productos cartesianos
    print("\nLos productos cartesianos entre los años y las edades son:")
    for producto in producto_cartesiano:
        print(producto)

def mostrar_operaciones(conj1, conj2):
    print(f"\nOperaciones entre conjuntos {conj1} y {conj2}:")
    print(f"Unión: {conj1 | conj2}")
    print(f"Intersección: {conj1 & conj2}")
    print(f"Diferencia  {conj1 - conj2}")
    print(f"Diferencia {conj2 - conj1}")
    print(f"Diferencia simétrica: {conj1 ^ conj2}")
    
#mostrar_operaciones(conjunto_digitos(dni1), conjunto_digitos(dni2))

#Funcion que vuelve todos los datos ingresados como al inicio
def funcion_eliminar_datos():
    global años_nacimiento, grupo_z, hay_bisiesto, cantidad_años, año_par, año_impar, años_nacimiento, edad_integrantes, producto_cartesiano
    años_nacimiento = []
    edad_integrantes = []
    producto_cartesiano = []
    grupo_z = True 
    hay_bisiesto = False
    año_par = 0
    año_impar = 0
    cantidad_años = 0

# Menú con las distintas opciones para llamar a las diferenctes funciones.
def menu():
    corte = "S"
    opcion = "A"
    while opcion != corte:
        print("\n""# OPCIONES #")
        print("\n""A - Ingresar nombre y número de dni")
        print("B - Unión de conjuntos")
        print("C - Ingresar años de nacimiento")
        print("D - Operaciones con los años de los integrantes")
        print("E - Ingreso de datos automatico de los integrantes del grupo")
        print("F - Eliminar todos los datos para comenzar de nuevo")
        print("S- Salir del programa")
    
    
        opcion = input(f"\n""Ingrese una opcion: ").upper()
    
        if opcion == "A":
            numero_dni = ingresar_dni()  # Llamada a la función conj_dni que toma como argumentos los valores que devuelven las funciones ingresar_nombre e ingresar_dni
            conjuntos_dni(numero_dni)
            print(diccionario_dnis)

        #elif opcion == "B":
            #union()      
        
        elif opcion == "C":
            funcion_ingreso_años()

        elif opcion == "D":
            funcion_operaciones_años()

        elif opcion == "E":
            ingreso_automatico()
        elif opcion == "F":
            funcion_eliminar_datos()
        
        elif opcion == "S":
            print("Cerrando programa")
            exit()

menu()