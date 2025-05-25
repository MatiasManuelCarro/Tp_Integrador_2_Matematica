
cont = 0
def conj_dni(nombre, nro): # Esta función toma los nombres y nros de DNI y los traasforma a ConjuntoA = {1, 2, 3, 4, 5, 6, 7, 8}, que es lo que pide la consigna.
    global cont 
    cont += 1 # este contador está para que a partir de 2 se habiliten las operaciones, ya que debe haber por lo menos 2 conjuntos
    a = str(nro)
    conjunto = {int(i) for i in a} # Aquí se itera sobre la variable a que es un strig pero guarda el entero en el conjunto, sin repetir.
    diccio = {"GABRIEL":"A", "GASPAR":"B", "DIEGO":"C", "HUGO":"D", "MATIAS":"E", "IGNACIO":"F" } # Diccionario que adigna una letra a cada nombre ingresado para que se cumpla ConjuntoA = ....
    # Aqui se hace una validació del nombre ingresado. El nombre ingresado debe pertenecer al grupo II.
    if nombre in diccio.keys():
        print(f"Conjunto {diccio[nombre]} = {conjunto}")
    else:
        print("Ingrese un nombre correcto")

#Esta funcion ingresa los datos de los integrantes del grupo de manera automatica
def ingreso_automatico():
    nombres_integrantes = ["GABRIEL", "GASPAR", "DIEGO", "HUGO", "MATIAS", "IGNACIO"]
    dni_integrantes = [39352395, 32789456, 32020446, 31879389, 37362003, 25002007]
    #año_nacimiento_integrantes = [] falta funcion que trabaje con los años
    print("Ingreso automatico de los integrantes del grupo:\n")
    for i in range (0, 5):
        conj_dni(nombres_integrantes[i], dni_integrantes[i])


def union(): # Funcion que dá el conjunto unión de todos los conjuntos
    if cont >= 2: # Valida que haya 2 o mas conjuntos para hacer la operación
        pass # Hacer la lógica
    else:
        print("No hay suficientes conjuntos para hacer la operación.")

def ingresar_nombre(): # Función que pide el nombre de los integrantes del grupo II
    nombre = input("\n""Ingrese su nombre: ").upper()
    return nombre

def ingresar_dni(): # Esta función pide el número de DNI del integrante que ya ingresó su nombre
    nro = input("\n""Ingrese su número de DNI: ")
    while len(nro) != 8 or int(nro) < 0: # Aquí se valida que el número tenga 8 cifras y que sea positivo
        print("El número ingresado no tiene 8 dígitos o es negativo")
        nro = input("Ingrese su número de DNI: ")
    return nro


# Menú con las distintas opciones para llamar a las diferenctes funciones.
def menu():
    corte = "S"
    opcion = "A"
    while opcion != corte:
        print("\n""# OPCIONES #")
        print("\n""A- Ingresar nombre y número de dni")
        print("B- Unión de conjuntos")
        print("C- Ingreso de datos automatico")
        print("S- Salir del programa")
    
    
        opcion = input(f"\n""Ingrese una opcion: ").upper()
    
        if opcion == "A":
            conj_dni(ingresar_nombre(), ingresar_dni())  # Llamada a la función conj_dni que toma como argumentos los valores que devuelven las funciones ingresar_nombre e ingresar_dni

        elif opcion == "B":
            union()

        elif opcion == "C":
            ingreso_automatico()
        
        
        

menu()