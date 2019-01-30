def fib():
    print("Fibonacci sequence:")
    a, b = 0, 1  # multiple assignment
    while a < 20:
        print(a, end=" ")
        a, b = b, a + b