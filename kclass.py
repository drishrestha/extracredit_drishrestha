# class for courses
from prof import Professor


class Courses:
    # constructor
    def __init__(self, title, course_code, Professor, point=None):
        self.title = title
        self.course_code = course_code
        self.professor = Professor
        self.point = 1

    # __repr__ method
    def __repr__(self):
        return f"\n             {self.title}, {self.course_code}, {self.professor}, point: {self.point}"
