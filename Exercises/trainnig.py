from collections import defaultdict
import operator
import numpy as np


"""""
def QuestionsMarks(strParam):

  count_question_marks = 0
  pair = 0
  digit = 0
  sum=0
  size = len(strParam)
  if size < 5:
    return False
  for i in range(0,size-1):
    if(strParam[size-1].isdigit and i == size-2):
        a = strParam[i]
        digit = digit+1
        sum = sum + int(strParam[size-1])
        if sum == 10:
            pair = pair+1
            sum = int(strParam[size-1])
    if(strParam[i].isdigit() and not strParam[i+1].isdigit()):
        digit = digit+1
        sum = sum + int(strParam[i])
        if sum == 10:
            pair = pair+1
            sum = int(strParam[i])

  number_question_marks = 3*(math.floor(pair/2))

  for i in range(0,size-1):
    if strParam[i].isdigit():
        j = i+1
        while (not (strParam[j].isdigit())):
            if(strParam[j] == '?'):
                count_question_marks = count_question_marks+1
            j = j+1
            if(j == size-1):
                break
            if strParam[j].isdigit() and (strParam[j].isdigit()+strParam[i].isdigit() != 10):
                count_question_marks = 0
                break
    if count_question_marks == 3:
            number_question_marks = number_question_marks-3
    if pair == 0:
        break
    #FIM FOR
  if number_question_marks == 0 and pair == 0:
    return True
  else:
    return False
    
# keep this function call here 
print(QuestionsMarks("acc?7??sss?3rr1??????5"))"""

"""def FirstFactorial(num):
    fat = num
    while num != 1:
        fat = fat * (num-1)
        num = num-1
    return fat

# keep this function call here 
print(FirstFactorial(4))"""

"""
def QuestionsMarks(strParam):

  size_param = len(strParam)
  positions_numbers = [0] * size_param
  question_marks_between = 0
  count = 0
  position_counter = 0
  numbers = [0] * size_param

  for i in range(0, size_param):
    if strParam[i].isdigit():
      numbers[count] = strParam[i]
      count = count+1
  
  print(numbers)

  for i in range(0, count-1):
    num1 = np.array(list(map(int, numbers[i])))
    num2 = np.array(list(map(int, numbers[i+1])))
    if num1 + num2 == 10:
      positions_numbers[position_counter] = numbers[i]
      position_counter = position_counter+1
      position_counter[position_counter] = numbers[i+1]
  
  if len(positions_numbers) == 0 or len(numbers) == 0 or len(strParam) < 5:
    return False
  else:
    position_numbers_parse = set(map(int, positions_numbers))
    j = 0
    size = len(position_numbers_parse)
    while(j != size-2):
      for i in range(position_numbers_parse[j], position_numbers_parse[j+1]):
        if(strParam[i] == "?"):
          question_marks_between = question_marks_between +1
      if(question_marks_between < 3 or question_marks_between > 3):
        return False
      j = j+1
    return True
    

# keep this function call here 
print(QuestionsMarks("aaa6???4"))"""


"""def LongestWord(sen):

  words = sen.split(' ')
  print(words)
  for word in words:


# keep this function call here 
print(LongestWord("I love dogs"))"""


"""
def QuestionsMarks(mystr):
  numbers_list = []
  for item,i in enumerate(mystr):
      if i.isdigit():
        numbers_list.append(int(item))
  
  ismatched = False
  for item,i in enumerate(numbers_list[:-1]):
      check = mystr[i:numbers_list[item+1]]
      aux = (numbers_list[item+1])
      no_of_question_marks = 0
      for char in check:
          if char == '?':
              no_of_question_marks = no_of_question_marks + 1
      if no_of_question_marks == 3:
          ismatched = True
  
    # code goes here 
  return ismatched
    
# keep this function call here  
print(QuestionsMarks("aaa6???4??3"))
"""
"""""
def QuestionsMarks(mystr):
  numbers_list = []
  for item,i in enumerate(mystr):
      if i.isdigit():
        numbers_list.append(int(item))
  
  size = len(numbers_list)
  ismatched = False
  for item,i in enumerate(numbers_list[:-1]):
      check = mystr[i:numbers_list[item+1]]
      no_of_question_marks = 0
      for char in check:
          if char == '?':
              no_of_question_marks = no_of_question_marks + 1
      if no_of_question_marks == 3:
          ismatched = True
  
    # code goes here 
  return ismatched
    
# keep this function call here  
print(QuestionsMarks("aaa6???4??3"))"""


## Data structures

# HashMap - Dictionaries: pair keys;values
# Useful: readability; O(1) runtimes, faster than arrays and lists
# How they work
# It works like an array, but in the array the key is pre-set
# Collision
# Key cannot be muttated

"""""ity_map = defaultdict(list)
cities = ["Rio de Janeiro", "São Paulo", "Brasilia"]
city_map["Brazil"] += cities"""

# Retrieve values: .keys(), .values(), .items()
# keys()
# values(): only de values
# items(): return a list of all things

"""strs = ["ate", "eat", "bat", "tab", "nat"]
#strs = [""]
anagram_map = {}
result = []
for s in strs:
  word = sorted(s)
  word2 = ''.join(word)
  if word2 not in anagram_map:
    anagram_map[word2] = []
    anagram_map[word2].append(s)
  elif word2 in anagram_map:
    anagram_map[word2].append(s)

for value in anagram_map.values():
  result.append(value)
  
print(result)
"""

"""
Min Window Substring
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, 
the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine 
the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest 
substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is 

aaddad
"aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all 
of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters. 
"""
#len(str1) == len(str2) and sorted(str1) == sorted(str2)

"""def MinWindowSubstring(strArr):

  characters_second_string = list(strArr[1])
  concat = ''
  dict_chars = {}
  j=0

  for i in range(0, len(strArr[0])):
    for j in range(0, len(characters_second_string)):
      if strArr[0][i] == characters_second_string[j]:
        dict_chars[i] = characters_second_string[j]
  
  for char in dict_chars.values():
    concat = concat + char

  size_concat = len(concat)
  size_string_2 = len(strArr[1])
  
  if(size_concat  == size_string_2):
    initial = list(dict_chars.keys())[list(dict_chars.values()).index(concat[0])]
    end = list(dict_chars.keys())[list(dict_chars.values()).index(concat[size_concat -1])]
    substring = strArr[0][initial: end]
    print(substring)
  
  j=1
  count_char=0
  for i in range(0, size_concat):
    position_concat = concat[i:(size_string_2-1)+j]
    sorted_array = sorted(strArr[1])
    if sorted(position_concat) == sorted_array:
      for k in range(0,i):
        if concat[k] == concat[i]:
          count_char = count_char + 1;

      return substring
    j = j+1

  return 0

# keep this function call here 
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))"""


"""
Letter Changes
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
Examples
Input: "hello*3"
Output: Ifmmp*3
Input: "fun times!"
Output: gvO Ujnft! 
"""
