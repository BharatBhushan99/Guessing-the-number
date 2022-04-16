
import random 
import graphics

def show_prompts():

  print(graphics.logo)
  print("Welcome to the Number Guessing Game!")
  print("I have a number between 1 and 100. Can you guess it?")

  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  return difficulty 

def check_guess(user_guess, num):
  return num - user_guess

user_guess = None

guesss_count = -1

num = random.randint(1, 100)

difficulty = show_prompts()

if difficulty == "easy":
  guesss_count = 10
else:
  guesss_count = 5

while guesss_count > 0 and user_guess != num:
  print(f"You have {guesss_count} attempts remaining to guess the number.")
  
  user_guess = int(input("Make a guess: "))

  guess_result = check_guess(user_guess, num)

  if  guess_result == 0:
    print(f"You got it! The answer was {num}")
  else:
    guesss_count -= 1

    if guess_result < 0:
      print("Too high.")
    else:
      print("Too low.")

  if guesss_count == 0:
    print("You have run out of guesses, you lose.")






