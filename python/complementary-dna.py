# Deoxyribonucleic acid(DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more http: // en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA(string, except for Haskell)
# you need to get the other complementary side. DNA strand is never empty or there is no DNA at all(again, except for Haskell).

# DNA_strand("ATTGC")  # return "TAACG"

# DNA_strand("GTAT")  # return "CATA"


# Iterates through the string checking each letter and appends the complementary
# for it on the complementary_string. Returns the complementary_string.
def DNA_strand(dna):
    complementary_string = ''
    for letter in dna:
        if letter == 'A': 
            complementary_string += 'T'
        elif letter == 'T':
            complementary_string += 'A'
        elif letter == 'C':
            complementary_string += 'G'
        elif letter == 'G':
            complementary_string += 'C'
    return complementary_string


DNA_strand1 = "ATTGC"
DNA_strand2 = "GTAT"

print(DNA_strand(DNA_strand1))
print(DNA_strand(DNA_strand2))

#best solution on codewars:
# import string

# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG", "TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

#other interesting solution
# pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
# def DNA_strand(dna):
    #     return ''.join([pairs[x] for x in dna])
