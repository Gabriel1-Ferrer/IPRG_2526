def factorial(n):
    if n == 6:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(6))
