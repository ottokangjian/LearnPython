print ("Welcome")
print ("Let's guess a number")

guess = input("input a number pls")
guess_int = int(guess)

if guess_int == 8:
	print ("Bingo!")
else:
	if guess_int > 8:
		print ("Too big")
	else:
		print ("Too small")
print ("Bye!")