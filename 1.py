Employee = {}
print("Enter the name and the salary or 'no' to exist :")
employee=input("Enter 'yes' to continue or 'no' to exit :")
if employee.lower()== "yes":
   while(employee.lower() !='no'):
       print("Enter the name and the salary or 'no' to exist :")
       employee = input("Enter the name or 'no' to exit :")
       if(employee.lower()=="no"):
           break
       salary = input("Enter the salary :")
       Employee[employee]=salary
       print(Employee.items())
elif employee.lower()=="no":
   print("shut down ...........")
else:
    print("Invalid")
    print("shut down ...........")

print("shut down ...........")