# This is where I define the main function.
def main():
    milesToKm()
    FahToCel()
    GalToLit()
    PoundsToKg()
    InchesToCm()
    print(' ')
    print('Thank you for using the conversion program!')

#This is where I define my conversion functions.
        
def milesToKm():
    miles = float(input('Input the number of miles to convert to kilometers '))
    if miles >= 0:
        kilometers = miles * 1.6
        print(miles, ' miles is equal to ', format(kilometers, ',.2f'), \
        ' in kilometers.')
        print(' ')
    else:
        print('Sorry. You cannot convert a negative number.')
        print(' ')
    
def FahToCel():
    degrees_f = float(input('Input the number of degrees fahrenheit to convert to degrees celsius '))
    if degrees_f <= 1000:
        degrees_c = (degrees_f - 32) * 5/9
        print(degrees_f, ' degrees fahrenheit is equal to ', \
        format(degrees_c, ',.2f'), ' in celsius.')
        print(' ')
    else:
        print('Sorry. You cannot convert a temperature larger than 1000 degrees.')
        print(' ')

def GalToLit():
    gallons = float(input('Input the number of gallons to convert to liters '))
    if gallons >= 0:
        liters = gallons * 3.9
        print(gallons, ' gallons is equal to ', format(liters, ',.2f'), \
        ' in liters.')
        print(' ')
    else:
        print('Sorry. You cannot convert a negative number.')
        print(' ')
        
def PoundsToKg():
    pounds = float(input('Input the number of pounds to convert to kilograms '))
    if pounds >= 0:
        kilograms = pounds * 0.45
        print(pounds, ' pounds is equal to ', format(kilograms, ',.2f'), ' in kilograms.')
        print(' ')
    else:
        print('Sorry. You cannot convert a negative number.')
        print(' ')
        
def InchesToCm():
    inches = float(input('Input the number of inches to convert to centimeters '))
    if inches >= 0:
        c_meters = inches * 2.54
        print(inches, ' inches is equal to ', format(c_meters, ',.2f'), ' in centimeters.')
        print(' ')
    else:
        print('Sorry. You cannot convert a negative number.')
        print(' ')

main()


