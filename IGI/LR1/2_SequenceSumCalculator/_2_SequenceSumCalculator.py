# Program: Sequence Sum Calculator
# Lab: Lab 2
# Version: 3.0
# Developer: Elenskiy A
# Date: 19.04.2024

import math

# Function to get user input sequence
def get_input_sequence():
    """
    This function gets a sequence of numbers from the user until 0 is entered.
    Returns:
        list: A list of integers entered by the user.
    """
    sequence = []
    while True:
        try:
            num = int(input("Enter a number (0 to end): "))
            if num == 0:
                break
            sequence.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return sequence

# Function to calculate average of even numbers in the sequence
def calculate_average(sequence):
    """
    This function calculates the average of even numbers in the given sequence.
    Args:
        sequence (list): A list of integers.
    Returns:
        float: Average of even numbers in the sequence, or 0 if no even numbers are present.
    """
    even_numbers = [num for num in sequence if num % 2 == 0]
    if len(even_numbers) == 0:
        return 0
    return sum(even_numbers) / len(even_numbers)

def main():
    print("Enter a sequence of numbers. Enter 0 to finish.")
    sequence = get_input_sequence()
    average = calculate_average(sequence)
    print("Average of even numbers:", average)

if __name__ == "__main__":
    main()