def is_palindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]
print(is_palindrome("А вал как лава"))
print(is_palindrome("Спел Лепс")) 
print(is_palindrome("Здравствуйте"))