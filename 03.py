'''
https://leetcode.com/problems/trapping-rain-water/solution/
Input: [7,1,5,3,6,4]
Output: 5 (Comprou no dia 2 (preço
igual a 1) e vendeu no dia 5 (preço
igual a 6), lucro foi de 6 – 1 = 5
Input: [7,6,4,3,1]
Output: 0 (Nesse caso nenhuma
transação deve ser feita, lucro máximo
igual a 0)
'''

def findBestBuySell(lista):
    min_index=0 
    for i in range(1,len(lista)): 
        if lista[i] < lista[min_index]: 
            min_index = i

    # Verify if the minimum value is in the last day
    if min_index == len(lista) - 1:
        return None

    max_index = min_index + 1
    for i in range(max_index + 1, len(lista)):
        if lista[i] > lista[max_index]:
            max_index = i

    return [min_index, max_index]
    
lista =[7,6,4,3,1]
dias = findBestBuySell(lista)

if dias:
    total_profit = lista[dias[1]] - lista[dias[0]]
    print("Comprado no dia {} ao valor de {}, e vendido no dia {} ao valor de {}. Lucro total de {}".format(dias[0] + 1,
        lista[dias[0]], dias[1] +1, lista[dias[1]], total_profit))
else:
    print("Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0")






    
