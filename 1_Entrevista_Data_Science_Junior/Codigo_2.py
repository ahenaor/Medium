def busqueda_vector (n, vector):
    resultado = []
    contador = 0

    i = 0
    j = 0
    while i < len(vector):
        contador = contador + vector[i] 

        if contador < n:
            resultado.append(vector[i])

        elif contador > n:
            i = j
            j += 1
            resultado = []
            contador = 0
            
        else:
            resultado.append(vector[i])
            print(resultado)
            i = j
            j += 1
            resultado = []
            contador = 0

        i += 1

busqueda_vector(n, vector)

vector = [ 3, 5, 1, 8, 3, 2, 1, 7, 2, 4, 5, 8, 1]     
n = 10







