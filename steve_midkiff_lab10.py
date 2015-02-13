# This program manages student information for Prefessor Polanco

import student
import pickle

# Global constants for the menu choices

LOOK_UP = 1
ADD = 2
CHANGE_GPA = 3
CHANGE_GRADE = 4
PRINT_INFO = 5
QUIT = 6

FILENAME = 'students.dat'



# main function

def main():

    mystudents = load_students()
    

    # initialize menu option

    choice = 0

    # process menu selection until user quits

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mystudents)
        elif choice == ADD:
            add_student(mystudents)
        elif choice == CHANGE_GPA:
            change_gpa(mystudents)
        elif choice == CHANGE_GRADE:
            change_grade(mystudents)
        elif choice == PRINT_INFO:
            print_info(mystudents)

    save_students(mystudents)
    

        
# The get_menu_choice function displays the menu and
# gets a validated choice from the user.

def get_menu_choice():
    print()
    print('Menu')
    print('--------------------------')
    print('1. Look up a students GPA')
    print('2. Add a new student')
    print('3. Change a students GPA')
    print('4. Change a students expected grade')
    print('5. Print all course students')
    print('6. Quit the program')
    print()

    # Get the user's choice
    choice = int(input('Enter your choice: '))

    # Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Please enter a valid choice: '))

    # return the user's choice
    return choice

# define the look_up function
def look_up(mystudents):
    # Get a name to look up
    print()
    try:
        name = input('Enter the students name: ')

        entry = mystudents.get(name)
    
        print('The students GPA is ', entry.get_gpa())

    except AttributeError:
        print('No entry found.')
    

# define the add student function
def add_student(mystudents):
    print()
    name = input('Please enter the students name: ')
    idnumber = input('Enter the students id number: ')
    gpa = input('Enter the students Grade Point Average: ')
    grade = input('Enter the students expected course grade: ')
    time = input('Is the student full-time or part-time? ')
    print()

    entry = student.Student(name, idnumber, gpa, grade, time)

    if name not in mystudents:
        mystudents[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')
                              
# define the change_gpa function
def change_gpa(mystudents):
    print()
    try:
        print('To change a students GPA')
        name = input('Enter the students name: ')
        print()
        entry = mystudents.get(name)

        print('The current GPA is ', entry.get_gpa())

        new_gpa = input('Enter the new GPA: ')

        entry.set_gpa(new_gpa)

        print('The new GPA has been recorded.')

    except AttributeError:
        print('No entry found.')
    

# define the change_grade function
def change_grade(mystudents):
    print()
    try:
        print('To change a students expected grade')
        name = input('Enter the students name: ')
        print()
        entry = mystudents.get(name)

        print('The current expected grade is ', entry.get_grade())

        new_grade = input('Enter the new expected grade: ')

        entry.set_grade(new_grade)

        print('The new expected grade has been recorded.')

    except AttributeError:
        print('No entry found.')
        
# This defines the print_info function
def print_info(mystudents):
    print()
    for key in mystudents:
        entry = mystudents.get(key)
        print(entry)
        print()

## This defines the load_students function

def load_students():
    try:
        input_file = open(FILENAME, 'rb')

        student_dct = pickle.load(input_file)

        input_file.close()

    except IOError:
        student_dct = {}

    return student_dct

# This defines the save_students function

def save_students(mystudents):
    output_file = open(FILENAME, 'wb')

    pickle.dump(mystudents, output_file)

    output_file.close()
    
# Call the main function
main()

