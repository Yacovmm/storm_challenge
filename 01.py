'''
dado numero [2, 7, 11, 15], alvo  = 9
2+7 = 9
return [0, 1]
'''

lista = [2, 7, 4, 15, 5, 4] 
alvo = 9

def searchSumPair(lista, alvo):
    dic_aux = {} # Build a dic aux
    for index in range(len(lista)):
        if dic_aux and lista[index] in dic_aux.keys():
            # Building our return index list
            return [dic_aux[lista[index]], index]
        # Adding to the dic wich the key will be the difference of the alvo and the current list value 
        # and the value will be the list index            
        dic_aux[alvo - lista[index]] = index        
    return False

print(searchSumPair(lista, alvo))
