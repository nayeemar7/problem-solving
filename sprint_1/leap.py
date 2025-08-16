def leap(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 == 0:
            return True
        elif n % 100 == 0 and n % 400 != 0:
            return False
        else: 
            return True
    else:
        return False 

year = int(input("Enter the year:"))
if leap(year):
    print("Leap Year")
else:
    print("Not a leap year!")


