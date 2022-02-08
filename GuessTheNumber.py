# Hi everbody, it's a just kidding. A simple game.

from random import randint

def guess(x):
  random = randint(1, x)
  attempt = 0
  guess = 0
  while guess != random:
    guess = int(input(f'Choose a number between 1 and {x}: '))

    if guess > random:
      print('Sorry, try again. Too high.')
    
    if guess < random:
      print('Sorry, try again. Too low')
    
    attempt += 1
  
  return attempt



def computer(limit):
  random2 = randint(1, limit)
  attempt2 = 0
  computering = randint(1, limit)
  while computering != random2:

    if computering > random2:
      computering -= 1

    if computering < random2:
      computering += 1

    attempt2 += 1
  
  return attempt2

def game(x):
  A = guess(x)
  B = computer(x)
  print(f'\nThe computer tried {B} time(s), while the player tried {A} time(s).')

  if int(A) < int(B):
    print('\nYessirr, you won, nice work!')
    print()
  
  elif int(A) > int(B):
    print('\nSorry, you did lose. But do not be unhappy, you can play again!')
    print()

  else:
    print('\nWoooow, you almost got the computer, play it again to beat it')
    print()