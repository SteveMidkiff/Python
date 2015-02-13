# Imports my conversion functions
import convert


# This is where I define the main function.

def main():
    miles, kilometers = convert.milesToKm()
    print(miles, ' miles is equal to ', format(kilometers, ',.2f'), \
        ' in kilometers.')
    print()
    degrees_f, degrees_c = convert.FahToCel()
    print(degrees_f, ' degrees fahrenheit is equal to ', \
        format(degrees_c, ',.2f'), ' in celsius.')
    print(' ')
    gallons, liters = convert.GalToLit()
    print(gallons, ' gallons is equal to ', format(liters, ',.2f'), \
    ' in liters.')
    print(' ')    
    pounds, kilograms = convert.PoundsToKg()
    print(pounds, ' pounds is equal to ', format(kilograms, ',.2f'), \
          ' in kilograms.')
    print(' ')
    inches, c_meters = convert.InchesToCm()
    print(inches, ' inches is equal to ', format(c_meters, ',.2f'), ' in centimeters.')
    print(' ')
    print('Thank you for using the conversion program!')

main()


