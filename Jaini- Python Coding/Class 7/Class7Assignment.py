previous= 0
current= 1
next_number= 0
count= 1
end= int(input("Enter your fibnocic series"))
while count <= end:
    print(next_number)
    count+= 1
    previous= current
    current= next_number
    next_number= previous + current
    Tnumber= previous + current