# This is where I define the main function.
def main():
    name, email = getinfo()
    milesToKm(name)
    FahToCel(name)
    GalToLit(name)
    PoundsToKg(name)
    InchesToCm(name)
    print(' ')
    print('Thank you for using the conversion program!')

#This is where I define my conversion functions.
        
def milesToKm(name): 
    miles = float(input('Input the number of miles to convert to kilometers '))
    if miles >= 0:
        kilometers = miles * 1.6
        print(name, ', the number you entered, ', miles, ' miles is equal to ', \
        format(kilometers, ',.2f'), ' in kilometers.', sep='')
        print(' ')
    else:
        print('Sorry, ', name, '. You cannot convert a negative number.', sep='')
        print(' ')
    
def FahToCel(name):
    degrees_f = float(input('Input the number of degrees fahrenheit to convert to degrees celsius '))
    if degrees_f <= 1000:
        degrees_c = (degrees_f - 32) * 5/9
        print(name, ', the number you entered, ', degrees_f, ' degrees fahrenheit is equal to ', \
              format(degrees_c, ',.2f'), ' in celsius.', sep='')   
        print(' ')
    else:
        print('Sorry, ', name, '. You cannot convert a temperature larger than 1000 degrees.', sep='')
        print(' ')

def GalToLit(name):
    gallons = float(input('Input the number of gallons to convert to liters '))
    if gallons >= 0:
        liters = gallons * 3.9
        print(name, ', the number you entered, ', gallons, ' gallons is equal to ', \
              format(liters, ',.2f'), ' in liters.', sep='')
        print(' ')
    else:
        print('Sorry, ', name, '. You cannot convert a negative number.', sep='')
        print(' ')
        
def PoundsToKg(name):
    pounds = float(input('Input the number of pounds to convert to kilograms '))
    if pounds >= 0:
        kilograms = pounds * 0.45
        print(name, ', the number you entered, ', pounds, ' pounds is equal to ', \
              format(kilograms, ',.2f'), ' in kilograms.', sep='')
        print(' ')
    else:
        print('Sorry, ', name, '. You cannot convert a negative number.', sep='')
        print(' ')
        
def InchesToCm(name):
    inches = float(input('Input the number of inches to convert to centimeters '))
    if inches >= 0:
        c_meters = inches * 2.54
        print(name, ', the number you entered, ', inches, ' inches is equal to ', \
              format(c_meters, ',.2f'), ' in centimeters.', sep='')
        print(' ')
    else:
        print('Sorry, ', name, '. You cannot convert a negative number.', sep='')
        print(' ')

def getinfo():
    name = input('Please provide your name: ')
    email = input('Please provide your email address: ')
    while '@' not in email:
        print('That is not a valid email address.')
        email = input('Please provide your email address: ')
    return name, email


main()


