## This program takes a numeric date in the format mm/dd/yy
## validates the input and prints the date in long form

# define the main program

def main():
    
# Get the date input from the user

    date = input('Please input the 2013 date in the following format - mm/dd/yy: ')
    

# Split the input into a list

    date_list = date.split('/')
    

# Validate the data

    new_month = validate_month(date_list[0])
    if new_month != date_list[0]:
        date_list[0] = str(new_month)
    new_day = validate_day(date_list[1])
    if new_day != date_list[1]:
        date_list[1] = str(new_day)
    new_year = validate_year(date_list[2])
    if new_year != date_list[2]:
        date_list[2] = str(new_year)

# Display the long form date

    display_date(date_list)

# Define the functions for the program

def validate_month(value):
    value = int(value)
    while value < 1 or value > 12:
        print('That is not a valid month.')
        try:
            value = int(input('Enter a valid month: '))
        except ValueError:
            print('Please enter the numerical value of the month only.')
    return value

def validate_day(value):
    value = int(value)
    while value < 1 or value > 31:
        print('That is not a valid day of the month.')
        try:
            value = int(input('Enter a valid day: '))
        except ValueError:
            print('Please enter the numerical value of the day only.')
    return value

def validate_year(value):
    value = int(value)
    while value != 13:
        print('The year must be 2013.')
        value = 13
    return value

def display_date(value_list):
    month = ''
    if value_list[0] == '1':
        month = 'January'
    if value_list[0] == '2':
        month = 'February'
    if value_list[0] == '3':
        month = 'March'
    if value_list[0] == '4':
        month = 'April'
    if value_list[0] == '5':
        month = 'May'
    if value_list[0] == '6':
        month = 'June'
    if value_list[0] == '7':
        month = 'July'
    if value_list[0] == '8':
        month = 'August'
    if value_list[0] == '9':
        month = 'September'
    if value_list[0] == '10':
        month = 'October'
    if value_list[0] == '11':
        month = 'November'
    if value_list[0] == '12':
        month == 'December'
    print('The date you entered is ', month, ' ', value_list[1], ', 20', \
          value_list[2], sep='')
    

main()



