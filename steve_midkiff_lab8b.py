## This is a program to read the student's names from Professor Polanco's
## class into a list, sort the list and write it to a file.

# Define the main function

def main():
    

# Create the list

    students = [0] * 12

# Get the input of 12 student names

    for index in range(12):
        print("Please enter student number", index + 1, \
                     "'s name: ", sep='', end='')
        students[index] = str(input())
    print(students)

# Sort the list

    list_sort(students)  

# Reverse the list

    list_reverse(students)

# append the professor's name

    add_your_name(students)

# append my name to the list

    add_my_name(students)

# write the list to the names file

    write_file(students)

# Display the contents of the file

    display_file()

# Convert the list to a tuple

    students_tuple = tuple(students)

## define my functions

def list_sort(students):
    students.sort()
    return students

def list_reverse(students):
    students.reverse()
    return students

def add_your_name(students):
    students.append('Professor Polanco')
    return students

def add_my_name(students):
    students.insert(0, 'Steve Midkiff')
    return students

def write_file(students):
    outfile = open('names.txt', 'w')
    for items in students:
        outfile.write(items + '\n')
    outfile.close()

def display_file():
    infile = open('names.txt', 'r')
    student_names = infile.readlines()
    infile.close()
    # strip the \n from each element
    index = 0
    while index <len(student_names):
        student_names[index] = student_names[index].rstrip('\n')
        index += 1
        
    for items in student_names:
        print(items)
    
    

# call the main function

main()




