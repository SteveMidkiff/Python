# The Student class provides information on each student

class Student:

    # The __init__ method accepts arguments for name, GPA,
    # expected grade, ID and full or part-time.

    def __init__(self, name, idnumber, gpa, grade, time):
        self.__name = name
        self.__idnumber = idnumber
        self.__gpa = gpa
        self.__grade = grade
        self.__time = time

    # The set gpa method accepts an argument for the gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    # The get gpa method returns the students gpa

    def get_gpa(self):
        return self.__gpa

    # The set grade method accepts an argument for the students grade

    def set_grade(self, grade):
        self.__grade = grade

    # The get idnumber method returns the students ID number

    def get_idnumber(self):
        return self.__idnumber

    # The get grade method returns the students expected grade

    def get_grade(self):
        return self.__grade

    # The get time method returns whether the student is full or part-time

    def get_time(self):
        return self.__time

    # The __str__ method returns the student information

    def __str__(self):
        return "Students name:\t" + self.__name + \
               "\nStudent ID number:\t" + self.__idnumber + \
               "\nGrade Point Average:\t" + self.__gpa + \
               "\nExpected Course Grade:\t" + self.__grade + \
               "\nFull or Part Time:\t" + self.__time
    
