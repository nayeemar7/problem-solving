def seq_missing(seq):
    missing = []
    for j in range(max(list)):
        if j not in list:
            missing.append(j)
    return missing

n = int(input("Enter how many numbers in sequence: "))
list = []
for i in range(n):
    num = int(input("Enter the number: "))
    list.append(num)
miss = seq_missing(list)
print(miss)
