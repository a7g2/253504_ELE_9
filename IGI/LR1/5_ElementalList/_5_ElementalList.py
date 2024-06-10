# Program: Elemental List
# Lab: Lab 5
# Version: 2.0
# Developer: Elenskiy A
# Date: 19.04.2024

def input_list():
    """
    Prompt the user to input elements of a list.

    Returns:
    list: The list of input elements.
    """
    while True:
        try:
            n = int(input("Enter the number of elements in the list: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    lst = []
    for i in range(n):
        while True:
            try:
                num = float(input("Enter element {}: ".format(i+1)))
                lst.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return lst

def product_of_negative_and_sum_of_positive(lst):
    """
    Calculate the product of negative elements and the sum of positive elements
    that occur before the maximum element in the list.

    Args:
    lst (list): The input list.

    Returns:
    tuple: A tuple containing the product of negative elements and the sum of positive elements.
    """
    max_index = lst.index(max(lst))
    negatives_product = 1
    sum_positives = 0
    has_negatives = False
    for i in range(max_index):
        if lst[i] < 0:
            negatives_product *= lst[i]
            has_negatives = True
        elif lst[i] > 0:
            sum_positives += lst[i]
    return has_negatives, negatives_product, sum_positives

def print_list(lst):
    """
    Print the elements of the list.

    Args:
    lst (list): The input list.
    """
    print("List elements:")
    for i, num in enumerate(lst, 1):
        print("Element {}: {}".format(i, num))

def main():
    lst = input_list()
    print_list(lst)
    has_negatives, negatives_product, sum_positives = product_of_negative_and_sum_of_positive(lst)
    if has_negatives:
        print("Product of negative elements:", negatives_product)
    else:
        print("There are no negative elements in the list.")
    print("Sum of positive elements before the maximum element:", sum_positives)

if __name__ == "__main__":
    main()
