def welcome():
    print('''
Welcome to Calculator
''')

def calculate():
	operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')

	number_1 = int(input('Enter your first number: '))
	number_2 = int(input('Enter your second number: '))

# Addition
	if operation == '+':
		print('{} + {} = '.format(number_1, number_2))
		print(number_1 + number_2)

# Subtraction
	elif operation == '-':
		print('{} + {} = '.format(number_1, number_2))
		print(number_1 + number_2)

# Multiplication
	elif operation == '*':
		print('{} * {} = '.format(number_1, number_2))
		print(number_1 * number_2)

# Division
	elif operation == '/':
		print('{} / {} = '.format(number_1, number_2))
		print(number_1 / number_2)

# Power
	elif operation == '**':
		powerTotal = 1
		count = number_2
		while (count >= 0):
	    		print(count)
			newPower = number_1*number_1
			count = count - 1
			powerTotal = powerTotal * newPower
		print('{} ^ {} = '.format(number_1, number_2))
		print(powerTotal)

# Modulo
	elif operation == '%':
		print('{} % {} = '.format(number_1, number_2))
		print(number_1 % number_2)

	else:
	   	print('You have not typed a valid operator, please run the program again.')
	again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

welcome()
calculate()


