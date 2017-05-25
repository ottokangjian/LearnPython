import random
secret = random.randint(1,10)

print ("Welcome")
print ("Let's guess a number")

guess = input("input a number pls")
guess_int = int(guess)

while guess_int != secret:


	if guess_int == secret:
		print ("Bingo!")
	else:
		if guess_int > secret:
			print ("Too big")
		else:
			print ("Too small")
			
	guess = input("input a number pls")
	guess_int = int(guess)

			
print ("Bye!")
