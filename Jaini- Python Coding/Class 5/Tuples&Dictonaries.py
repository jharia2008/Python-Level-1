#tuple is used to store lot of data in (round bracket), but you can add or delete anything in a tuple, once created, its created
a=(1, 2, 3, "lions")
print(a)
#sort and reverse can be applied in tuple but not append and pop
b=list(a)
print(b)
b.append("tigers")
print(b)
c=tuple(b)
print(c)
#string, int, and float can be converted to each other, list, tuples, and sets can be converted to each other
#dictionaries store data/keys (keys mean the information of data)
d={
"name": "Jaini",
"money" : 3
}
print(d)
#there is no index value, if you want to get one or two values, you need to with the help of keys
print(d["money"])
print(d.values())
print(d.keys())
#sets have no index value, no position is given to the data, everytime we run the code, the position of the data will change randomly
j={5, 7, 2, "abcd", "efgh", False}
print(j)