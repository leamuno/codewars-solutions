# DESCRIPTION:
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

# My Solution

def add_binary(a,b):
    sum = a + b
    binary = ""
    count = 0
    while sum > 1:
        sum /= 2
        if sum >= 1:
            count += 1
    sum = a + b
    for i in reversed(range(count + 1)):
        sub = 2 ** i
        if sum - sub >= 0:
            binary += "1"
            sum -= sub
        else:
            binary += "0"
    return binary
