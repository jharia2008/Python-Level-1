#for loop is used to get the data from list, tuple, set, dictionaries
list1=(1, 3, 5, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29)
for num in list1:
    print(num)
#range is like creating a list but only when your data is in numbers and in one sequence
#creating a range function is like creating a list in alternating sequence
for num in list(range(1, 31, 2)): #the 1 and 31 are the range of the numbers and the 2 is what the numbers are counting by (ex. 1, 3, 5...)
    print(num)

#library is a prewritten code made by someone else which we can use in our code
import random
a=random.randint(1, 10)
print(a)
#randint is used to generate a random number 
import random
b=random.choices()
print(random.choices)