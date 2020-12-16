import random

secretnumber=random.randint(1,20)
print('I am thinking the number is between 1 and 20')

for guessing in range(1,7):
	print('Take a guess')
	guess=int(input())

	if guess < secretnumber:
		print('Your guess is too low')
	elif guess > secretnumber:
		print('Your guess is too high')
	else:
		break

if guess==secretnumber:
	print('Good job! you guessed my number in' + str(guessing) + 'guesses')
else:
	print('Nope.The number I was thinking of was' + str(secretnumber))
