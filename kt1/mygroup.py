groupmates = [
    {
        "name": "Дмитрий",
        "surname": "Устинов",
        "exams": ["Информатика", "Аиг", "История"],
        "marks": [5, 3, 5],
        "average": 4.3
    },
    {
        "name": "Максим",
        "surname": "Ментуc",
        "exams": ["Информатика", "Аиг", "История"],
        "marks": [5, 5, 5],
        "average": 5
    },
    {
        "name": "Юрий",
        "surname": "Григорьев",
        "exams": ["Информатика", "Аиг", "История"],
        "marks": [5, 5, 5],
        "average": 5
    },
    {
        "name": "Даниил",
        "surname": "Каширкин",
        "exams": ["Информатика", "Аиг", "История"],
        "marks": [4, 3, 5],
        "average": 4
    },
    {
        "name": "Никита",
        "surname": "Кузьмин",
        "exams": ["Информатика", "Аиг", "История"],
        "marks": [5, 5, 5],
        "average": 5
    }
]

def print_students(students):
    a=float(input("Введите средний балл: "))
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"    Оценки".ljust(20))
    for student in students:
        if student["average"] >= a:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20),str(student["average"]).ljust(20))


print_students(groupmates)
