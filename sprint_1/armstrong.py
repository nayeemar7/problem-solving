def armstrong(endrange):
    armstronglist = []
    for i in range(1,endrange):
        sum = 0
        for digit in str(i):
            cube = int(digit) ** len(str(i))
            sum = sum + cube
        if sum == i:
                armstronglist.append(i)
    return armstronglist 
             
num = int(input("Enter the range of armstrong numbers needed: "))
print(armstrong(num))


        



