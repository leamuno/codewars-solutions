# DESCRIPTION:
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# My Solution

def solution_1(text, ending):
    start = len(text) - len(ending)
    return((False, True) [text[start:] == ending])

def solution_2(string, ending):
    return string.endswith(ending)
