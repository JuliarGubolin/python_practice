def NearestSmallerValues(arr):

  size_arr = len(arr)
  arr_answers = []
  count = 0
  concat = ''
  for i in range(0,size_arr):
    if i == 0:
      arr_answers.append(-1)
    else:
      for j in range(i-1, -1, -1):
        count = 0
        x = arr[j]
        y = arr[i]
        if x <= y:
          arr_answers.append(arr[j])
          count = count + 1
          break
      if count == 0:
        arr_answers.append(-1)
       
  for numbers in arr_answers:
    concat = concat + str(numbers) + ' '
  return concat


print(NearestSmallerValues([5, 2, 8, 3, 9, 12]))