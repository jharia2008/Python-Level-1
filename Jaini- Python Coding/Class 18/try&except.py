#sometimes program might not work due to some errors which are not syntax errors, but some other different exception errors which might come
#to handle these types of errors we use try and except
#put of code you doubt and think will create a problem in try, try will try to execute the code and if it works its good, but if it doesn't work, it goes to except
#except will not remove the error instead whatever message is put in except will be displayed
#the only basic reason to use try and except is so errors aren't displayed and messages are displayed
try: 
    s= open("C:/Users/anish/OneDrive/Desktop/Jaini- Python Coding/Class 16/random.txt", "r")
    print(s.read())
except: 
    print("There has been an error in the code.")
else:
    print("This is the else part")
#else is excuted when the try part works, there is a finally keyword also which is used after except
#finally code will be excuted no matter if the error comes or not
finally:
    print("This is the finally part and will always be seen")