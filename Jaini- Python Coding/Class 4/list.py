#lists are something that helps you store lots of data
#it is written in the [square bracket]
#you can add or delete the data as you want in the list
a=[1, 2, 3, "orange", "purple"]
#it has a index value that starts with 0 and goes on as the data comes
print(a[4])
#slicing
print(a[1:])
print(a[:1])
#append(to add data at the end) and pop(to delete data from the end)
a.append("green")
print(a)
a.pop()
print(a)
#insert(to insert data at a specific position)
a.insert(3, "red")
print(a)
#sort(sorting the data) and reverse(reversing the order of the data)
b=[7, 9, 6, 10, 8]
b.sort()
b.reverse()
print(b)
#nesting(creating a list inside of another list)
one=["pink, purple, blue, green"]
two=[1, 5, 8, 3]
three=["apples, pears, grapes, bananas"]
list=[one, two, three]
print(list)