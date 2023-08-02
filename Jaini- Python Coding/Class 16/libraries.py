#counter function is used to count the number of items
from collections import * 
a= [1, 5, 2, 1, 5, 5]
print(Counter(a))
#OrderedDict remembers the order of the keys in which they are inserted
d={}
d["apple"]= 2
d["orange"]= 1
a=OrderedDict()
a["apple"]= 2
a["orange"]= 1
for key, value in a.items():
    print(key, value)
#deque can append or pop from both sides: the left side and the right side
q= deque([2, 4, 8, 1, 5])
q.append(4)
q.appendleft(4)
print(q)
import datetime
print()
#libraries means a pre-written code by someone else which other people can use in their own code to save their time
#example- if a person needs a function or feature which they want to use in their code, if that function is already there in the library, then it csn be used from their instead of creating it again
#libraries have differnt types of functions, classes, etc. which other people can use