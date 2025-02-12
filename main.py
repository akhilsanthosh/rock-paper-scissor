import random
import pyttsx3

engine = pyttsx3.init()

choices = ["rock", "paper", "scissors"]
running = True 

def speak(text):
    engine.say(text)
    engine.runAndWait()

while running:
    player = None
    computer = random.choice(choices)

    try:
        player = input("Enter a choice(rock, paper, scissors): ")
        if player not in choices:
            raise Exception("Invalid choice")
    except Exception as e:
        print(e)
        speak(str(e))
        continue
    print(f"Player: {player}")
    speak(f"Player: {player}")
    
    print(f"Computer: {computer}")
    speak(f"Computer: {computer}")
    
    if player == computer:
        result = "It's a tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        result = "You Win"
    else: 
        result = "You lose"
    print(result)
    speak(result)
    
    play_again = input("Do you want to play again? (y/n):").lower()
    if play_again != "y":
        running  = False 
        speak("Thanks for playing")