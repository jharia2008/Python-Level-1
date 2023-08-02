password=input("enter a password")
num=2
while password!="bananas":
    if num== 0:
        print("too many attempts")
    else:
        print("wrong password")
        num=num-1