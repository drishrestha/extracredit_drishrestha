# creating student class
from kclass import Courses


class Student:
    # constructor that takes name, major, graduating year
    def __init__(self, name, id, major, year, Courses=None, point=None):
        self.name = name
        self.id = id
        self.year = year
        self.major = major
        self.courses = Courses
        if point == None:
            self.point = 0
        else:
            self.point = point
        # if courses is none then make courses an empty list else
        if Courses == None:
            self.courses = []
        else:
            self.courses = Courses

    # class methods
    def __repr__(self):  # magic method to get student info
        return f"Name: {self.name}\n\
        idno.: {self.id} \n\
        major: {self.major}\n\
        year: {self.year}\n\
        courses: {self.courses}"

    # making a method which adds a class to a student
    # max point = 3
    def add_course(self, Courses):
        # add a course if point is <3
        if self.point <3:
            # add course to course list
            # point increases by 1
            self.point += 1
            self.courses.append(Courses)
            print(f"Course {Courses.title} has been added.")
        else:
            print("You already have 3 points. Sorry you cant take more :). ")

    # dropping course deducts point by 1
    # removes course from course list
    def drop_course(self, Courses):
        if self.point < 1:
            print("There are no courses to be dropped.")
        else:
            self.point -= 1
            self.courses.remove(Courses)
            print(f"Course {Courses.title} has been dropped.")
