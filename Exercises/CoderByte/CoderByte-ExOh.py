def ExOh(strParam):
  
  x_count = 0
  o_count = 0

  for char in strParam:
    if char == 'x' or char == 'X':
      x_count = x_count + 1
    elif char == 'o' or char == 'O':
      o_count = o_count + 1
          
  return x_count == o_count

# keep this function call here 
print(ExOh("x"))