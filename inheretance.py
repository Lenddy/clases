from clases import Student
class Display(Student):
    def __init__(self, f_name, l_name, age, instructore, stack):
        super().__init__(f_name, l_name, age, instructore, stack)

l = Display("ana","maria","age","pablo","java")
l.display_student_info()