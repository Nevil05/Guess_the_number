import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'enter your guess from 1 to {x}: '))
        if guess >= 1 and guess <= x:
            if guess > random_number:
                print('Your guess is too high!')
            elif guess < random_number:
                print('Your guess is too low!')
        else:
            print('Out of range choice!')
    print('Yayyy! You have guessed the number correctly!!!!')


guess(10)
