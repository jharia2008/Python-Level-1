#datetime library have all the functions related to date and time
import datetime
#datetime.now used to find out the current date and time
x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.date)
#strfttime takes one argument and returns the thingd according to that
print(x.strftime("%B")) #this sign is used to show the current month
print(x.strftime("%a")) #this sign shows short weekday (Mon)
print(x.strftime("%A")) #this sign shows long weekday (Monday)
print(x.strftime("%w")) #this sign shows weekday in number
print(x.strftime("%b")) #month in short (Jan)
print(x.strftime("%m")) #month in numbers 
print(x.strftime("%y")) #year in short (23)
print(x.strftime("%Y")) #year in long (2023)
print(x.strftime("%S")) #seconds
print(x.strftime("%z")) #timezone
print(x.strftime("%W")) #week number of the year
print(x.strftime("%c")) #the century
print(x.strftime("%x")) #local version of the date
print(x.strftime("%X")) #local version of the time
print(x.strftime("%p")) #shows am or pm
print(x.strftime("%I")) #shows the hour
print(x.strftime("%M")) #shows the minute
#timestamp is used to show how many total timestamps have been born
print(x.timestamp())
#timedelta class is used to calculate differences between dates/ it can add or delete the time
from datetime import timedelta
y= x + timedelta(days=2) 
print(y)
#calender library has functions related to calender
import calendar
z= calendar.month(2023, 7) #this is used to show the whole calendar of the month
print(z)
h= calendar.prcal(2023) #this is used to show the whole calendar of the year
print(h)
#time library has all the functions related to the time
import time
print(time.time()) #it prints the number of ticks spent from 1970 to 2023/now
print(time.sleep(1)) #sleep is used to stop or delay the time by a few seconds
for i in range (0, 5):
    print(i)
    time.sleep(4)