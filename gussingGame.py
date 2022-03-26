correct_guess=9
count=0
limit=3
while count < limit:
    guess = int(input('Guess a number: '))
    count += 1
    if guess == correct_guess:
        print('Congratulations! YOU WON!!!')
        break
else:
    print('YOU LOST!!!! The number is', correct_guess)