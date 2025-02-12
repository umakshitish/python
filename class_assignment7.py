#printing fibonacci series

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Function to print the Fibonacci series
def print_fib_series(n):
    for i in range(n):
        print(fib(i), end=" ")

# Input: Number of terms to print
n = int(input("Enter the number of terms in the Fibonacci series: "))
print("Fibonacci series:")
print_fib_series(n)
