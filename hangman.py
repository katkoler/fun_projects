import random

word_file = "/usr/share/dict/words"

def pick_word():
	with open(word_file) as f:
		words = list(f)

	# words = ["banana's", 'dog']

	while True:
		word = random.choice(words).strip().lower()
		if len(word)>= 5:
			if word.isalpha():
				return word
		else: 
			print("Sorry, the answer was too easy, picking a new word.")

def print_answer(answer):
	print(" ".join(list(answer)))

def ask():
	while True:
		guess = input("Guess? ")
		if len(guess) != 1:
			print("Please guess a single letter.")
		elif not guess.isalpha():
			print("Please guess a letter.")
		else:
			break
	return guess

def update(target, answer, guess):
	if guess in target:
		new_answer = "" 
		for i, l in enumerate(target):
			if l == guess:
				new_answer += guess
			else:
				new_answer += answer[i]
		return new_answer, 0
	else:
		return answer, 1

HANGMANPICS = [''' ''','''

      
      
      
      
      
=========''','''

      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
     /|
=========''', '''
  +---+
  |   |
      |
      |
      |
     /|
=========''','''
  +---+
  |   |
  O   |
      |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
     /|
=========''']

input_string = "Want to play? y/n "

while input(input_string) == "y":
	input_string = "Want to play again? y/n "
	target = pick_word()
	answer = "_"*len(target)
	mistakes = 0
	sofar = []

	while True:
		print_answer(answer)
		print_answer(sofar)
		print("Mistakes:", mistakes)
		print(HANGMANPICS[mistakes])
		guess = ask()
		sofar.append(guess)
		answer, c = update(target, answer, guess)
		mistakes += c
		if mistakes >= len(HANGMANPICS)-1:
			print(HANGMANPICS[-1])
			print("DEAD!!! Game over.")
			print("The answer was:", target)
			break
		if answer == target:
			print_answer(answer)
			print("Well done.")
			break


