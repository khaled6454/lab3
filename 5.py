x= int(input("Enter a number of repetitions"))
# Write your decorator here

def rep():
    for _ in range(x-1):
        hello()
def hello():
       print ('Hello')
rep()
hello()
