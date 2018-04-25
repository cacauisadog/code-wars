### Description:
# Given an array, find the int that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

import pdb

# run through array inserting array numbers into a dict containing the numbers and the number of times they show up;
# search through dict for the only odd value;
# finding it, return its key;
# if it doesn't find it, return None


def find_it(seq):
    count = {}
    for number in seq:
        count.setdefault(number, 0)
        count[number] += 1
    for key, value in count.items():
        if value % 2 != 0:
            return key
    return None


teste = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, -2]
print(find_it(teste))

# best solution on codewars:
# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i
