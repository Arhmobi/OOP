class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender # пол
        self.finished_courses = [] # завершенные курсы
        self.courses_in_progress = [] #курсы в прогрессе
        self.grades = {} # оценки

    def grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_grade(self):
        if not self.grades:
            return 0.0
        all_grades = [grd for grade in self.grades.values() for grd in grade]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        some_student = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашнее задание: {self.__average_grade()}\n' f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n' f'Завершенные курсы: {', '.join(self.finished_courses)}'
        return some_student

    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()

    def __gt__(self, other):
        return self.__average_grade() > other.__average_grade()

    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()

    def __le__(self, other):
        return self.__average_grade() <= other.__average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname # фамилия
        self.courses_attached = [] # закрепленные курсы


class Lecturer(Mentor):
    grades = {}

    def __average_grade(self):
        if not self.grades:
            return 0.0
        all_grades = [grd for grade in self.grades.values() for grd in grade]
        return round(sum(all_grades) / len(all_grades), 1)

    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()

    def __gt__(self, other):
        return self.__average_grade() > other.__average_grade()

    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()

    def __le__(self, other):
        return self.__average_grade() <= other.__average_grade()

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.__average_grade()}'

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
        return f'Имя: {self.name}\n' f' Фамилия: {self.surname}'


student1 = Student('Sanya', 'Dryahlicin', 'male')
student1.courses_in_progress += ['Python', 'C#', 'Java']
student1.finished_courses += ['Введение в программирование']


student2 = Student('Victorya', 'Obramovich', 'female')
student2.courses_in_progress += ['Python', 'C++', 'Basic']
student2.finished_courses += ['Введение в программирование']



lecturer1 = Lecturer('Boris', 'Davidof')
lecturer1.courses_attached += ['Python']


lecturer2 = Lecturer('Ivan', 'Demidov')
lecturer2.courses_attached += ['Python']



rewiewer1 = Reviewer('Ignat', 'Lobanov')
rewiewer1.courses_attached += ['Python']
rewiewer1.rate_hw(student1, 'Python', 9)
rewiewer1.rate_hw(student1, 'Python', 9)


rewiewer2 = Reviewer('Sergey', 'Martinov')
rewiewer2.courses_attached += ['Python']
rewiewer2.rate_hw(student2, 'Python', 10)
rewiewer2.rate_hw(student2, 'Python', 10)

student1.grade_lecturer(lecturer1, 'Python', 7)
student1.grade_lecturer(lecturer2, 'Python', 9)

student2.grade_lecturer(lecturer1, 'Python', 10)
student2.grade_lecturer(lecturer2, 'Python', 9)

student_list = [student1, student2]

def average_student(student_list, course):
    sum_ = 0
    len_gr = []
    for student in student_list:
        if course in student.grades.keys():
            for grades in student.grades[course]:
                sum_ += grades
                len_gr.append(grades)
    print(sum_ / len(len_gr))

average_student(student_list, 'Python')

lecturer_list = [lecturer1, lecturer2]
def average_lecturer(student_list, course):
    sum_ = 0
    len_gr = []
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            for grades in lecturer.grades[course]:
                sum_ += grades
                len_gr.append(grades)
    print(sum_ / len(len_gr))

average_lecturer(lecturer_list, 'Python')
print(student1 >= student2)
print(student1)
print(lecturer1 != lecturer2)

