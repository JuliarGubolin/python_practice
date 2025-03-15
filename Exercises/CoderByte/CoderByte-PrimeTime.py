"""
Prime Time
Have the function PrimeTime(num) take the 
num parameter being passed and return the 
string true if the parameter is a prime number,
otherwise return the string false. The range 
will be between 1 and 2^16.
Examples
Input: 19
Output: true
Input: 110
Output: false 
"""

import math

def PrimeTime(num):

  if(num == 2): return True
  elif(num <=1 or num % 2 == 0): return False
  else:
    root = math.floor(math.sqrt(num))
    for i in range(3, root):
      if(num % i == 0):
        return False
    
  return True

print(PrimeTime(110))