def is_palindrome(s):
    return s == s[::-1]

pol = input()
print(is_palindrome(pol))
