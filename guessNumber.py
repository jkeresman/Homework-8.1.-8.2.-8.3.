
secretNumber = 5

guess = int(input("Guess a number: "))

if guess == secretNumber:
    print("Congratulations you've guessed right number")
else:
    print("Your guess was wrong, secret number is : {}".format(secretNumber))

