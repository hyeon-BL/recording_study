def power(A, n):
    # Base case
    if n == 0:
        return 1
    
    # Recursively divide the problem into subproblems
    half = power(A, n // 2)
    
    # If n is even
    if n % 2 == 0:
        return half * half
    # If n is odd
    else:
        return A * half * half

# Test the function
A = 2
n = 3
print(power(A, n))