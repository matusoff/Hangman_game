#Hangman
import random
import hangman_words
import hangman_stages


chosen_word = random.choice(hangman_words.word_list)    

display = []
for letter in chosen_word:
    display.append("_")
print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()
    
    if guess_letter in display:
        print(f"You've already passed {guess_letter}")
    if guess_letter not in chosen_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
   
        
#Check guessed letter
#position of guess_letter is from 0 to the length of chosen_word
    for position in range(len(chosen_word)):  
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter
    print(display)

    if guess_letter not in chosen_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose")                    
        
   
    if '_' not in display:
        end_of_game = True
        print("You win")
            
    print(hangman_stages.stages[lives])