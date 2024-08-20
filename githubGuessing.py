from random import randint as r

print("="*50)
print("""        Guess the Secret Number!
You start out with 10 lives and you lose one with each wrong guess!""")
print("="*50)
print()

def game():
    number = r(1, 30)
    num_lives = 10
    
    while num_lives > 0:
        print(f"Lives remaining: {num_lives}")

        try:
            guess = int(input('Please guess the secret number between 1 and 30: '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 30.')
            continue

        if guess < 1 or guess > 30:
            print('Invalid range. Please choose 1 - 30')
            continue
        elif guess > number:
            print('Too high!')
        elif guess < number:
            print('Too low!')
        else:
            print(f'Congratulations! You have guessed the secret number: {number}')
            break
        
        num_lives -= 1
    
    if num_lives == 0:
        print(f"Better luck next time! The secret number was {number}") 

game()
