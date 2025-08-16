def fibo_rec(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_rec(num-1) + fibo_rec(num-2)
    
def print_fibo(num):
    if num <= 0:
        print("invalid input")
    else:
        print("Fibonacci series: ")
        for i in range(num):
            print(fibo_rec(i),end = " ")

n = int(input("Enter the number: "))
print_fibo(n)
