# Define the main program
# Get employee name, longevity, sales and vacation days

def main():
    emp_name=str(input("Who's paycheck are we calculating today? "))
    longevity=int(input("How many months has the employee worked for SoftwarePirates? "))
    sales=float(input("How much did the employee have in sales this month? "))
    days_off=int(input("How many days off has the employee taken this month? "))
    commission=0.0
    bonus=0
    add_bonus=0
    deduct=0
    base_pay=2000
    gross_pay=0
    
# Calculate the gross paycheck
# Start with calculating the commission

    if sales >= 10000 and sales <= 100000:
        commission = sales * 0.02
    elif sales > 100000 and sales <= 500000:
        commission = sales * 0.15
    elif sales > 500000 and sales <= 1000000:
        commission = sales * 0.28
    elif sales > 1000000:
        commission = sales * 0.35

# Calculate the bonus

    if longevity > 3:
        if sales > 100000 and sales <= 500000:
            bonus = 1000
        elif sales > 500000 and sales <= 1000000:
            bonus = 5000
        elif sales > 1000000:
            bonus = 100000

# Calculate additional bonus

    if longevity > 60 and sales > 100000:
        add_bonus = 1000

# Calculate deduct

    if days_off > 3:
        deduct = 200

# Calculate gross paycheck

    gross_pay = base_pay + commission + bonus + add_bonus - deduct

# Print out the results

    print(' ')
    print(emp_name, ', who has been with the company for ', longevity, ' months,', sep='')
    print('has a base salary of $', base_pay, sep='')
    print('This month, ', emp_name, ' earned a commission of $', format(commission, ',.2f'), sep='')
    print('This month, ', emp_name, ' earned a bonus of $', format(bonus, ',.2f'), sep='')
    print('This month, ', emp_name, ' earned an additional bonus of $', format(add_bonus, ',.2f'), sep='')
    print('This month, ', emp_name, ' had a deduction of $', format(deduct, ',.2f'), sep='')
    print('And ' , emp_name, "'s total pay for this month is $", format(gross_pay, ',.2f'), sep='')
    
    
          
    
        


main()


    
