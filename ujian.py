# Nama: Rizky Prilian Dwicahya
# Job Connector Data Science - JCDS0804
# ------------------------------------
# Ujian Module 1 (Python)
# 11 Maret 2020
# ------------------------------------





# No.1
# 1. Create a function called Hashtag that generate hashtag which accepting string separated
# by space as presented in the below with following rules (15 Points):
# • It must start with a hashtag (#).
# • All words must have their first letter capitalized.
# • If the final result is longer than 140 chars it must return False.
# • If the input or the result is an empty string it must return False.

# ----- start

# def Hashtag(string):
#     # if string is an empty string, return False
#     if len(string)<1:
#         return False

#     # split the text by space and capitalize each words
#     splittedString = [word.capitalize() for word in string.split()]

#     # concatenate list into string
#     leHashtag = ''.join(splittedString)

#     # print(len(leHashtag))
#     # check if final string is longer than 140, return False
#     if len(leHashtag) > 140:
#         return False
#     # else, return the final string. append # to the front of the string
#     else:
#         return '#{}'.format(leHashtag)

# # Hashtag(" Hello there how are you doing") # would return "#HelloThereHowAreYouDoing"
# # Hashtag(" Hello World " ) #would return "#HelloWorld"
# # Hashtag("") # would return False

# testCases = [" Hello there how are you doing", " Hello World ","",'I love Python way of handling list but i hate the identation I love Python way of handling list but i hate the identation I love Python way of handling list but i hate the identation I love Python way of handling list but i hate the identation']
# # execute testCases
# print(list(map(Hashtag, testCases)))

# # --- end











# No.2
# Write a function that accepts a list of 10 integers (between 0 and 9), that returns a string
# of those numbers in the form of a phone number (10 points).
# output format: "(123) 456-7890"

# ---- start

# validateListOnlyInt = lambda inputList: False if len([x for x in inputList if type(x) != int]) > 0 else True
# validateListIntMinMax = lambda inputList, _min, _max: False if len([x for x in inputList if x < _min or x > _max]) > 0 else True

# def create_phone_number(number):
#     if len(number) != 10 or not validateListOnlyInt(number) or not validateListIntMinMax(number, 0, 9):
#         return False
#     else:
#         # this code below returns problem : Too many argument for format
#         # return '({}{}{}) {}{}{}-{}{}{}'.format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9])
#         prefix = '{}{}{}'.format(number[0],number[1],number[2])
#         phone1 = '{}{}{}'.format(number[3],number[4],number[5])
#         phone2 = '{}{}{}{}'.format(number[6],number[7],number[8],number[9])
#         return '({}) {}-{}'.format(prefix, phone1, phone2)

# testCases = [
#     [1,2,3,4,5,6,7,8,9,0],
#     [5,3,4,5],
#     [6,3,2,3,4,5,2,3,5,1],
#     ['6',4,2,3,'lalala',4,5,3,4,1],
#     [2,3,1,2,26,3,4,6,7,18]
# ]

# # execute testCases
# print(list(map(create_phone_number, testCases)))

# ---- end









# No.3
# You are given a list of integers. Your task is to sort odd numbers within the list in ascending
# order, and even numbers in descending order but keep all the odds or the evens number in
# the same index group (35 Points).
# Note that zero is an even number. If you have an empty list, you need to return it.
# Sort_odd_even([5, 3, 2, 8, 1, 4]) // would return [1, 3, 8, 4, 5, 2]

# odd numbers ascending: [1, 3, 5, ] ( Odds number in the index 0, 1, and 4)
# even numbers descending: [ 8, 4, 2] (Evens number in the index 2,3, and 5)


# ---------- start

# def bubbleSort(inputList, order='asc'): 
#     listLength = len(inputList)
#     # iterate sebanyak jumlah list
#     for i in range(listLength):
#         for j in range(0, listLength-i-1):
#             if order == 'asc':
#                 # ascending order
#                 # Tuker kalau angka sebelah kanan nya (j+1) lebih besar dari angka sebelumnya
#                 if inputList[j] > inputList[j+1] :
#                     inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
#             else:
#                 # descending order
#                 # Tuker kalau angka sebelah kanan nya (j+1) lebih kecil dari angka sebelumnya
#                 if inputList[j] < inputList[j+1] :
#                     inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
#     return inputList

# def sort_odd_even(listOfNum):
#     # before we do any sorting, we need to store all the original index location for both odd and even number
#     indexPosEven = [i for i, num in enumerate(listOfNum) if num%2 == 0 or num == 2]
#     indexPosOdd = [i for i, num in enumerate(listOfNum) if num%2 != 0]

#     # even numbers descending
#     evenNumbersSorted = bubbleSort(list(filter(lambda num: num%2 == 0 or num == 2, listOfNum)), order='desc')
#     # odd numbers ascending
#     oddNumbersSorted = bubbleSort(list(filter(lambda num: num%2 != 0, listOfNum)))

#     # create a mock up list first with same length as input list to avoid out of index error when replacing numbers position
#     sortedNum = [idx for idx in range(len(listOfNum))]

#     designatedNumbers = list(zip(indexPosEven, evenNumbersSorted)) + list(zip(indexPosOdd, oddNumbersSorted))
#     # print(designatedNumbers)
#     # print(len(designatedNumbers) == len(listOfNum))
    
#     for designatedPos, num in designatedNumbers:
#         # print(designatedPos, num)
#         sortedNum[designatedPos] = num

#     return sortedNum


# testCases = [
#     [5,3,2,8,1,4],
#     [9,6,8,4,7,2,1,6,2,3]
# ]

# # execute code
# print(list(map(sort_odd_even, testCases)))

# ---------- end










# No.4
# Create a function hollowTriangle(height) that returns a hollow triangle of the correct
# height or level. (40 Points)


# -------start
from math import floor
def hollowTriangle(rowHeight):
    z = ''
    if rowHeight < 1:
        z = ''
    elif rowHeight == 1:
        z = '#'
    else:

        # there is a pattern for the bottom part of the triangle
        # this number will determine the max width of each row
        # row height -> max row width
        # 2->3, 3->5, 4->7, 5->9, 6->11
        # if row number is n, the math formula of nth row is 2n-1
        
        # maxRowWidth will returns odd numbers
        maxRowWidth = (2*rowHeight) - 1

        # the first row will be all _'s with one # at the center
        z += ('_'*int(floor(maxRowWidth/2))) + '#' + ('_'*int(floor(maxRowWidth/2)))
        z += '\n'

        # middle rows on rowHeight more than two
        # if rowHeight = 3, there are 1 midrow, for rowHeight 4, there is 2 midrow
        if rowHeight > 2:
            for midRowNum in range(0,rowHeight - 2):

                # center underscores (the hollow part) pattern is sequence of odd numbers
                # 1,3,5,7,9,11
                # 2n+1
                numOfCenterUnderscores = (2*midRowNum) + 1

                # the centerunderscores will be in between two #
                # since we know the maxRowWidth, we can know the number of outside _
                numOfOutsideUnderscores = int(floor((maxRowWidth - (numOfCenterUnderscores + 2)) / 2))

                # next we print the middle rows
                z += ('_'*numOfOutsideUnderscores) + '#' + ('_'*numOfCenterUnderscores) + '#' + ('_'*numOfOutsideUnderscores)
                z += '\n'

        # the last row will consists of all #'s with the width of maxRowWidth
        z += '#'*maxRowWidth

    return z

testCases = [x for x in range(1,11)]

# execute codes
for test in testCases:
    print('row num: {}\n'.format(test))
    print(hollowTriangle(test))
    print('\n')

# -----end