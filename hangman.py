import random
won = 0
lost = 0
print("H A N G M A N")
menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
while menu != 'quit':
    if menu == 'play':
        words = ['python', 'java', 'swift', 'javascript']
        word = random.choice(words)
        print('')
        life = 8  # counter
        letter = ' '
        letters = ''
        alf = list('abcdefghijklmnopqrstuvwxyz ')
        while life > 0:
            k = 0
            for letter in word:
                if letter in letters:
                    print(letter, end='')
                else:
                    print('-', end='')
                    k += 1
            print('')
            if k == 0:
                won += 1
                print(f"You guessed the word {word}!")
                print("You survived!")
                break
            letter = input("Input a letter:")
            if len(letter) > 1 or letter == "":
                print("Please, input a single letter.")
                print('')
                continue
            if letter not in alf:
                print("Please, enter a lowercase letter from the English alphabet.")
                print('')
                continue
            if letter in letters:
                print("You've already guessed this letter.")
                continue
            letters += letter
            if letter not in word:
                life -= 1
                print("That letter doesn't appear in the word.")
            if life == 0:
                print("You lost!")
                lost += 1
            print('')
    if menu == 'results':
        print(f"You won: {won} times.")
        print(f"You lost: {lost} times.")
    if menu == 'exit':
        exit()
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
