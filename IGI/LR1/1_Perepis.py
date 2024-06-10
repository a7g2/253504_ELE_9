import csv
import pickle
import os
# from colorama import init, Fore, Style

class Person:
    def __init__(self, surname, gender, height):
        self.surname = surname
        self.gender = gender
        self.height = height

    def __repr__(self):
        return f"Person('{self.surname}', '{self.gender}', {self.height})"


def serialize_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['surname', 'gender', 'height']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for person in data:
            writer.writerow({'surname': person.surname, 'gender': person.gender, 'height': person.height})

def serialize_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Пример данных
people_data = [
    Person('Smith', 'Male', 180),
    Person('Johnson', 'Female', 165),
    Person('Williams', 'Male', 175),
    Person('Brown', 'Female', 160),
    Person('Jones', 'Male', 185),
    Person('Garcia', 'Female', 170)
]

# Сериализация в CSV и pickle файлы
serialize_to_csv(people_data, 'people.csv')
serialize_to_pickle(people_data, 'people.pickle')


def deserialize_from_csv(filename):
    people_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            people_data.append(Person(row['surname'], row['gender'], int(row['height'])))
    return people_data

def deserialize_from_pickle(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def average_height_of_women(people_data):
    women_heights = [person.height for person in people_data if person.gender == 'Female']
    if len(women_heights) == 0:
        return 0
    return sum(women_heights) / len(women_heights)

def tallest_male_surname(people_data):
    male_people = [person for person in people_data if person.gender == 'Male']
    tallest_male = max(male_people, key=lambda x: x.height)
    return tallest_male.surname

def has_duplicate_heights(people_data):
    heights = [person.height for person in people_data]
    return len(heights) != len(set(heights))

def input_person_data():
    surname = input("Enter surname: ")

    while True:
        gender_input = input("Enter gender (1 for Male, 2 for Female): ")
        if gender_input == '1':
            gender = 'Male'
            break
        elif gender_input == '2':
            gender = 'Female'
            break
        else:
            print("Invalid input. Please enter '1' for Male or '2' for Female.")
    
    while True:
        try:
            height = int(input("Enter height: "))
            if height <= 0:
                print("Height must be a positive number.")
            elif height >= 280:
                print("Are you okey??")
            else:
                break
        except ValueError:
            print("Invalid input. Height must be a number.")

    return Person(surname, gender, height)

def print_person_info(person):
    print(f"Surname: {person.surname}")
    print(f"Gender: {person.gender}")
    print(f"Height: {person.height}")

# Пример использования
def search_people_by_info(people_data, surname=None, gender=None, height=None):
    matches = []
    for person in people_data:
        if (surname is None or person.surname.lower() == surname.lower()) and \
           (gender is None or person.gender.lower() == gender.lower()) and \
           (height is None or person.height == height):
            matches.append(person)
    return matches

def main1():
    # Загрузка данных
    csv_data = deserialize_from_csv('people.csv')
    pickle_data = deserialize_from_pickle('people.pickle')
    # print("\033[31m Proverka ")
    
    while True:
        print("\nWhat would you like to do?")
        print("0. Exit program")
        print("1. Add new person")
        print("2. Calculate average height of women")
        print("3. Find surname of the tallest male")
        print("4. Check if there are at least two people with the same height")
        print("5. Search for a person")
        
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting program.")
            break
        elif choice == '1':
            new_person = input_person_data()
            pickle_data.append(new_person)
            serialize_to_pickle(pickle_data, 'people.pickle')
            print("New person added successfully.")
        elif choice == '2':
            avg_height = average_height_of_women(csv_data)
            print(f"Average height of women: {avg_height}")
        elif choice == '3':
            tallest_surname = tallest_male_surname(pickle_data)
            print(f"Surname of the tallest male: {tallest_surname}")
        elif choice == '4':
            if has_duplicate_heights(csv_data):
                print("There are at least two people with the same height.")
            else:
                print("There are no two people with the same height.")
        elif choice == '5':
            print("Enter person's information (surname, gender, height) separated by comma. Use '-' for missing information.")
            input_data = input("Enter: ").split(',')
            surname, gender, height = [item.strip() if item.strip() != '-' else None for item in input_data]
            matches = search_people_by_info(pickle_data, surname, gender, height)
            if len(matches) == 0:
                print("No matching person found.")
            else:
                print(f"Found {len(matches)} matching person(s):")
                for match in matches:
                    print_person_info(match)
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main1()
