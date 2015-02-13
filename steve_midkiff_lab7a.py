# This program gives the user a choice for converting
# various Imperial units of measure to their Metric counterparts


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

#This is where I define my conversion functions. I used a counter to limit the
# input validation. I hope it's ok I used break.
        
def milesToKm():
    # I used a loop and counter so that any exception errors would not count
    # Otherwise I would have used a for loop
    loop = 0
    while loop != 10:
        try:
            miles = float(input('Input the number of miles to convert to kilometers '))
            
            # here I define my exception error
            if miles < 0:
                raise ValueError

        except ValueError:
            print()
            print('Sorry. You cannot convert a negative number.')
            print()

        else:        
            kilometers = miles * 1.6
            loop += 1

            # Open the file in append mode
            conversion_file = open('conversions.txt', 'a')

            # Write the data to the file
            conversion_file.write(str(miles) + '\n')
            conversion_file.write('miles' + '\n')
            conversion_file.write(str(kilometers) + '\n')
            conversion_file.write('kilometers' + '\n')

            # Close the file
            conversion_file.close()


    
def FahToCel():
    # I used a loop and counter so that any exception errors would not count
    # Otherwise I would have used a for loop
    loop = 0
    while loop != 10:
        try:
            degrees_f = float(input('Input the number of degrees fahrenheit to convert to degrees celsius '))

            # here I define my exception error
            if degrees_f > 1000:
                raise ValueError

        except ValueError:
            print()
            print('Sorry. You cannot convert a temperature larger than 1000 degrees.')
            print()

        else:        
            degrees_c = (degrees_f - 32) * 5/9
            loop += 1

            # Open the file in append mode
            conversion_file = open('conversions.txt', 'a')

            # Write the data to the file
            conversion_file.write(str(degrees_f) + '\n')
            conversion_file.write('degrees Fahrenheit' + '\n')
            conversion_file.write(str(degrees_c) + '\n')
            conversion_file.write('degrees Celcius' + '\n')

            # Close the file
            conversion_file.close()

def GalToLit():
    # I used a loop and counter so that any exception errors would not count
    # Otherwise I would have used a for loop    
    loop = 0
    while loop != 10:
        try:
            gallons = float(input('Input the number of gallons to convert to liters '))

            # here I define my exception error
            if gallons < 0:
                raise ValueError

        except ValueError:
            print()
            print('Sorry. You cannot convert a negative number.')
            print()

        else:        
            liters = gallons * 3.9
            loop += 1

            # Open the file in append mode
            conversion_file = open('conversions.txt', 'a')

            # Write the data to the file
            conversion_file.write(str(gallons) + '\n')
            conversion_file.write('gallons' + '\n')
            conversion_file.write(str(liters) + '\n')
            conversion_file.write('liters' + '\n')

            # Close the file
            conversion_file.close()
            
def PoundsToKg():
    # I used a loop and counter so that any exception errors would not count
    # Otherwise I would have used a for loop    
    loop = 0
    while loop != 10:
        try:
            pounds = float(input('Input the number of pounds to convert to kilograms '))

            # here I define my exception error
            if pounds < 0:
                raise ValueError

        except ValueError:
            print()
            print('Sorry. You cannot convert a negative number.')
            print()

        else:        
            kilograms = pounds * 0.45
            loop += 1

            # Open the file in append mode
            conversion_file = open('conversions.txt', 'a')

            # Write the data to the file
            conversion_file.write(str(pounds) + '\n')
            conversion_file.write('pounds' + '\n')
            conversion_file.write(str(kilograms) + '\n')
            conversion_file.write('kilograms' + '\n')

            # Close the file
            conversion_file.close()

def InchesToCm():
    # I used a loop and counter so that any exception errors would not count
    # Otherwise I would have used a for loop    
    loop = 0
    while loop != 10:
        try:
            inches = float(input('Input the number of inches to convert to centimeters '))

            # here I define my exception error
            if inches < 0:
                raise ValueError

        except ValueError:
            print()
            print('Sorry. You cannot convert a negative number.')
            print()

        else:        
            c_meters = inches * 2.54
            loop += 1

            # Open the file in append mode
            conversion_file = open('conversions.txt', 'a')

            # Write the data to the file
            conversion_file.write(str(inches) + '\n')
            conversion_file.write('inches' + '\n')
            conversion_file.write(str(c_meters) + '\n')
            conversion_file.write('centimeters' + '\n')

            # Close the file
            conversion_file.close()
            
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


