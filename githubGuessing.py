import random


print("="*50)
print("""		Guess the Secret Number!
You start out with 3 lives and you lose one with each wrong guess!""")
print("="*50)
print()


number = random.randint(1,20)


num_lives = 3

while num_lives > 0:
    print(f"Lives remaining: {num_lives}")
    
    
    guess = int(input("Please guess the secret number between 1 and 20: "))  
    
    
    if guess > number:
        print("Too high!")
        num_lives -= 1
    
    elif guess < number:
        print("Too low!")
        num_lives -= 1
        
    else:
        print("Congratulations! You guessed the secret number", number) 
        break  

if num_lives == 0:
    print(f"Better luck next time! The secret number was {number}") 