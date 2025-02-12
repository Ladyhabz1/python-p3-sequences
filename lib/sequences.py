#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1] if length > 1 else [0] if length == 1 else []
    
    while len(fibonacci) < length:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci)  # Ensure it prints as a list


print_fibonacci(10) # Expected Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
