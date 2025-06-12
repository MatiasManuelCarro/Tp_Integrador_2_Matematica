from datetime import date
# utilizamos datetime para consegui la fecha actual
fecha_actual = date.today()
# utilizamos la fecha_actual para conseguir el año
año_actual = fecha_actual.year
#años_nacimiento = [1975, 1986, 1987, 1992, 1993, 1996]
años_nacimiento = []
edad_integrantes = []
año_par = int(0)
año_impar = int(0)
grupo_z = True          #Comienza en True la funcion
hay_bisiesto = False
#cantidad_años = int(6)         #solo para testeo
cantidad_años = int(0)      #version que tiene que ir 
producto_cartesiano = []

def funcion_ingreso_años():
    global cantidad_años        #contador de la cantidad de años ingresados
    print("\n Ingrese los años de nacimiento de los integrantes del grupo, deben ser al menos dos\n para finalizar ingrese cualquier letra")
    año = input("Ingrese el año de nacimiento:\n")
    while año.isdigit():        #Verifica que se hayan ingresado numeros solamente
        año = int(año)  
        if año <= 2025:         #verifica si el año es menor o igual a 2025
            cantidad_años += 1
            años_nacimiento.append(año)         #se agrega a la lista de años
            año = input("Ingrese otro año:\n")
        else:
            año = input("Ingrese un año correcto:\n")
    print("Ingreso de años finalizado, volviendo al menu")
    menu()

#funcion que llama a todas las funciones de operaciones con los años
def funcion_operaciones_años():
    global años_nacimiento, grupo_z, hay_bisiesto, cantidad_años, año_par, año_impar, años_nacimiento, edad_integrantes, año_actual, producto_cartesiano
    for año in años_nacimiento:           #recorre la lista de años y las carga en las funciones
        año_par, año_impar = funcion_años_par_impar(año, año_par, año_impar)
        grupo_z = funcion_grupo_z(año, grupo_z)
        hay_bisiesto = funcion_es_bisiesto(año, hay_bisiesto)
    producto_cartesiano = funcion_producto_cartesiano()

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
    for año in años_nacimiento:
        for edad in edad_integrantes:
            producto_cartesiano.append((año, edad))
    
    #mostralos los productos
    print("\nLos productos cartesianos entre los años y las edades son:")
    for producto in producto_cartesiano:
        print(producto)



    
    

    
###
#def ingreso_automatico():
    #nombres_integrantes = ["GABRIEL", "GASPAR", "DIEGO", "HUGO", "MATIAS", "IGNACIO"]
    #dni_integrantes = [39352395, 32789456, 32020446, 31879389, 37362003, 25002007]
    
#    for i in range(0, 6):
#        funcion_operaciones_años(años_nacimiento[i])

    #print("Ingreso automatico de los integrantes del grupo:\n")
    #for i in range (0, 5):
    #    conj_dni(nombres_integrantes[i], dni_integrantes[i])
###

#for i in range(0,6):
#    año_par, año_impar = funcion_operaciones_años(años_nacimiento[i])
#    grupo_z = funcion_grupo_z(años_nacimiento[i])
#    hay_bisiesto = funcion_es_bisiesto(años_nacimiento[i])

# Menú con las distintas opciones para llamar a las diferenctes funciones.
def menu():
    corte = "S"
    opcion = "A"
    while opcion != corte:
        print("\n""# OPCIONES #")
        print("\n""A- Ingresar nombre y número de dni")
        print("B- Unión de conjuntos")
        print("C - Ingresar años de nacimiento")
        print("D - Operaciones con los años de los integrantes")
        print("E- Ingreso de datos automatico de los integrantes del grupo")
        print("S- Salir del programa")
    
    
        opcion = input(f"\n""Ingrese una opcion: ").upper()
    
        #if opcion == "A":
        #    conj_dni(ingresar_nombre(), ingresar_dni())  # Llamada a la función conj_dni que toma como argumentos los valores que devuelven las funciones ingresar_nombre e ingresar_dni

        #elif opcion == "B":
        #    union()

        if opcion == "C":
            funcion_ingreso_años()
            
        
        elif opcion == "D":
            funcion_operaciones_años()
        
        elif opcion == "P":
            funcion_producto_cartesiano()
        #elif opcion == "D":
        #    ingreso_automatico()

menu()