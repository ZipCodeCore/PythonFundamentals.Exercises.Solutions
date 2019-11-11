def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    last, next = 0, 1
    for _ in range(n):
        temp = next
        next = last + next
        last = temp
    return last


print(fibonacci(0))
print(fibonacci(4))
print(fibonacci(30))
print(fibonacci(149))
