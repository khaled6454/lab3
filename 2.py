MaxNumber=[]
for i in range(10):
    number = int(input("Enter a number : "))
    MaxNumber.append(number)
MaxNum=MaxNumber[0]
for num in MaxNumber:
   if num > MaxNum:
      MaxNum=num
print("The Max number is : "+str(MaxNum))