"""
Have the function Division(num1,num2) take both parameters being passed and return the Greatest Common Factor. 
That is, return the greatest number that evenly goes into both numbers with no remainder. For example: 
12 and 16 both are divisible by 1, 2, and 4 so the output should be 4. The range for both parameters will be from 1 to 10^3.
Examples
Input: 7 & num2 = 3
Output: 1
Input: 36 & num2 = 54
Output: 18 
"""

def Division(num1,num2):

  list_num1 = []
  list_num2 = []

  menor = min(num1, num2)

  if menor == 1:
    return 1

  for i in range(1, menor+1):
    if num1 % i == 0:
      list_num1.append(i)
    if num2 % i == 0:
      list_num2.append(i)
  
  conj_1 = set(list_num1)
  conj_2 = set(list_num2)

  iguais = conj_1 & conj_2
  maior = max(iguais)
  return str(maior)

  """if len(maior_lista) == len(menor_lista) and len(maior_lista) == 1:
      return maior_lista[0]
  
  list_num1.reverse()
  list_num2.reverse()
  for i in range(0, min(len(list_num1), len(list_num2))):
    num_current = list_num1[i]
    if num_current in list_num2:
      return num_current"""
                 
  
# keep this function call here 
print(Division(100, 50))