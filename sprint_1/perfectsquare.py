def perfect_square(num):
    if num < 0:
        return False
    for i in range(int(num**0.5+1)):
        if i*i == num:
            return True
    return False

n = int(input("Enter a number: "))
x = perfect_square(n)
if x:
    print("Perfect Square!")
else:
    print("Not a perfect square")   
