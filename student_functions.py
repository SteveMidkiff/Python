## This defines the load_students function

def load_students():
    try:
        input_file = open(FILENAME, 'rb')

        student_dct = pickle.load(input_file)

        input_file.close()

    except IOError:
        student_dct = {}

    return student_dct

## This defines the new student function

def add_student(mystudents):
    name = input('Enter students name: ')


    entry = students.Students(name, gpa, 
