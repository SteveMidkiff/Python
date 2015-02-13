# This program writes the names and averages of 12 students to a txt file
# and then reads them from the file to display on the screen

# Define our variables
def main():
    



# Get the input from the keyboard
    student_num = 0
    while student_num != 12:
        student_name = input('Please enter the students name...')
        try:
            student_grade = int(input('What is the students average grade...'))

            if student_grade < 0 or student_grade > 100:
                raise ValueError

        except ValueError:
            print()
            print('The Students grade cannot be less than zero or greater' \
                  ' than 100.')
            print()



# Open the file in append mode
        else:
            grades_file = open('grades.txt', 'a')
            student_num += 1

# Write the data
            grades_file.write(student_name + '\n')
            grades_file.write(str(student_grade) + '\n')

# Close the file
            grades_file.close()
        
    print('Students name and grade averages were written to' \
              ' grades.txt.')
    print()
    input('Press enter to review the data. ')
    print()
        
        
# Open the file for input and display results
    try:
        grades_file = open('grades.txt', 'r')

    except IOError:
        print()
        print('An error occurred trying to read the file grades.txt.')
        print()

    else:
        read_name = grades_file.readline()
        while read_name != '':
            read_grade = grades_file.readline()

            read_name = read_name.rstrip('\n')
            
            print('The students name is ', read_name),
            print('with an average of ', read_grade)

            read_name = grades_file.readline()

        grades_file.close()
        
main()
