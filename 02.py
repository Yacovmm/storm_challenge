'''
{[()]} SIM
{[(])} NAO
{{[[(())]]}} SIM
'''


def isBalancedSequecy(sequency):

    # Declare opened bracket dict data
    brackets_dict = {"(" : ")", "{" : "}", "[" : "]", }

    # Declare our stakc
    stack = []

    # Loop through our sequecy
    for char in sequency:
        if char in brackets_dict.keys():
            stack.append(char)
        else:
            # Check if I have something in my stack
            if not stack:
                return False

            # Check if the current bracket closing with the last open one
            if char is not brackets_dict[stack[-1]]:
                return False
            stack.pop()
    
    # Check if remain any oppening bracket in my stack
    if stack:
        return False

    return True

 
print(isBalancedSequecy('{[()]}')) # SIM            
print(isBalancedSequecy('{[(])}')) # NAO            
print(isBalancedSequecy('{{[[(())]]}}')) # SIM            


    
    
