def fibonacci_sequence(n):
    fibonacci_numbers = []

    if n <= 0:
        return fibonacci_numbers

    a, b = 0, 1
    for _ in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b

    return fibonacci_numbers
