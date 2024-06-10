# Program: Power Series Expansion of arccos(x)
# Lab: Lab 1
# Version: 3.0
# Developer: Elenskiy A
# Date: 19.04.2024

import math

def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def power_series_arccos(x, eps=1e-6, max_iterations=500):
    """Calculate the value of arccos(x) using power series expansion."""
    result = math.pi/2 - x
    n = 1
    term = x
    while abs(term) > eps and n < max_iterations:
        term *= -(x ** 2) * (2 * n - 1) / (2 * n)
        result += term / (2 * n + 1)
        n += 1
    return result, n

def main():
    """Main function to execute the program."""
    print("Welcome to Power Series Expansion of arccos(x) Calculator!")
    while True:
        try:
            x = float(input("Enter the value of x (|x| <= 1): "))
            if abs(x) > 1:
                print("Error: |x| must be less than or equal to 1.")
                continue
            eps = float(input("Enter the desired accuracy (eps): "))
            result, n = power_series_arccos(x, eps)
            math_result = math.acos(x)
            print("x   n   F(x)        Math F(x)    eps")
            print("{:.2f}  {}  {:.6f}  {:.6f}  {:.6f}".format(x, n, result, math_result, eps))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
