# DESCRIPTION:
# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

# My Solution

def find_needle(haystack):
    for needle in haystack:
        if needle == "needle":
            position = haystack.index("needle")
            text = "found the needle at position " + str(position)
            return text
