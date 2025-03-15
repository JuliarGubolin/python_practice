# Prime number check

import math


def prime_number(number_to_check):
    if(number_to_check == 2): return "It's prime"
    elif(number_to_check <=1 or number_to_check % 2 == 0): return "It's not a prime number"
    else:
        root = math.floor(math.sqrt(number_to_check))
        for i in range(3, root):
            if(number_to_check % i == 0):
                return "It's not a prime number"
    
    return "It's prime"

print(prime_number(9))