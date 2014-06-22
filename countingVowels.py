#s is provided by tutor
s = 'azcbobobegghakl'

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for each_char in s:
    if each_char in vowels:
        count += 1

print "Number of vowels: " + str(count)