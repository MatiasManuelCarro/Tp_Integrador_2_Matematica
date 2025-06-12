# conjuntos de dígitos sin repetir para cada DNI
A = {0, 2, 3, 4, 6}       # Diego
B = {1, 3, 7, 8, 9}       # Hugo
C = {0, 2, 3, 6, 7}       # Matías
D = {0, 2, 5, 7}          # Ignacio
E = {2, 3, 5, 9}          # Gabriel
F = {0, 2, 3, 5, 7, 9}    # Gaspar

print("DNIs y conjuntos ")

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