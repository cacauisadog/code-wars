# Return the number(count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.

# for each letter in the string, check to see if it's in the vowels array. If True, num_vowels += 1
def getCount(inputStr):
    num_vowels = 0
    for letter in inputStr:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1

    return num_vowels

test = 'potato'
print(getCount(test))

# best solution on codewars:
# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")
