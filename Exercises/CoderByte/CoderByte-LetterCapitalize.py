def LetterCapitalize(strParam):

  splitted_words = strParam.split(' ')
  join_again = ''

  for word in splitted_words:
    aux = word[0].upper() + word[1:]
    join_again = join_again + aux + ' '
  return join_again

# keep this function call here 
print(LetterCapitalize("he3llo world a mied"))