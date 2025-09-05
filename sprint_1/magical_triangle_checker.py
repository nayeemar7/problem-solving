import math
def magical_triangle_checker(l):
    global gcd
    sum_of_list = sum(l)
    root = math.sqrt(sum_of_list)
    if root*root != sum_of_list:
        return False
    str_of_sum_of_list = str(sum_of_list)
    l_of_sum = []
    for i in str_of_sum_of_list:
        l_of_sum.append(i)
    gcd = gcd_multiple(l_of_sum)
    return prime_check(gcd)

def gcd_multiple(l):
    def gcd(a,b):
        while b!= 0:
            remainder = a % b
            a = b
            b = remainder 
        return a
    result = l[0]
    for i in l[1:]:
        result = gcd(int(result),int(i))
    return result
    
def prime_check(n):
        if int(n) < 2:
            return False   
        else:
            for i in range(int(n)):
                for j in range(2,int(math.sqrt(i))+1): 
                    if int(n) % i != 0:
                        return False
        return True 

l = []
n = int(input("Enter number of elements in list: "))
for i in range(n):
    ele = int(input("Enter the element: "))
    l.append(ele)
if magical_triangle_checker(l):
    print("Magical")
else:
    print("Not magical")    

    
    
    


    


    








    






