# DESCRIPTION:
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!

# My Solution

def remove_every_other_1(my_list):
    result = []
    count = 1
    for element in my_list:
        if count % 2 != 0:
            result.append(element)
        count += 1
    return result

def remove_every_other_2(my_list):
    return my_list[::2]

def remove_every_other_3(my_list):
    del my_list[1::2]
    return my_list
