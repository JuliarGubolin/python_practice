"""
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then 
capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 
"""

def LetterChanges(strParam):

  vowels = ['a', 'e', 'i', 'o', 'u']
  number_space = '1234567890!@#$%&*()<>^;,+-[]~:?/ '
  new = strParam

  for i in range(0, len(strParam)):
    new_char = chr(ord(strParam[i])+1)
    if strParam[i] == 'z':
      new_char = 'a'
    if strParam[i]  not in list(number_space):
      new = new[:i] + new_char + new[i+1:]
  
  strParam = new
  for i in range(0, len(strParam)):
    if new[i] in vowels:
     strParam = strParam[:i] + strParam[i].upper() + strParam[i+1:]
  
  return strParam

# keep this function call here 
print(LetterChanges("beautiful^"))