"""
Have the function CaesarCipher(str,num) 
take the str parameter and perform a Caesar 
Cipher shift on it using the num parameter as 
the shifting number. A Caesar Cipher works by 
shifting each letter in the string N places in 
the alphabet (in this case N will be num). 
Punctuation, spaces, and capitalization should 
remain intact. For example if the string is 
"Caesar Cipher" and num is 2 the output should 
be "Ecguct Ekrjgt".
Examples
Input: "Hello" & num = 4
Output: Lipps
Input: "abc" & num = 0
Output: abc 
"""

def CaesarCipher(strParam,num):

  concat = ''
  for char in strParam:
    if char.isalpha():
      
    concat = concat + char

  return strParam

# keep this function call here 
print(CaesarCipher("Hello"))