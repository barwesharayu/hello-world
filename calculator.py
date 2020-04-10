while True:
	print('Welcome to calculator')
	print('1. Addition')
	print('2. Subtraction')
	print('3. Multiplication')
	print('4. Division')
	print('Print "quit" to cancel')
	user_input= input(":")

	if user_input == "quit":
		break

	elif user_input == 'Addition':
		num1 = float(input('Enter the first number: '))
		num2 = float(input('Enter the second number: '))
		res = str(num1+num2)
		print('Result is '+ res)

	elif user_input == 'Subtraction':
		num1 = float(input('Enter the first number: '))
		num2 = float(input('Enter the second number: '))
		res = str(num1-num2)
		print('Result is '+ res)

	elif user_input == 'Multiplication':
		num1 = float(input('Enter the first number: '))
		num2 = float(input('Enter the second number: '))
		res = str(num1*num2)
		print('Result is '+ res)

	elif user_input == 'Division':
		num1 = float(input('Enter the first number: '))
		num2 = float(input('Enter the second number: '))
		res = str(num1%num2)
		print('Result is '+ res)
	
	else:
		print('Unknown input')	
		
			