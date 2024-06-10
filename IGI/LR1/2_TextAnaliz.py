import re
import os

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def extract_dates(text):
    return re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)

def extract_words_with_specific_structure(text):
    return re.findall(r'\b\w*[aeiou][^aeiou]\b', text)

# ������ ������ �� �����
filename = 'Test.txt'
text = read_text_from_file(filename)

# ���������� ��� �� ������
dates = extract_dates(text)
print("Dates found:", dates)

# ���������� ���� � ������������ ����������
words = extract_words_with_specific_structure(text)
print("Words with specific structure:", words)

def count_sentences(text):
    # ������������ ���������� �����������
    sentences = re.split(r'[.!?]', text)
    return len(sentences)

def count_sentence_types(text):
    # ������������ ���������� �����������������, �������������� � ������������� �����������
    narr_sentences = len(re.findall(r'[.!?]\s[A-Z]', text))
    interrogative_sentences = len(re.findall(r'[?]\s[A-Z]', text))
    imperative_sentences = len(re.findall(r'[!]\s[A-Z]', text))
    return narr_sentences, interrogative_sentences, imperative_sentences

def count_smileys(text):
    # ������������ ���������� ���������
    smileys = re.findall(r'[;:]-*[\(\)\[\]]+', text)
    return len(smileys)

# ������� ������ ���������� �����������, ����� ����������� � ���������
total_sentences = count_sentences(text)
narr_sentences, interrogative_sentences, imperative_sentences = count_sentence_types(text)
smileys_count = count_smileys(text)

print("Total number of sentences:", total_sentences)
print("Number of narrative sentences:", narr_sentences)
print("Number of interrogative sentences:", interrogative_sentences)
print("Number of imperative sentences:", imperative_sentences)
print("Number of smileys:", smileys_count)


