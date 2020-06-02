# - El enunciado era el siguiente: dado un vector numérico y un valor n, 
# - diseñar un algoritmo que devuelva un subvector de los números consecutivos cuya suma sea el número n.
 
def busqueda_vector (n, vector):
    resultado = []
    contador = 0

    for i in range(len(vector)):

        resultado = []
        contador = 0
        
        for j in range(i,len(vector)):

            if contador < n:
                contador = contador + vector[j]
                resultado.append(vector[j])
            
            elif contador > n:
                break
            
            else:
                print(resultado)
                break            

vector = [ 3, 5, 1, 8, 3, 2, 1, 7, 2, 4, 5, 8, 1]     
n = 10
busqueda_vector(n, vector)    
