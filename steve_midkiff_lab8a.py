# This is where I define the main function.

def main():
    choice = 0

    while choice != 6:
        display_menu()
        try:
            choice = int(input('Enter your choice: '))          
                
            if choice == 1:
                milesToKm()

            elif choice == 2:
                GalToLit()

            elif choice == 3:
                PoundsToKg()

            elif choice == 4:
                InchesToCm()

            elif choice == 5:
                FahToCel()

            elif choice > 6:
                raise ValueError

        except ValueError:
            print()
            print('That is not a menu option. Please try again.')
            print()

             
    
    print(' ')
    print('Thank you for using the conversion program!')

#This is where I define my conversion functions.

def FahToCel():
    temp_list = []

    for degree in range(-10, 100, 10):
        celcius = (degree - 32) * 5/9
        convert_list = [degree, celcius]
        temp_list.append(convert_list)

    for items in temp_list:
        print(items[0], 'degrees Celcius is equal to', \
              format(items[1], '.2f'), 'degrees Fahrenheit.')

def milesToKm():
    temp_list = []

    for miles in range(-10, 100, 10):
        kilometers = miles * 1.6
        convert_list = [miles, kilometers]
        temp_list.append(convert_list)

    for items in temp_list:
        print(items[0], 'miles is equal to', \
              format(items[1], '.2f'), 'kilometers.')

def GalToLit():
    temp_list = []

    for gallons in range(-10, 100, 10):
        liters = gallons * 3.9
        convert_list = [gallons, liters]
        temp_list.append(convert_list)

    for items in temp_list:
        print(items[0], 'gallons is equal to', \
              format(items[1], '.2f'), 'liters.')

def PoundsToKg():
    temp_list = []

    for pounds in range(-10, 100, 10):
        kilograms = pounds * 0.45
        convert_list = [pounds, kilograms]
        temp_list.append(convert_list)

    for items in temp_list:
        print(items[0], 'pounds is equal to', \
              format(items[1], '.2f'), 'kilograms.')

def InchesToCm():
    temp_list = []

    for inches in range(-10, 100, 10):
        c_meters = inches * 2.54
        convert_list = [inches, c_meters]
        temp_list.append(convert_list)

    for items in temp_list:
        print(items[0], 'inches is equal to', \
              format(items[1], '.2f'), 'centimeters.')
    
# Defining the main menu
def display_menu():
    print('Conversion Program')
    print('Please select from the menu')
    print('1.) Miles to kilometers')
    print('2.) Gallons to liters')
    print('3.) Pounds to kilograms')
    print('4.) Inches to centimeters')
    print('5.) Fahrenheit to Celcius')
    print('6.) Quit')

# Calling the main function    
main()

