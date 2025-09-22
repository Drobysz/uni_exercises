from random import randrange

def guess_num(input_val, rand_num):
    if '.' in input_val:
      print("\nYou entered a floating point number")
      return(guess_num(input(f"\nEnter your number again: "), rand_num))

    n = int(input_val)  
    if n not in range(1, 11):
      print("\nYour number went out of range")
      return(guess_num(input(f"\nEnter your number again: "), rand_num))

    if (n == rand_num):
      print("\n***You guessed***\nCongratulations!!!") 
      return True
    else:
      print(f"\n***You failed!***")
      return False
    

if __name__ == '__main__':
    greeting_text = '''
You\'re playing a game where you\'re supposed 
to guess a number in range from 1 to 10 with 3 tentatives
	'''
    rand_num = randrange(1, 11)
 
    exit() if guess_num(input(greeting_text + '\nEnter your 1st number: '), rand_num) else print("\nTry one more time")
    exit() if guess_num(input('\nEnter your 2nd number: '), rand_num) else print("Try one more time")
    exit() if guess_num(input('\nEnter your 3rd number: '), rand_num) else print("You lost")
	
