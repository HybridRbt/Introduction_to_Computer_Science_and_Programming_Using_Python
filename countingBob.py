__author__ = 'jeredyang'

#s = 'bdjgbobobobjoboboobobpphodo'

# convert s to be all lower case and setup counter
s = s.lower()
count = 0

# for every three characters check if a bob is in
for index in range(len(s)):
    temp_s = s[index: index + 3]
    if temp_s == "bob":
        count += 1

# print result
print "Number of times bob occurs is: " + str(count)