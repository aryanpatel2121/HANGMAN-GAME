import random

words = ["goodnoon", "crystal", "flutter", "mango", "whistle",
    "orbit", "jungle", "quartz", "napkin", "zebra"]
chosen_word = random.choice(words)
correct_letters = []
chance = 6
game_over = False
print(chosen_word)
while not game_over:
    guess_letter = input("Enter your guess: ").lower()
    
    if guess_letter in chosen_word:
        print("Right!")
        correct_letters.append(guess_letter)
    else:
        print("Wrong!")
        chance -= 1
        print(f"Chances left: {chance}")


    # Build the display string
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\n" + display + "\n")

    # Check win condition
    if all(letter in correct_letters for letter in set(chosen_word)):
        print("You win!! The word was:", chosen_word)
        game_over = True
    if chance== 0:
        print("game over you lose !!")
