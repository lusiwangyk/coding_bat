# Return True if the string "cat" and "dog" appear the same number of times in the given string.


def cat_dog(str):
  cat_counter = 0
  dog_counter = 0
  for x in range(len(str)-2):
    if str[x] == "c" and str[x+1] == "a" and str[x+2] == "t":
      cat_counter += 1
    elif str[x] == "d" and str[x+1] == "o" and str[x+2] == "g":
      dog_counter += 1
  return cat_counter == dog_counter
