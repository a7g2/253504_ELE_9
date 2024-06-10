# Program: Text Analysis V2.0
# Lab: Lab 4
# Version: 3.0
# Developer: Elenskiy A
# Date: 19.04.2024

def count_vowel_start_end_words(text):
    """
    Count the number of words in the text that start or end with a vowel.

    Args:
    text (str): The input text.

    Returns:
    int: The number of words starting or ending with a vowel.
    """
    vowels = "aeiou"
    words = text.lower().split()
    count = 0
    for word in words:
        if word[0] in vowels or word[-1] in vowels:
            count += 1
    return count

def count_char_occurrences(text):
    """
    Count the occurrences of each character in the text.

    Args:
    text (str): The input text.

    Returns:
    dict: A dictionary where keys are characters and values are their occurrences.
    """
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def words_after_comma(text):
    """
    Extract and sort words after commas in alphabetical order.

    Args:
    text (str): The input text.

    Returns:
    list: A list of words after commas in alphabetical order.
    """
    words = text.split(",")
    words_after_comma = [word.strip() for word in words[1:]]
    return sorted(words_after_comma)

def main():
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

    vowel_count = count_vowel_start_end_words(text)
    print("Number of words starting or ending with a vowel:", vowel_count)

    char_occurrences = count_char_occurrences(text)
    print("Character occurrences:")
    for char, count in char_occurrences.items():
        print(char, ":", count)

    words_after_comma_list = words_after_comma(text)
    print("Words after comma in alphabetical order:", words_after_comma_list)

if __name__ == "__main__":
    main()