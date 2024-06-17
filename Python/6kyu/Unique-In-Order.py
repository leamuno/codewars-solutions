# DESCRIPTION:
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

# My Solution

def unique_in_order_1(sequence):
    result = []
    count = 0
    for element in sequence:
        if element not in result:
            result.append(element)
            count += 1
        elif element != result[count - 1]:
            result.append(element)
            count += 1
    return result

def unique_in_order_2(sequence):
    result = []
    prev = None
    for element in sequence:
        if element != prev:
            result.append(element)
            prev = element
    return result

def unique_in_order_3(sequence):
    result = []
    for element in sequence:
        if len(result) == 0 or element != result[-1]:
            result.append(element)
    return result
