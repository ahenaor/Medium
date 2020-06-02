
def busqueda_vector (n, vector):
    resultado = []
    contador = 0
    for i in range(len(vector)):

        if contador < n:
            contador = contador + vector[i]
            resultado.append(vector[i])

        elif contador > n:
            resultado = []
            contador = vector[i]
        else:
            print(resultado)
            break 
        print(vector[i])
        print(contador)
        print("="*50)

vector = [ 3, 5, 1, 8, 3, 2, 1, 7, 2, 4, 5, 8, 1]     
n = 10    

busqueda_vector(n, vector)