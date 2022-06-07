import random

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Rupert"
letter_list = [letter for letter in name]
print(letter_list)

double_list = [n*2 for n in range(1,5)]
print(double_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

students_score = {name:random.randint(1,100) for name in names}
print(students_score)
passed_students = {name:score for (name,score) in students_score.items() if score >= 50}
print(passed_students)