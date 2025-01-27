""" QUESTION
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string fal
"""

def CodelandUsernameValidation(strParam):

  size = len(strParam)
  special_characters = "!@#$%^&*()-+?=,<>/.';"

  if(size < 4 or size > 25): return False
  elif(strParam[0].isalpha() == False or strParam.endswith("_")): return False
  elif any(c in special_characters for c in strParam): return False
  else:
    return True

# keep this function call here 
print(CodelandUsernameValidation("huewfbweubcewubceuivbuiervbuirevbuier"))