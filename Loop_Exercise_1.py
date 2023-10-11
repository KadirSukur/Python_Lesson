number= int(input("Enter a number: "))

i = 1
total=0
while (i < number):
    if (number % i == 0):
        total +=i
    i+=1
if (total == number):
  print("number is perfect number...")
else:
     print("number isn't perfect number")  