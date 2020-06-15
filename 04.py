'''
Dados n inteiros não negativos representando um mapa de
elevação onde a largura de cada barra é 1, calcule quanta
água é capaz de reter após a chuva.
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

def findWater(lista): 
  
    # initialize our result 
    result = 0
       
    # max elevation on right and left sides 
    left_max = 0
    right_max = 0
       
    # indexes  
    lo = 0
    hi = len(lista)-1
       
    while(lo <= hi):  
        
        if(lista[lo] < lista[hi]): 
            # Verify if our left elevation
            if(lista[lo] > left_max): 
                # update left max elevation 
                left_max = lista[lo] 
            else: 
                # fill our result (left max elevation - current position)
                result += left_max - lista[lo] 
            lo+= 1
          
        else: 
            if(lista[hi] > right_max): 
                # update right max elevation 
                right_max = lista[hi] 
            else: 
                # fill our result (right max elevation - current right max position)
                result += right_max - lista[hi] 
            hi-= 1
          
    return result 

lista = [0,1,0,2,1,0,1,3,2,1,2,1]
print(find_qty_water(lista))
