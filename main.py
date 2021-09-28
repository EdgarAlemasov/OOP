class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)

        grade_for_lecture = sum(all_grades) / len(all_grades)
        return round(grade_for_lecture, 1)

    def average_grade_for_one_course(self, course_name):
        if course_name in self.grades.items():
            print(course_name)
            res = sum(course_name.values()) / len(course_name.values())
            print(round(res, 1))

    def courses(self):
        all_courses = ', '.join(self.courses_in_progress)
        return all_courses

    def courses_end(self):
        all_courses = ', '.join(self.finished_courses)
        return all_courses

    def __str__(self):
        res = f'Имя = {self.name}' \
              f'\nФамилия = {self.surname}' \
              f'\nСредняя оценка за домашние задания = {self.average_grade()}' \
              f'\nКурсы в процессе изучения: {self.courses()}' \
              f'\nЗавершённые курсы: {self.courses_end()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)

        grade_for_lecture = sum(all_grades) / len(all_grades)
        return round(grade_for_lecture, 1)

    def __str__(self):
        res = f'Имя = {self.name}' \
              f'\nФамилия = {self.surname}' \
              f'\nСредняя оценка за лекции = {self.average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя = {self.name}' \
              f'\nФамилия = {self.surname}'
        return res


# ПРОВЕРКА КОДА
student_1 = jason_cook = Student('Jason', 'Cook', 'male')
student_2 = harry_rose = Student('Harry', 'Rose', 'male')
mentor_1 = maria_day = Mentor('Maria', 'Day')
mentor_2 = dana_edwards = Mentor('Dana', 'Edwards')
lecturer_1 = christopher_smith = Lecturer('Christopher', 'Smith')
lecturer_2 = christina_kelly = Lecturer('Christina', 'Kelly')
reviewer_1 = deborah_hammond = Reviewer('Deborah', 'Hammond')
reviewer_2 = tina_hall = Reviewer('Tina', 'Hall')

student_list = [student_1, student_2]
mentor_list = [mentor_1, mentor_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]

jason_cook.courses_in_progress += ['Python', 'Java', 'Javascript']
jason_cook.grades.update({'Python': [10, 9, 10, 8, 8], 'Java': [9, 9, 9, 6, 10, 10], 'Javascript': [7, 7, 9, 10]})

harry_rose.courses_in_progress += ['Python', 'Java', 'Javascript']
harry_rose.grades.update({'Python': [8, 10, 10], 'Java': [10, 10, 8, 7, 10], 'Javascript': [10, 10, 10, 10, 9, 7]})

christopher_smith.courses_attached += ['Python', 'Java', 'Javascript']
christopher_smith.grades.update(
    {'Python': [10, 10, 10, 10, 10], 'Java': [10, 10, 9], 'Javascript': [9, 9, 9, 8, 8, 10]})

christina_kelly.courses_attached += ['Python', 'Java', 'Javascript']
christina_kelly.grades.update({'Python': [8, 10, 8, 10, 7], 'Java': [7, 10, 9], 'Javascript': [9, 9, 10, 10, 10, 10]})

help = ("""
    'Welcome to help menu: '
    'sag' - средняя оценка за дз конкретного курса у всех студентов
    'lag' - средняя оценка за лекции конкретного курса у всех лекторов
    'all_students' - все студенты
    'all_lecturers' - все лекторы
    'all_reviewers' - все ревьюверы
    'student_compare' - сравниваем студентов по средней оценке за ДЗ
    'lecturer_compare' - сравниваем лекторов по средней оценке за лекции

    'Course list: Python, Java, JavaScript'
""")


def student_average_grade(student_list, course_name):
    for student in student_list:
        if course_name in student.courses_in_progress:
            if course_name in student.grades:
                all_course_grade = []
                avg = sum(student.grades.get(course_name)) / len(student.grades.get(course_name))
                all_course_grade.append(avg)
    all_avg = sum(all_course_grade) / len(all_course_grade)
    res = print(f'Средний балл за ДЗ по курсу {course_name} = {round(all_avg, 2)}')
    return res


def lecturer_average_grade(lecturer_list, course_name):
    for lecturer in lecturer_list:
        if course_name in lecturer.courses_attached:
            if course_name in lecturer.grades:
                all_course_grade = []
                avg = sum(lecturer.grades.get(course_name)) / len(lecturer.grades.get(course_name))
                all_course_grade.append(avg)
    all_avg = sum(all_course_grade) / len(all_course_grade)
    res = print(f'Средний балл за лекции по курсу {course_name} = {round(all_avg, 2)}')
    return res


def student_compare():
    if jason_cook < harry_rose:
        print(
            f' Средняя оценка за дз {jason_cook.name} {jason_cook.surname} меньше средней оценки {harry_rose.name} {harry_rose.surname}')
        print(jason_cook < harry_rose)
    elif jason_cook > harry_rose:
        print(
            f' Средняя оценка за дз {jason_cook.name} {jason_cook.surname} больше средней оценки {harry_rose.name} {harry_rose.surname}')
        print(jason_cook > harry_rose)
    elif jason_cook == harry_rose:
        print(
            f' Средняя оценка за дз {jason_cook.name} {jason_cook.surname} равна средней оценки {harry_rose.name} {harry_rose.surname}')
        print(jason_cook == harry_rose)


def lecturer_compare():
    if christopher_smith < christina_kelly:
        print(
            f' Средняя оценка за лекции {christopher_smith.name} {christopher_smith.surname} меньше средней оценки {christina_kelly.name} {christina_kelly.surname}')
        print(christopher_smith < christina_kelly)
    elif christopher_smith > christina_kelly:
        print(
            f' Средняя оценка за лекции {christopher_smith.name} {christopher_smith.surname} больше средней оценки {christina_kelly.name} {christina_kelly.surname}')
        print(christopher_smith > christina_kelly)
    elif christopher_smith == christina_kelly:
        print(
            f' Средняя оценка за лекции {christopher_smith.name} {christopher_smith.surname} равна средней оценки {christina_kelly.name} {christina_kelly.surname}')
        print(christopher_smith == christina_kelly)


def start():
    while True:
        answer = input('\nВведите команду или Help для справки: ').lower()
        if answer.lower() == 'help':
            print(help)
        elif answer == 'sag':
            course_name = input('Введите название курса: ').capitalize()
            student_average_grade(student_list, course_name)
        elif answer == 'lag':
            course_name = input('Введите название курса: ').capitalize()
            lecturer_average_grade(lecturer_list, course_name)
        elif answer == 'all_students':
            print(f'\nСтуденты: \n{student_1} \n{student_2}')
        elif answer == 'all_lecturers':
            print(f'\nЛекторы: \n{lecturer_1} \n{lecturer_2}')
        elif answer == 'all_reviewers':
            print(f'\nРевьюверы: \n{reviewer_1} \n{reviewer_2}')
        elif answer == 'student_compare':
            student_compare()
        elif answer == 'lecturer_compare':
            lecturer_compare()
        elif answer == 'quit':
            print('Вы вышли из программы!')
            break
        else:
            print('Неверная команда!')
    else:
        start()


start()