# DESCRIPTION:
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

# My Solution

def descending_order_1(num):
    sorted_arr = sorted(list(str(num)), reverse=True)
    return int("".join(sorted_arr))

def descending_order_2(num):
    sorted_arr = int("".join(sorted(list(str(num)), reverse=True)))
