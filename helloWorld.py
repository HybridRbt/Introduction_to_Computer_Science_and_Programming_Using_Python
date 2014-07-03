# print 'I like 6.00.1x!'

# temp = '32'
# if temp > 85:
#   print "Hot"
#elif temp > 62:
#   print "Comfortable" 
#else:
#   print "Cold" 

#temp = 120
#if temp > 85:
#   print "Hot"
#elif temp > 100:
#   print "REALLY HOT!"
#elif temp > 60:
#   print "Comfortable" 
#else:
#   print "Cold"

#temp = 50
#if temp > 85:
#   print "Hot"
#elif temp > 100:
#   print "REALLY HOT!"
#elif temp > 60:
#   print "Comfortable"
#else:
#   print "Cold"

#varA = 'abc'
#if type(varA) == str:
#    print 'string'

#num = 0
#while num <= 5:
#    print num
#    num += 1
#
#print "Outside of loop"
#print num 

#num = 10
#while num > 3:
#    num -= 1
#    print num 

#num = 10
#while True:
#    if num < 7:
#        print 'Breaking out of loop'
#        break
#    print num
#    num -= 1
#print 'Outside of loop' 

#n = 2
#while n <= 10:
#    print n
#    n += 2
#    
#print "Goodbye!"

#print "Hello!"
#
#n = 10
#while n >= 2:
#    print n
#    n -= 2

#end = 6
#result = 0
#while end > 0:
#    result += end
#    end -= 1
#    
#print result

#greeting = 'Hello!'
#count = 0
#
#for letter in greeting:
#    count += 1
#    if count % 2 == 0:
#        print letter 
#    print letter
#
#print 'done'
#
#school = 'Massachusetts Institute of Technology'
#numVowels = 0
#numCons = 0
#
#for char in school:
#    if char == 'a' or char == 'e' or char == 'i' \
#       or char == 'o' or char == 'u':
#        numVowels += 1
#    elif char == 'o' or char == 'M':
#        print char
#    else:
#        numCons -= 1
#
#print 'numVowels is: ' + str(numVowels)
#print 'numCons is: ' + str(numCons) 

#num = 10
#for num in range(5):
#    print num
#print num 

#divisor = 2
#for num in range(0, 10, 2):
#    print num/divisor
#
#for variable in range(20):
#    if variable % 4 == 0:
#        print variable
#    if variable % 16 == 0:
#        print 'Foo!' 

#count = 0
#for letter in 'Snow!':
#    print 'Letter # ' + str(count) + ' is ' + str(letter)
#    count += 1
#    break
#print count 

#for num in range(2, 11, 2):    
#    print num
#
#print "Goodbye!"
#
#print "Hello!"
#
#for num in range(10, 0, -2):
#    print num
#
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) >= epsilon:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print 'failed'
#else:
#    print 'succeeded: ' + str(guess)

#x = 23
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while abs(guess**2-x) >= epsilon:
#    if guess <= x:
#        guess += step
#        print guess
#    else:
#        break
#
#if abs(guess**2 - x) >= epsilon:
#    print 'failed'
#else:
#    print 'succeeded: ' + str(guess)

#x = 12
#if x <= 10:
#   if x > 4:
#      print "One"
#   else:
#      print "Two"
#else:
#   if x >= 11:
#      print "Three"
#   else:
#      print "Four"

#abc = "With three words"
#stuff = abc.split()
#print len(stuff)

#stuff = ['joseph', 'sally', 'walter', 'tim']
#print stuff[2]
#
#st = "abc"
#ix  = int(st)
#
#lst = []
#lst.append(4)
#lst.append(10)
#lst.append(21)
#lst.append(6)
#print lst[2]

#tot = 0
#for i in range(5):
#    tot = tot + i
#print tot

#def hello():
#    print "Hello"
#    print "Fun"
# 
#hello()
#hello()
#
#stx = "hello there bob how are you"
#wds = stx.split()
#print wds[2]
#
# x = 12
# def g(x):
#     x = x + 1
#     def h(y):
#         return x + y
#     return h(6)
# g(x)


# def iterPower(base, exp):
#     if exp == 0:
#         return float(1)
#
#     result = 1
#     while exp > 0:
#         result *= base
#         exp -= 1
#
#     return float(result)
#
#
# print iterPower(-3.33, 8)

# def recurPowerNew(base, exp):
#     if exp == 0:
#         return float(1)
#
#     if exp > 0:
#         if exp % 2 == 0:
#             return recurPowerNew(base * base, exp / 2)
#         else:
#             return base * recurPowerNew(base, exp - 1)
#
#
# print recurPowerNew(9.41, 10)
#
# x = (1, 2, (3, 'John', 4), 'Hi')
# print x[0:-1]
# print x[0:1]
# print range(3)
# print sum(range(len([1, 2, [3, 'John', 4], 'Hi'])))

# aList = range(1, 6)
# bList = aList
# aList[2] = 'hello'
# print aList == bList
# print aList is bList

# cList = range(6, 1, -1)
# dList = []
# for num in cList:
#     dList.append(num)
# print cList == dList
# print cList is dList
#
# listA = [1, 4, 3, 0]
# listB = ['x', 'z', 't', 'q']
#
# print listA.sort()
# print listA
# listA.remove(3)
# print listA
#
# listB.sort()
# listB.pop()
# listB.count('a')
# # listB.remove('a')
# listA.extend([4, 1, 6, 3, 4])
# listA.count(4)
# listA.index(1)
# listA.pop(4)
# # listA.reverse()
# # print listA
#
# animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
# animals['d'] = 'donkey'
#
# print animals


def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    # Your Code Here
    current_largest = None
    current_key = None
    for each_key in aDict:
        if current_largest is None or current_largest < len(aDict[each_key]):
            current_largest = len(aDict[each_key])
            current_key = each_key

    return current_key

print biggest({'a': [16], 'c': [6, 15, 17, 8, 10, 19, 15, 9], 'b': [6, 14, 5, 15, 6, 20]})