# DESCRIPTION:
# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# My Solution

def solution_1(string):
    str = ""
    for i in range(len(string)-1, -1, -1):
        str += string[i]
    return str

def solution_2(string):
    return string[::-1]
