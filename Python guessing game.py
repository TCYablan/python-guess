#Das ist ein Pthon Rate-Die-Zahl Spiel
import random

print('Hello. What is your name?')
name = input()

print('Well' + name + '. Guess a number betwenn 1 and 20.')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
      print('Take a guess')
      guess = int(input())

      if guess < secretNumber:
          print('Too low')
      elif guess > secretNumber:
          print('Too high')
      else:
          break # This condition is for the correct guess.

if guess == secretNumber:
      print('Good Job, '+ name + '. You guessed my number in ' + str(guessesTaken)+ ' guesses.')


