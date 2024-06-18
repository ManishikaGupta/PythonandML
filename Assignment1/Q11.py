def generate_fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(generate_fibonacci(n))