def QuestionsMarks(strParam):

  pair = 0
  count_question_marks = 0
  positions = []
  positions_2 = []
  for i, char in enumerate(strParam):
    if char.isdigit():
      positions.append(int(i))

  if len(positions) == 0:
    return False     

  for i in range(0, len(positions)-1):
    if int(strParam[positions[i]]) + int(strParam[positions[i+1]]) == 10:
      pair = pair + 1
      positions_2.append(positions[i])
      positions_2.append(positions[i+1])
  
  if pair == 0:
    return False
  
  for i in range(0, len(positions_2)-1):
   for j in range(positions_2[i]+1, positions_2[i+1]):
    if strParam[j] == '?':
      count_question_marks = count_question_marks + 1
   if count_question_marks == 3:
    pair = pair -1
    count_question_marks = 0

  if pair == 0:
    return True
  else:
    return False

# keep this function call here 
print(QuestionsMarks("ddqwdqw7??aaaaaaaaaaaaaaaaaaa??3???5"))