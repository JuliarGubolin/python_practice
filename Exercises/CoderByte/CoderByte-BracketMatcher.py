def BracketMatcher(strParam):

  stack = []
  count_open = 0
  count_close = 0
  for i in range(0, len(strParam)):
    if strParam[i] == '(':
      stack.append(strParam[i])
      count_open = count_open + 1
    elif strParam[i] == ')':
      count_close = count_close + 1
      if not len(stack) == 0:
        stack.pop()
      
  
  if len(stack) == 0 and count_open == count_close:
    #Certo
    return 1
  else:
    #Errado
    return 0

# keep this function call here 
print(BracketMatcher("(hello (world))"))