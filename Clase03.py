import random
#en procceso falta terminar el punto 5
def agregar_matriz (matriz):
    bandera = 0
    while bandera == 0:
        Libro = input("Ingrese el nombre del libro: ")
        Libro = Slice(Libro, 15)#[:x]
        Codigo = input("Digite el código: ")
        Codigo = Slice(Codigo, 3)#[:x]
        Categoria = input("Ingrese el género del libro: ")
        Categoria = Slice(Categoria, 10)#[:x] == slice
            
        nuevo_valor = {
        "Libro" : Libro, 
        "Código" : Codigo,
        "Categoría" : Categoria 
        }
        matriz.append(nuevo_valor)#meto la {} adentro del diccionario
        
        confirmacion = input("Desea agregar otro valor? [y/n]")#rompe el while cambiando la flag
        if confirmacion in ["n", "N", "No", "NO", "no"]:
            bandera = 1
    return(matriz)

def agregar_matrizR(matriz):
    valor = int(input('ingrese la cantidad de libros q agregar: '))
    for v in range(valor):
        Libro = random.choice(['Zapa','Pinoccio','Sample', 'Dimitan'])
        Libro = Slice(Libro, 15)#[:x]
        Codigo = input("Digite el código: ")
        Codigo = Slice(Codigo, 3)#[:x]
        Categoria = random.choice(['Fantastico', 'Historia', 'Épico', 'Lirico', 'Ciencias'])
        Categoria = Slice(Categoria, 10)#[:x] == slice
        Puntuacion = random.choice(['10', '9', '8', '7', '6', '5','4','3','2','1'])
            
        nuevo_valor = {
        "Libro" : Libro, 
        "Código" : Codigo,
        "Categoría" : Categoria, 
        "Puntuación" : Puntuacion
        }
        matriz.append(nuevo_valor)#meto la {} adentro del diccionario
        
    return matriz
    

def Slice (Opcion, x): #limitas los caracteres antes del append
    if len(Opcion) > x:
        return Opcion[:x]
    else: 
        return Opcion

def Formato(item):# title(para la primera letra), upper(para toda la palabra)
    item["Libro"] = item.get("Libro").title()
    item["Categoría"] = item.get("Categoría").upper()
    return item

def ordenar_pri(matriz):
    matriz.sort(key = lambda x: (int(x["Código"])))# el x para que se ordene de manera ascendente
    matriz.reverse()# y esto lo pasa a descendente
    return matriz
def ordenar_sec(matriz):
    matriz.sort(key = lambda x: (x["Puntuación"]))# el x para que se ordene de manera ascendente

def mostrarbien(matriz):

    claves = matriz[0].keys() #para ubicar los valores claves
    
    encabezados = " | ".join(f"{clave:<25}" for clave in claves)#print encabezados de columna
    print(encabezados)
    print("-" * len(encabezados)) #linea para separar y el len para saber cuantos hacer

    # Imprimir filas de datos
    for fila in matriz:
        cadena = " | ".join(f"{fila.get(clave):<25}" for clave in claves)
        print(cadena)

matriz = [
    {
     "Libro" : "El Zar", "Código" : "001", "Categoría" : "Historia", "Puntuación" : "10"
    }
]# matriz base

value = input("Si desea agregar algún contenido confirme la acción y/n: ")
if value in ['y', 'yes', 'Y', 'YES', 'Yes' ]:
    agregar_matrizR(matriz)

ordenar_pri(matriz)
ordenar_sec(matriz)

for item in matriz:
    Formato(item)
mostrarbien(matriz)