import math
def prime(num):
    if num < 2:
        print("Invalid number")
        return
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            print("Not a Prime number!")
            return
    print("Prime number!")
 
n = int(input("Enter a number: "))
prime(n)