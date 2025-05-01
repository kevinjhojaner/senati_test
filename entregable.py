import numpy as np

# Función para pedir al usuario un vector validado (solo números enteros)
def obtener_vector(nombre):
    while True:
        try:
            valores = input(f"Ingrese los valores del vector {nombre} (solo números enteros) separados por espacios: ")
            vector = np.array([int(x) for x in valores.split()])  # Convertir a enteros
            if vector.size == 0:
                raise ValueError("El vector no puede estar vacío.")
            return vector
        except ValueError:
            print("Error: Asegúrese de ingresar SOLO números enteros separados por espacios. Intente nuevamente.")

# Función para pedir las dimensiones de una matriz validada
def obtener_dimensiones_matriz():
    while True:
        try:
            dimensiones = input("Ingrese el número de filas y columnas de la matriz (ejemplo: 3 3): ")
            filas, columnas = [int(x) for x in dimensiones.split()]
            if filas <= 0 or columnas <= 0:
                raise ValueError("Las dimensiones deben ser mayores que cero.")
            return filas, columnas
        except ValueError:
            print("Error: Ingrese dos números enteros positivos separados por un espacio. Intente nuevamente.")

# Generar matriz aleatoria con dimensiones dadas por el usuario
def generar_matriz():
    filas, columnas = obtener_dimensiones_matriz()
    matriz = np.random.randint(1, 10, (filas, columnas))
    print("\nMatriz generada:")
    print(matriz)
    return matriz

# Propiedad conmutativa (A + B = B + A)
def conmutativa_suma(vector1, vector2):
    return np.array_equal(vector1 + vector2, vector2 + vector1)

# Propiedad asociativa ((A + B) + C = A + (B + C))
def asociativa_suma(vector1, vector2, vector3):
    return np.array_equal((vector1 + vector2) + vector3, vector1 + (vector2 + vector3))

# Propiedad distributiva (A * (B + C) = A * B + A * C)
def distributiva(vector1, vector2, vector3):
    return np.array_equal(vector1 * (vector2 + vector3), (vector1 * vector2) + (vector1 * vector3))

# Inverso aditivo (A + (-A) = 0)
def inverso_aditivo(vector):
    return np.array_equal(vector + (-vector), np.zeros_like(vector))

# Identidad (A * I = A)
def identidad(vector):
    identidad_matriz = np.eye(len(vector))
    return np.array_equal(vector @ identidad_matriz, vector)

# Solicitar valores al usuario
vector_a = obtener_vector("A")
vector_b = obtener_vector("B")
vector_c = obtener_vector("C")
matriz = generar_matriz()

# Mostrar resultados
print("\nResultados de las propiedades aritméticas:")
print(f"Conmutativa de la suma: {conmutativa_suma(vector_a, vector_b)}")
print(f"Asociativa de la suma: {asociativa_suma(vector_a, vector_b, vector_c)}")
print(f"Distributiva: {distributiva(vector_a, vector_b, vector_c)}")
print(f"Inverso aditivo: {inverso_aditivo(vector_a)}")
print(f"Identidad: {identidad(vector_a)}")
