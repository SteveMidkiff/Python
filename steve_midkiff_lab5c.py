# This program calculates student letter grades and class average

# Get grade input from user and validate to continue

def main():
    class_avg = 0.0
    total_grades = 0.0
    total_entries = 0

    
    print('Enter a students grade to get the letter grade and the class average')
    print('or enter -1 to exit the program.')
    grade = int(input('What was the students grade? '))
    while grade != -1:
    
# Calculate and print letter grade and message
# Use if then print statements

        if grade >= 90:
            print(' ')
            print('Your grade of', grade, 'is an A!')
            print('Great Job! You obviously did your homework!')
            print(' ')

        elif grade >= 80 and grade < 90:
            print(' ')
            print('Your grade of', grade, 'is a B!')
            print('Good Job! You understand the material.')
            print(' ')

        elif grade >= 70 and grade < 80:
            print(' ')
            print('Your grade of', grade, 'is a C!')
            print('This is good enough to pass, but you can do better.')
            print(' ')

        elif grade >= 60 and grade < 70:
            print(' ')
            print('Your grade of', grade, 'is a D!')
            print('You are going to have to do much better than this!')
            print(' ')

        elif grade < 60:
            print(' ')
            print('Your grade of', grade, 'is an F!')
            print('You obviously have not done your homework!')
            print(' ')

# Add to class average and running total of entries

        total_entries += 1
        total_grades = total_grades + grade
        class_avg = total_grades / total_entries
       

        print('Enter another students grade to continue')
        print('or enter -1 to exit the program.')
        grade = int(input('Enter the next students grade '))

# Print total class results

    print(' ')
    print('Your class average is', format(class_avg, '.1f'), 'with', total_entries, 'grades entered.')
    print(' ')
        

main()
