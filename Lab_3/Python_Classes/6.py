def is_prime(n):
    if n == 1 or n < 2: return False
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True
nums = [int(i) for i in range(50)]
ans = list(filter(is_prime, nums))
print(ans)