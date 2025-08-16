def pascal(row):
    triangle = []
    current_row = [1]
    for i in range(row):
        triangle.append(current_row)
        next_row = [1]
        for j in range(len(current_row)-1):
            element = current_row[j] + current_row[j+1]
            next_row.append(element)
        next_row.append(1)
        current_row = next_row
    return triangle

n = int(input("Enter number of rows: "))
print(pascal(n))