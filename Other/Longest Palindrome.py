def longest_palindrome(s):
    slice_lengths = []
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            slice = s[i:j]
            if slice == slice[::-1]:
                slice_lengths.append(len(slice))
    return max(slice_lengths) if len(slice_lengths) > 0 else 0


print(longest_palindrome("baablkj12345432133d"))