def fibonaccifind(position):
    list = []
    a = 0
    b = 1
    list.append(0)
    for i in range(position + 1):
        list.append(b)
        c = a + b
        a = b
        b = c
    return list[position]

n = int(input("Enter the position of sequence: "))
print("At position",n,"of the Fibonacci sequence, the number is",fibonaccifind(n))
