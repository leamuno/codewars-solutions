# DESCRIPTION:
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# My Solution

def reverse_words(text):
  words = text.split(" ")
  reverse = ""
  count = 0
  for word in words:
        if count == 0:
            r_word =""
            for c in word:
                r_word = c + r_word
            reverse += r_word
            count += 1
        else:
            r_word =""
            for c in word:
                r_word = c + r_word
            reverse += " " + r_word

  return reverse
