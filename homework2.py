class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer (self,lecturer,lcourse,lgrade):
        if isinstance(lecturer,Lecturer) and lcourse in lecturer.courses_attached or lcourse in self.courses_in_progress:
            if lcourse in lecturer.lgrades:
                lecturer.lgrades[lcourse] += [lgrade]
            else:
                lecturer.lgrades[lcourse] = [lgrade]
        else:
            print ('Ошибка')

    def get_average_grade(self):
        total_grade = 0
        total_assignments = 0
        print (self.grades) # Проверка что оценки записаны правильно для себя
        for grades in self.grades.values():
            total_grade += sum(grades)
            total_assignments += len(grades)
        if total_assignments == 0:
            return 0
        #print (total_grade, total_assignments) # Проверка расчета среднего
        return total_grade / total_assignments

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{self.get_average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if isinstance(self, Student):
            return self.get_average_grade() < other.get_average_grade()
        elif isinstance(other, Student):
            return self.get_average_grade() < other.get_average_lgrade()
        else:
            raise TypeError("Можно сравнивать только студентов и лекторов")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):    # Лекторы
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.lgrades={}

    def get_average_lgrade(self):
        total_lgrade = 0
        total_lassignemts = 0
        print (self.lgrades) #Проверка что оценка и курсы записаны правильно для себя
        for lgrade in self.lgrades.values():
            total_lgrade += sum (lgrade)
            total_lassignemts += len (lgrade)
        if total_lassignemts == 0:
            return 0
        return total_lgrade / total_lassignemts

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{self.get_average_lgrade()}')

    def __lt__(self, other):
        if isinstance(self, Lecturer):
            return self.get_average_lgrade() < other.get_average_lgrade()
        elif isinstance(other, Lecturer):
            return self.get_average_lgrade() < other.get_average_lgrade()
        else:
            raise TypeError("Можно сравнивать только студентов и лекторов")


class Reviewer (Mentor):    # Эксперты проверяющие ДЗ
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')



best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['SQL']
best_student1.finished_courses += ['Введение в программирование']

best_student2 = Student('Grigorii', 'Rachkov', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['SQL']
best_student2.finished_courses += ['GIT']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['SQL']

cool_lector1 = Lecturer ('John', 'Snow')
cool_lector1.courses_attached += ['SQL']
cool_lector2 = Lecturer ('Nikolay', 'Khashchanov')
cool_lector2.courses_attached += ['SQL']

best_student1.rate_lecturer(cool_lector1, 'SQL', 5)
best_student1.rate_lecturer(cool_lector2, 'SQL', 10)
best_student2.rate_lecturer(cool_lector1, 'SQL', 6)
best_student2.rate_lecturer(cool_lector2, 'SQL', 9)

cool_mentor.rate_hw(best_student1, 'Python', 8)
cool_mentor.rate_hw(best_student1, 'SQL', 8)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'SQL', 10)


print(best_student1)
print(best_student2)


print(cool_lector1)
print(cool_lector2)


print(best_student1 < best_student2)
print(cool_lector1 < cool_lector2)


#print(best_student.grades)
#print(cool_lector.lgrades)

