#Find the missing letter

# Write a method that takes an array of consecutive(increasing) letters as 
# input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter 
# be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Iterate through each char in the string. If the next char's unicode is 
# different from the current char + 1, it means it's not the next in sequence.
# If so, returns that char.
def find_missing_letter(chars):
    for i in range(len(chars)):
        if ord(chars[i+1]) != ord(chars[i])+1:
            return chr(ord(chars[i])+1)


test1 = ['a', 'b', 'c', 'd', 'f']
test2 = ['O', 'Q', 'R', 'S']

print(find_missing_letter(test1))
print(find_missing_letter(test2))

# best solution from codewars (kinda meh):
# def find_missing_letter(chars):
#     n = 0
#     while ord(chars[n]) == ord(chars[n+1]) - 1:
#         n += 1
#     return chr(1+ord(chars[n]))
