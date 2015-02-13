# This is where I define the main function.
def main():
    milesToKm()
    FahToCel()
    GalToLit()
    PoundsToKg()
    InchesToCm()
    print(' ')
    print('Thank you for using the conversion program!')

#This is where I define my conversion functions. I used a counter to limit the
# input validation. I hope it's ok I used break.
        
def milesToKm():
    times_to_try = 0
    miles = float(input('Input the number of miles to convert to kilometers '))
    while miles < 0:
        if times_to_try == 2:
            break
        print('Sorry. You cannot convert a negative number.')
        print(' ')
        miles = float(input('Input the number of miles to convert to kilometers '))
        times_to_try += 1
    if miles >= 0:
        kilometers = miles * 1.6
        print(miles, ' miles is equal to ', format(kilometers, ',.2f'), \
        ' in kilometers.')
        print(' ')
    else:
        print('Sorry. You only get three tries and you still cannot convert a negative number.')
        print(' ')

    
def FahToCel():
    times_to_try = 0
    degrees_f = float(input('Input the number of degrees fahrenheit to convert to degrees celsius '))
    while degrees_f > 1000:
        if times_to_try == 2:
            break
        print('Sorry. You cannot convert a temperature larger than 1000 degrees.')
        print(' ')
        degrees_f = float(input('Input the number of degrees fahrenheit to convert to degrees celsius '))
        times_to_try += 1    
    if degrees_f <= 1000:
        degrees_c = (degrees_f - 32) * 5/9
        print(degrees_f, ' degrees fahrenheit is equal to ', \
        format(degrees_c, ',.2f'), ' in celsius.')
        print(' ')
    else:
        print('Sorry. You only get three tries and you cannot convert a temperature larger than 1000 degrees.')
        print(' ')

def GalToLit():
    times_to_try = 0
    gallons = float(input('Input the number of gallons to convert to liters '))
    while gallons < 0:
        if times_to_try == 2:
            break
        print('Sorry. You cannot convert a negative number.')
        print(' ')
        gallons = float(input('Input the number of gallons to convert to liters '))
        times_to_try += 1
    if gallons >= 0:
        liters = gallons * 3.9
        print(gallons, ' gallons is equal to ', format(liters, ',.2f'), \
        ' in liters.')
        print(' ')
    else:
        print('Sorry. You cannot convert a negative number.')
        print(' ')
        
def PoundsToKg():
    times_to_try = 0
    pounds = float(input('Input the number of pounds to convert to kilograms '))
    while pounds < 0:
        if times_to_try == 2:
            break
        print('Sorry. You cannot convert a negative number.')
        print(' ')
        pounds = float(input('Input the number of pounds to convert to kilograms '))
        times_to_try += 1
    if pounds >= 0:
        kilograms = pounds * 0.45
        print(pounds, ' pounds is equal to ', format(kilograms, ',.2f'), ' in kilograms.')
        print(' ')
    else:
        print('Sorry. You only get three tries.')
        print(' ')
        
def InchesToCm():
    times_to_try = 0
    inches = float(input('Input the number of inches to convert to centimeters '))
    while inches < 0:
        if times_to_try == 2:
            break
        print('Sorry. You cannot convert a negative number.')
        print(' ')
        inches = float(input('Input the number of inches to convert to centimeters '))
        times_to_try += 1
    if inches >= 0:
        c_meters = inches * 2.54
        print(inches, ' inches is equal to ', format(c_meters, ',.2f'), ' in centimeters.')
        print(' ')
    else:
        print('Sorry. You only get three tries.')
        print(' ')

main()


