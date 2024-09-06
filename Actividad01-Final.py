import random
def mostrar_matriz(matriz):
    print(matriz)
    print('Alumno:', end=" ")
    print(materias[0], end = ' ')
    print(materias[1], end = ' ')
    print(materias[2], end = ' ')
    print(materias[3], end = ' ')
    cont= -1

    print()
    for j in range(4):
        
        if cont == -1:
            print(estudiantes[-1], end=" ")
            fila = matriz[0]
            print(fila)
                        
        if cont == 0:
            print(estudiantes[0], end=" ")
            fila = matriz[1]
            print(fila)
                
        if cont == 1:
            print(estudiantes[2], end=" ")
            fila = matriz[2]
            print(fila)
                
        if cont == 2:
            print(estudiantes[3], end=" ")
            fila = matriz[3]
            print(fila)
        cont += 1
            
def promedioAlumno(matriz, n):
    filas = n
    columnas = len(matriz[0])
    total_suma = 0
    
    for i in range(filas):
        total_suma = 0
        for j in range(columnas):
            total_suma += matriz[i][j]
        promedio = total_suma / columnas
        print('el estudiante', i + 1, 'cuenta con un promedio en sus materias de:', promedio)

def promedioMateria(matriz, m):
    columnas = m
    filas = len(matriz)
    elementos = 0
    for i in range(columnas):
        total_suma = 0
        for j in range(filas):
            total_suma += matriz[j][i]
            promedio = total_suma / filas
        print('la materia', i + 1, 'cuenta con un promedio en sus alumnos de:', promedio)


estudiantes = ['Lucas', 'Mateo', 'Nico', 'Felipe']
materias = ['Matematicas', 'Algebra', 'Programacion1', 'Colorimetria']

n = len(estudiantes)
m = len(materias)#el len es para q te de la cant de 'elementos' en la lista
matriz = []

for x in range(n):#filas
    matriz.append([])
    for j in range(m):
        calificaciones = random.randint(1,10)
        matriz[x].append(calificaciones)# j recorre los espacios vacios y el append los rellena con calificaciones

mostrar_matriz(matriz)
promedioAlumno(matriz,n)
promedioMateria(matriz,m)

