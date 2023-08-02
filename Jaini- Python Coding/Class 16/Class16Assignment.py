print("To win this game, you must get a 6, but if you get 3 6's in a row, YOU LOSE.")
import random
a= random.randint(1,6)
b= random.randint(1,6)
c= random.randint(1,6)
print(a)
if a == 6:
    print("YOU WIN!")
    print(b)
elif b == 6:
    print("YOU WIN!")
    print(c)
elif c == 6:
    print("YOU WIN!")
elif a==6 and b==6 and c==6:
    print("YOU LOSE.")
else:
    print("YOU LOSE.")