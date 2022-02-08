# Hi everbody, it's a just kidding. A simple game.

from random import randint

def guess(x):
  random = randint(1, x)
  guess = 0
  while guess != random:
    guess = int(input(f'Choose a number between 1 and {x}'))
    
    if guess > random:
      print('Sorry, try again. Too high.')
    
    if guess < random:
      print('Sorry, try again. Too low')
      
   print('Yessirr, you did guess the number, nice work!')
   
   guess(7)
