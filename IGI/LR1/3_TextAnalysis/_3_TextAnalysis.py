# Program: Text Analysis
# Lab: Lab 3
# Version: 1.0
# Developer: Elenskiy A
# Date: 19.04.2024

import string

def count_spaces_and_punctuation(text):
    """
    Count the number of spaces and punctuation marks in the input text.

    Args:
    text (str): The input text to analyze.

    Returns:
    tuple: A tuple containing the counts of spaces and punctuation marks, respectively.
    """
    space_count = 0
    punctuation_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
    return space_count, punctuation_count

def main():
    """
    Main function to execute the program.
    """
    text = input("Enter the text: ")
    spaces, punctuation = count_spaces_and_punctuation(text)
    print("Number of spaces: ", spaces)
    print("Number of punctuation marks: ", punctuation)

if __name__ == "__main__":
    main()
