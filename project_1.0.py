import numpy as np


class Person:
    def __init__(self, name: str, age: int, id_code: str):
        self.name = name
        self.age = age
        self._id_code = id_code

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('invalid value.')
        self._age = age

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nMeliCode: {self._id_code}'


class Student(Person):
    univ_id = 10001
    total_student = 0

    def __init__(self, name: str, age: int, id_code: str):
        super().__init__(name, age, id_code)
        self.univ_id = Student.univ_id
        self.lessons = {}
        Student.univ_id += 1
        Student.total_student += 1

    def add_lesson_score(self, lesson, score: int = 0):
        if lesson not in self.lessons:
            fl = lesson.add_student(self.name)
            if fl:
                self.lessons[lesson.topic] = score
        else:
            self.lessons[lesson.topic] = score

    def __str__(self):
        text = super().__str__()
        return text + f'\nUnivID: {self.univ_id}'

    def gpa(self):
        return sum(i for i in self.lessons.values()) / len(self.lessons)


class Lesson:
    def __init__(self, topic: str, teacher_name: str, capacity: int):
        self.topic = topic
        self.teacher = teacher_name
        self.capacity = capacity
        self.students = []

    def add_student(self, student_name: str):
        if self.capacity <= len(self.students):
            print('class capacity is full')
            return False
        if student_name in self.students:
            print(f'{student_name} already is in class list.')
        else:
            self.students.append(student_name)
            return True


class Univ:
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.lessons = []

    def add_student(self, student):
        if isinstance(student, Student) and student not in self.students:
            self.students.append(student)
            print('Done.')
        else:
            print('Error...! student already is in univ list')

    def del_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print('Done.')
        else:
            print('failed. student is not in univ list')

    def add_lesson(self, lesson):
        if isinstance(lesson, Lesson) and lesson not in self.lessons:
            self.students.append(lesson)
            print('Done.')
        else:
            print('Error...!')

    def sort_by_gpa(self):
        total_gpa = []
        for i in self.students:
            total_gpa.append((i.name, i.gpa()))

        n = len(total_gpa)
        for i in range(n):
            for j in range(i+1, n):
                if total_gpa[j][1] > total_gpa[i][1]:
                    total_gpa[i], total_gpa[j] = total_gpa[j], total_gpa[i]

        # the time of the static sorting method is O(n**2) and tata(n**2) that n is len of total_gpa, because thr 2
        # loops are nested inside each other

        for i in range(n):
            print(f'{i+1}. {total_gpa[i][0]}: {total_gpa[i][1]}')

    def scores_list(self, lesson):
        scores = np.array([i.lessons[lesson.topic] for i in self.students])
        mean_scores = np.mean(scores)
        max_scores = np.max(scores)
        min_scores = np.min(scores)
        std_scores = np.std(scores)
        passed_students = np.sum(scores >= 10)
        failed_students = np.sum(scores < 10)
        print(f'mean: {mean_scores}\nmax: {max_scores}\nmin: {min_scores}\nstd: {std_scores}'
              f'\nnumber of passed students: {passed_students}\nnumber of failed students: {failed_students}')

    @staticmethod
    def add_score(student, lesson, score: float):
        student.add_lesson_score(lesson, score)

    @staticmethod
    def print_scores(student):
        print(student, '\n')
        for i, z in student.lessons.items():
            print(f'{i}: {z}')


person1 = Person('soroush sharifi', 19, '3721316290')

student1 = Student('soroush sharifi', 19, '3721316290')
student2 = Student('raman sharifi', 19, '0326317299')
student3 = Student('ahmad sharifi', 20, '3821456700')

lesson1 = Lesson('math2', 'Zakeri', 40)
lesson2 = Lesson('advance_programing', 'Ahmadi', 43)

lesson3 = Lesson('andisheh', 'Aghabigi', 60)
kntu = Univ('kntu')

kntu.add_student(student1)
kntu.add_student(student2)
kntu.add_student(student3)

kntu.add_score(student1, lesson1, 18.60)
kntu.add_score(student1, lesson2, 20)
kntu.add_score(student1, lesson3, 18)
kntu.add_score(student2, lesson1, 17)
kntu.add_score(student2, lesson2, 9)
kntu.add_score(student2, lesson3, 17)
kntu.add_score(student3, lesson1, 20)
kntu.add_score(student3, lesson2, 20)
kntu.add_score(student3, lesson3, 17)

print(80*'*')
kntu.print_scores(student1)
print(80*'*')
kntu.sort_by_gpa()
print(80*'*')
kntu.scores_list(lesson2)
