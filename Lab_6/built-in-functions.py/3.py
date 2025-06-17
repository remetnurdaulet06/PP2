def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == ''.join(reversed(s))
test_string = input()
if is_palindrome(test_string):
    print("Yes")
else:
    print("No")