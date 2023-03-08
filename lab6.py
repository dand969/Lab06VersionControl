def encode(string):
	encoded = ''
	for i in string:
		encoded+=str((int(i)+3)%10)
	return encoded

def main():
	option_chosen = 0
	while option_chosen!=3:
		print('''Menu 
-------------
1. Encode 
2. Decode 
3. Quit\n\n''')
		option_chosen = int(input('Please enter an option: '))
		if option_chosen==1:
			password = input('Please enter your password to encode: ')
		if option_chosen in [1,2,3]:
			if option_chosen==1:
				encoded_password = encode(password)
				print('Your password has been encoded and stored!\n')
			if option_chosen==2:
				print('The encoded password is {}, and the original password is {}.\n'.format(encoded_password,password))
		else:
			print('Invalid option. Try again!\n')

if __name__=='__main__':
	main()