def mode(list):
    freq_dict = {}
    for i in list:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    max_element = None
    max_freq = -1
    for element,freq in freq_dict.items():
        if freq > max_freq:
            max_element = element
            max_freq = freq
    return max_element

list = []
n = int(input("Enter elements range: "))
for i in range(n):
    x = int(input("Enter elements: "))
    list.append(x)
print(mode(list))