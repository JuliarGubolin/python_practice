def LongestWord(sen):

  words_separately = []
  words_separately = sen.split(' ')
  dict_words_lenghts = {}

  for words in words_separately:
    if words.isalnum():
      lenght = len(words)
      if lenght not in dict_words_lenghts.keys():
          dict_words_lenghts[lenght] = words
  

  keys = list(dict_words_lenghts.keys())
  max_value = max(keys)
  sen = dict_words_lenghts.get(max_value) 

  return sen

# keep this function call here 
print(LongestWord("fun&!! time"))