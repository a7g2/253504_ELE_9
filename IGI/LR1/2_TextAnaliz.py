import re
import os

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def extract_dates(text):
    return re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)

def extract_words_with_specific_structure(text):
    return re.findall(r'\b\w*[aeiou][^aeiou]\b', text)

# Чтение текста из файла
filename = 'Test.txt'
text = read_text_from_file(filename)

# Извлечение дат из текста
dates = extract_dates(text)
print("Dates found:", dates)

# Извлечение слов с определенной структурой
words = extract_words_with_specific_structure(text)
print("Words with specific structure:", words)

def count_sentences(text):
    # Подсчитываем количество предложений
    sentences = re.split(r'[.!?]', text)
    return len(sentences)

def count_sentence_types(text):
    # Подсчитываем количество повествовательных, вопросительных и побудительных предложений
    narr_sentences = len(re.findall(r'[.!?]\s[A-Z]', text))
    interrogative_sentences = len(re.findall(r'[?]\s[A-Z]', text))
    imperative_sentences = len(re.findall(r'[!]\s[A-Z]', text))
    return narr_sentences, interrogative_sentences, imperative_sentences

def count_smileys(text):
    # Подсчитываем количество смайликов
    smileys = re.findall(r'[;:]-*[\(\)\[\]]+', text)
    return len(smileys)

# Подсчет общего количества предложений, типов предложений и смайликов
total_sentences = count_sentences(text)
narr_sentences, interrogative_sentences, imperative_sentences = count_sentence_types(text)
smileys_count = count_smileys(text)

print("Total number of sentences:", total_sentences)
print("Number of narrative sentences:", narr_sentences)
print("Number of interrogative sentences:", interrogative_sentences)
print("Number of imperative sentences:", imperative_sentences)
print("Number of smileys:", smileys_count)


