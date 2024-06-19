# DESCRIPTION:
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

# My Solution

def fake_bin_1(x):
  result = ''
  for i in range(len(x)):
    if int(x[i]) < 5:
      result += '0'
    else:
      result += '1'
  return result

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
