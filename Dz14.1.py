class LimitError(Exception):
    def __init__(self, message="Превышен лимит студентов в группе"):
        super().__init__(message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}  {self.record_book}"

class Group:

    def __init__(self, number, max_v = 10):
        self.number = number
        self.group = set()
        self.max_v = max_v

    def add_student(self, student):
        if len(self.group) >= self.max_v:
            raise LimitError(f"Нельзя добавить больше {self.max_v} студентов ")
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students =  "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students} '

group = Group('PD1')
for i in range(15):
    try:
        group.add_student(Student('Male', 30 + i, f'Steve_{i}', 'Jobs', 'AN142'))
    except LimitError as e:
        print(e)
print(group)
