# extracredit_drishrestha

This is a readme file for my extra credit assignment that contains three classes all of which can be instantiated in main.py. The classes are named as following:
- Student
- Professor
- Courses

# class Student #
The class student takes in constructor the following:
- name
- id
- Major
- year
- Courses
- point

The class contains 2 methods:
- add_course
- drop_course

* add_course
This method takes Courses in its parameter from the class Course. It adds the course to student's course list only if the point is < 3 as max point is 3. If point is greater than 3 it prints and error message.

* drop_course
This method removes the mentioned course from the student's course list and while doing so also deducts the point the course carries. The method doesn't work is point is less than 1.

# class Courses #
The class Courses takes in its parameter:
- title
- course_code
- Professor
- point

It only contains the magic method __repr__ as the class is accessed in class Student. 
Here, the parameter point has a default value of 1 as every course has 1 point.






