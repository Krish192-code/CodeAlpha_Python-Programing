import random

def hangman():
    List = ["python", "programming", "computer", "algorithm", "developer"]
    
    secret_word = random.choice(List)
    guessed_letters = []  
    correct_letters = []  
    incorrect_guesses = 0  
    max_incorrect = 6     
    display_word = ["_"] * len(secret_word)
    
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_incorrect} incorrect guesses allowed.")
    print(f"The word has {len(secret_word)} letters: {' '.join(display_word)}")
    
    while incorrect_guesses < max_incorrect and "_" in display_word:
        
        guess = input("\nEnter a letter: ").lower()
        
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            correct_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
            
            
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
        
        
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    
    
    if "_" not in display_word:
        print(f"\n🎉 Congratulations! You won! The word was '{secret_word}'")
    else:
        print(f"\n💀 Game Over! You've used all {max_incorrect} incorrect guesses.")
        print(f"The word was '{secret_word}'")


if __name__ == "__main__":
    hangman()