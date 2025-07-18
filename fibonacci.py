def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
n = 10  # Generate first 10 Fibonacci numbers
print(fibonacci_series(n))