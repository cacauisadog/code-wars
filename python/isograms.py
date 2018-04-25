# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    #check for empty string
    if not string:
        return True
    #transform string to lowercase, then check if any letters repeat. If they
    #do, returns False
    for letter in string:
        if string.lower().count(letter) > 1:
            return False
    return True

test1 = "Dermatoglyphics"
test2 = "isogram"
test3 = "moOse"
test4 = ""

print(is_isogram(test1))
print(is_isogram(test2))
print(is_isogram(test3))
print(is_isogram(test4))

#best solution on codewars:
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))



