#!/usr/bin/env python3
# Author ID: jsingh1101

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure student number is stored as a string
        self.courses = {}

    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:  # Prevent ZeroDivisionError
            print(f'GPA of student {self.name} is 0.0')
            return
        gpa = sum(self.courses.values()) / len(self.courses)
        print(f'GPA of student {self.name} is {gpa}')

