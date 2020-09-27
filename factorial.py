def factorial(count: int) -> int:
    if count == 1:
        return 1
    return count * factorial(count - 1)


print(factorial(5))
