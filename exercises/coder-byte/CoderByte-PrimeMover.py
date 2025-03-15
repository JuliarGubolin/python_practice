"""
Prime Mover
Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4. 
For example: if num is 16 the output should be 53 as 53 is the 16th prime number.
Examples
Input: 9
Output: 23
Input: 100
Output: 541 

"""
import math

def prime_number(number_to_check):
    if(number_to_check == 2): return number_to_check
    elif(number_to_check <=1 or number_to_check % 2 == 0): return False
    else:
        i=0
        root = math.floor(math.sqrt(number_to_check))
        for i in range(3, root+1):
            if(number_to_check % i == 0):
                return False
    
    return number_to_check

def PrimeMover(num):
  j=0
  for i in range(2,10000):
      prime = prime_number(i)
      if prime != False:
        j = j + 1
        if j == num:
          return prime
          

# keep this function call here 
print(PrimeMover(741))