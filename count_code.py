# Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.


def count_code(str):
  word_counter = 0
  for x in range(len(str)-3):
    if str[x] == "c" and str[x+1] == "o" and str[x+3] == "e":
      word_counter += 1
  return word_counter
