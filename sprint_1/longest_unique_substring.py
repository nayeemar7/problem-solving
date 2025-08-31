def longest_unique_substring(s):
    if not s:
        return 0   

    start = 0
    max_length = 0
    best_start = 0  

    for end in range(len(s)):
        current_char = s[end]
        current_window_substring = s[start:end]

        if current_char in current_window_substring:
            repeat_index = s.find(current_char, start, end)
            start = repeat_index + 1

        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            best_start = start   
    longest_substring = s[best_start:best_start + max_length]
    return longest_substring, max_length
str = input("Enter the string: ")
print(longest_unique_substring(str))