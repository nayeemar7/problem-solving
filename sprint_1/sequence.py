def sequence(row):
    mul = row*2
    list = []
    for i in range(mul):
        list.append(i+1)
    return list
        

rows = int(input("Enter number of rows: "))
n = sequence(rows)
for seq in range(rows):
    print(n[2*seq],n[2*seq+1])


