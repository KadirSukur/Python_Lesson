number = int(input("enter a number:"))
total = 0
list_of_number=[int(i) for i in str(number) ]
for i in list_of_number:

    total +=pow(i,len(list_of_number)) 
if (total == number):
    print(f"{number} is a armstrong number")
else:
    print(f"{number} isn't a armstrong number")
