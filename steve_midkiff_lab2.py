
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
        

    elif convert == '4':
        pounds = float(input('Input the number of pounds to convert to kilograms '))
        kilograms = pounds * 0.45
        print(pounds, ' pounds is equal to ', format(kilograms, ',.2f'), ' in kilograms.')

    elif convert == '5':
        inches = float(input('Input the number of inches to convert to centimeters '))
        c_meters = inches * 2.54
        print(inches, ' inches is equal to ', format(c_meters, ',.2f'), ' in centimeters.')

    else:
        print('That is not an option.')

    print('Thank you for using the conversion program!')


def milesToKm():
    miles = float(input('Input the number of miles to convert to kilometers '))
    kilometers = miles * 1.6
    print(miles, ' miles is equal to ', format(kilometers, ',.2f'), \
    ' in kilometers.')

def FahToCel():
    degrees_f = float(input('Input the number of degrees fahrenheit to convert to degrees celsius '))
    degrees_c = (degrees_f - 32) * 5/9
    print(degrees_f, ' degrees fahrenheit is equal to ', \
    format(degrees_c, ',.2f'), ' in celsius.')

def GalToLit():
    gallons = float(input('Input the number of gallons to convert to liters '))
    liters = gallons * 3.9
    print(gallons, ' gallons is equal to ', format(liters, ',.2f'), \
    ' in liters.')
        
main()
