import random
from pathlib import Path

WORDLIST = Path("wordlist.txt")
words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
    ]

def instructions(version):
    print("Okay! Here are some basic instructions! Skip? (Y/N)")
    skip = input()
    while skip != 'y' and skip != 'Y' and skip != 'n' and skip != 'N':
        print("Not a valid answer. Please type Y or N")
        skip = input()
    if skip == 'n' or skip == 'N':
        print("Just like real wordle, you get 6 tries to guess a 5 letter word.")
        print("You type in your word and we'll tell you which letters are correct and in the right spot,")
        print('and which letters are correct but in the wrong spot.')
        print('For the letters that are wrong, you won\'t get a message')
    elif skip == 'y' or skip == 'Y':
        print('Okay! Skipping...')
    print('We have two versions! One with symbols and one without. Which would you like? Type 1 for symbols and 2 for without.')
    version = int(input())
    while version != 1 and version != 2:
        print('Not a valid answer. Please type 1 or 2.')
        version = int(input())
    return version

def symbol_instruct():
    print('💚 means you have the correct letter in the correct place. ')
    print('💛 means it\'s the right letter but in the wrong place.')
    print('❌ means it\'s the wrong letter.')
    print('Let\'s get this started!')

def get_random_word():
    return random.choice(words)

def game_over(word):
    print(f'Out of guesses! The word was {word}! Maybe next time!')

def sym_game_over(word):
    print(f"Out of guesses!😣 The word was {word}. Maybe next time!❣️")

def splay():
    word = get_random_word()
    correct_sym = "💚"
    place_sym = "💛"
    wrong_sym = "❌"
    for guess_num in range(1,7):
        my_list = []
        guess = input(f"Guess {guess_num}: ").upper()

        if guess == word:
            print('Congrats You won!🎉🎊🥇')
            break
        
        correct_letters = {letter for letter,correct in zip(guess, word) if letter == correct}
        misplaced_letters = set(guess) & set(word) - correct_letters
        wrong_letters = set(guess) - set(word)
        
        for item in guess:
            if item in correct_letters:
                my_list.append(correct_sym)
            elif item in misplaced_letters:
                my_list.append(place_sym)
            elif item in wrong_letters:
                my_list.append(wrong_sym)

        print(" ".join(my_list))

    else:
        sym_game_over(word)

def nplay():
    word = get_random_word()

    for guess_num in range(1,7):
        guess = input(f'Guess {guess_num}: ').upper()
        if guess == word:
            print('Correct! Congrats, you\'ve won!')
            break

        correct_letters = {letter for letter,correct in zip(guess, word) if letter == correct}
        misplaced_letters = set(guess) & set(word) - correct_letters
        wrong_letters = set(guess) - set(word)

        print('Correct letters: ', ", ".join(sorted(correct_letters)))
        print('Misplaced letters: ' , ", ".join(misplaced_letters))
        print("Wrong letters: " , ",".join(wrong_letters))
    else:
        game_over(word)


print('Welcome to my Wordle Game! ')
print('Play? (Y/N)')
play = input()

while play != 'y' and play != 'Y' and play != 'n' and play != 'N':
    print('Not a valid entry. Please enter Y or N')
    play = input()
version = 0
if play == 'y' or play == 'Y':
    version = instructions(version)
    
    if version == 1:
        symbol_instruct()
        splay()
    elif version == 2:
        print('Let\'s get this started!')
        nplay()
        
    print('Thanks for playing!')
elif play == 'n' or play == 'N':
    print('Awe too bad. Goodbye!')
    exit()
