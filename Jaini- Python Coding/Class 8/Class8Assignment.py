#reversing a number
a="5 15 1349 over"
s=(a[:9])
string=print()
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = ""
 
print("The original string is : ", end="5 15 1349")
print(s)
 
print("The reversed string(using loops) is : ", end="5 51 9431")
print(reverse(s))