def FindIntersection(strArr):

  first_string = list(map(int, strArr[0].split(',')))
  last_string = list(map(int, strArr[1].split(',')))
  result = list(set(first_string).intersection(last_string))
  result.sort()
  if not result:
    return False
  return result
  

# keep this function call here 
input = ["1, 3, 77, 11, 17, 18", "13, 4, 9, 10"]
print(FindIntersection(input))