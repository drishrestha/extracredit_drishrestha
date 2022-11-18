# Knox College
# This is where all the testing is done

from student import Student
from kclass import Courses

# Lets make a professor
# lets make Course
cs208 = Courses("cs", 208, "Bose")
mus = Courses("mus", 100, "Sol")
psyc = Courses("psyc", 101, "Maam")
bio = Courses("bio", 100, "sir")

# lets make a student
bacha1 = Student("Su", 1, "CS", 2025)
bacha2 = Student("Dri",2, "CS", 2025)

bacha1.add_course(cs208)
bacha1.add_course(mus)
bacha1.add_course(psyc)
print (bacha1)

# testing 4th course that cant be added
# error message
bacha1.add_course(bio)

# testing removing course
# after dropping a course point will be <3 Therefore can add another course
bacha1.drop_course(mus)
bacha1.add_course(bio)
print (bacha1)

