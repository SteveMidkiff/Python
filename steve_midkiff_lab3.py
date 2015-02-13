# This is where I define the main function.
def main():
    print('Please choose what you would like to convert:')
    print('Select 1 to convert miles to kilometers')
    print('Select 2 to convert fahrenheit to celsius')
    print('Select 3 to convert gallons to liters')
    print('Select 4 to convert pounds to kilograms')
    print('Select 5 to convert inches to centimeters')
    convert = input('Selection --> ')


    if convert == '1':
        milesToKm()
        
    elif convert == '2':
        FahToCel()
    
    elif convert == '3':
        GalToLit()

    elif convert == '4':
        PoundsToKg()

    elif convert == '5':
        InchesToCm()
        
    else:
        print('That is not an option.')

#This is where I define my conversion functions.
        
def milesToKm():
    miles = float(input('Input the number of miles to convert to kilometers '))
    if miles >= 0:
        kilometers = miles * 1.6
        print(miles, ' miles is equal to ', format(kilometers, ',.2f'), \
        ' in kilometers.')
    else:
        print('Sorry. You cannot convert a negative number.')
    
def FahToCel():
    degrees_f = float(input('Input the number of degrees fahrenheit to convert to degrees celsius '))
    if degrees_f <= 1000:
        degrees_c = (degrees_f - 32) * 5/9
        print(degrees_f, ' degrees fahrenheit is equal to ', \
        format(degrees_c, ',.2f'), ' in celsius.')
    else:
        print('Sorry. You cannot convert a temperature larger than 1000 degrees.')

def GalToLit():
    gallons = float(input('Input the number of gallons to convert to liters '))
    if gallons >= 0:
        liters = gallons * 3.9
        print(gallons, ' gallons is equal to ', format(liters, ',.2f'), \
        ' in liters.')
    else:
        print('Sorry. You cannot convert a negative number.')
        
def PoundsToKg():
    pounds = float(input('Input the number of pounds to convert to kilograms '))
    if pounds >= 0:
        kilograms = pounds * 0.45
        print(pounds, ' pounds is equal to ', format(kilograms, ',.2f'), ' in kilograms.')
    else:
        print('Sorry. You cannot convert a negative number.')
        
def InchesToCm():
    inches = float(input('Input the number of inches to convert to centimeters '))
    if inches >= 0:
        c_meters = inches * 2.54
        print(inches, ' inches is equal to ', format(c_meters, ',.2f'), ' in centimeters.')
    else:
        print('Sorry. You cannot convert a negative number.')

main()

# I wanted to give an option to convert something else here, but I guess I need a loop?
# It only gives me the option one time.

print(' ')
cont=input('Would you like convert something else? Enter Y or N. ')
if cont=='Y' or cont == 'y':
    print(' ')
    main()

elif cont=='N' or cont == 'n':
    print(' ')
    print('Thank you for using the conversion program!')

