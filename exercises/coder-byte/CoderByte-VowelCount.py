"""
Have the function VowelCount(str) take the str string parameter being 
passed and return the number of vowels the string contains (ie. "All cows eat grass 
and moo" would return 8). Do not count y as a vowel for this challenge. 
"""

def VowelCount(strParam):

  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  count_vowels = 0
  for char in strParam:
    if char in vowels:
      count_vowels = count_vowels + 1;
  # code goes here
  return count_vowels

# keep this function call here 
print(VowelCount(input()))