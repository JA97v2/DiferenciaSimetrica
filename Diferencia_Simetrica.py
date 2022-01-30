from __future__ import annotations

''' 
Definir función que realice diferencia simétrica
'''
def dif_simetrica(conjunto1, conjunto2) -> list:
    resultado = []                          # Lista vacía para almacenar resultado
    for item in conjunto1:                  # Iterar por cada item del conjunto1
        if item not in conjunto2:           # Verificar si el item no existe en el conjunto2
            if item not in resultado:       # Verificar si el item no existe en el resultado
                resultado.append(item)      # Agregar item al resultado

    for item in conjunto2:                  # Iterar por cada item del conjunto2
        if item not in conjunto1:           # Verificar si el item no existe en el conjunto1
            if item not in resultado:       # Verificar si el item no existe en el resultado
                resultado.append(item)      # Agregar item al resultado

    return resultado                        # Retornar el resultado

'''
Definir función que realice la diferencia simétrica en todos los conjuntos ingresados
(condiciones 1 y 2)
'''
def op_conjuntos(*args) -> list:
    '''
    La diferencia es una operación binaria, si hay mas de 2 conjuntos se debe operar el
    resultado de esta operación con el siguiente conjunto, al asignar el primer conjunto
    de los argumentos de la función como resultado, se crea la lógica de operar el 
    resultado con el conjunto adyacente a los 2 conjuntos operados
    '''
    resultado = args[0]                                 # Lista para almacenar resultado
    for i in range(1, len(args)):                       # Iterar por cada conjunto ingresado
        resultado = dif_simetrica(resultado, args[i])   # Actualizar la lista de resultado
    resultado.sort()                                    # Organizar lista en orden ascendente
    return resultado                                    # Retornar resultado
        

def main():
    print(op_conjuntos([1, 2, 3], [5, 2, 1, 4]))

if __name__ == '__main__':
    main()