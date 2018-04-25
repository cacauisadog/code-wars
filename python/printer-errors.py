# In a factory a printer prints labels for boxes. For one kind of boxes the 
# printer has to use colors which, for the sake of simplicity, are named with 
# letters from a to m.

# The colors used by the printer are recorded in a control string. For example 
# a "good" control string would be aaabbbbhaijjjm meaning that the printer used 
# three times color a, four times color b, one time color h then one time color 
# a...

# Sometimes there are problems: lack of colors, technical malfunction and a "
# bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

# You have to write a function printer_error which given a string will output 
# the error rate of the printer as a string representing a rational whose 
# numerator is the number of errors and the denominator the length of the 
# control string. Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters 
# from at o z.

# takes each letter in the string and checks if its unicode value is between
# n and z's unicode value and increments errors if it is. Returns a formatted
# string.
def printer_error(s):
    errors = 0
    for letter in s:
        if ord(letter) in range(ord('n'), ord('z')+1):
            errors += 1
    return (str(errors) + "/" + str(len(s)))


s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))

# best solution on codewars
# from re import sub
# def printer_error(s):
#     return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))
