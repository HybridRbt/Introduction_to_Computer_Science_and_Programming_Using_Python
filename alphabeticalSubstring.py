__author__ = 'jeredyang'
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example,
if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'jbctikjsbils'

# setup substring and length count
substring = ""
current_length = 0

# for each char from s[0] to s[-1]
for substring_start in range(len(s) - 1):
    temp_sub = s[substring_start]
    # check every char after it to s[-1]
    for substring_end in range(substring_start + 1, len(s)):
        # if there's a reversed char, note the length of temp sub, if longer than current length, write to substring
        # and then break
        if s[substring_end] < s[substring_end - 1]:
            if current_length < len(temp_sub):
                current_length = len(temp_sub)
                substring = temp_sub
                break
            else:
                break
        else:
            temp_sub += s[substring_end]
            if current_length < len(temp_sub):
                current_length = len(temp_sub)
                substring = temp_sub

print "Longest substring in alphabetical order is: " + substring
