def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
input_str = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)
palindromes = [num for num in numbers if is_palindrome(num)]
print("Palindromes:", palindromes)
prime_palindromes = [num for num in prime_numbers if is_palindrome(num)]
print("Prime palindromes:", prime_palindromes)