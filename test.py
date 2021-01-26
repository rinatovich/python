from colorama import Fore, Back, Style


print(Fore.WHITE)
print(Style.NORMAL)
print(Back.BLUE)

operation = input('choose operation(+/-): ')

a = float(input('First number: '))
b = float(input('Second number: '))

print(Back.CYAN)
if operation == '+':
	c = a+b
	print('answer is equal to: ' + str(c) + '\n\n\n')
elif operation == '-':
	c = a-b
	print('answer is equal to: ' + str(c) + '\n\n\n')
else:
	print('undefined operation! \n\n\n')