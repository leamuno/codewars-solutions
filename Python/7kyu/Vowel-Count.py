# DESCRIPTION:
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

# My Solution

def get_count_1(sentence):
    count = 0
    for char in sentence:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            count += 1
    return count

def getCount(sentence):
    return sum(1 for char in sentence if char.lower() in "aeiou")
