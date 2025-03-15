def RunLength(strParam):

  """dict_chars = {}
  concat = ''

  for char in strParam:
    count = strParam.count(char)
    dict_chars[char] = count

  for keys, values in dict_chars.items():
    concat = concat + str(values) + keys
  
  print(concat)
  return strParam"""
  """list_chars = []
  list_count = []
  j=0;i=0;k=0
  count = 0
  current = str()
  concat = ''

  while i <= len(strParam)-1:
    current = strParam[i]
    while strParam[j] == current:
      count = count + 1
      j = j+1
      if (j >= len(strParam)):
        break

    list_chars.append(current)
    list_count.append(count)
    count = 0
    i = j
    
  for k in range(0, len(list_chars)):
    concat = concat + str(list_count[k]) + list_chars[k]
  
  return concat"""
  list_tuples = []
  j=0;i=0;count = 0
  current = str()
  concat = ''
  tupla = tuple()

  while i <= len(strParam)-1:
    current = strParam[i]
    while strParam[j] == current:
      count = count + 1
      j = j+1
      if (j >= len(strParam)):
        break
    
    tupla = (current, count)
    list_tuples.append(tupla)
    count = 0
    i = j
    
  for item in list_tuples:
    concat = concat + str(item[1]) + item[0]
  
  return concat

print(RunLength("aabbcdeiia"))