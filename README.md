# Rock-Paper-Scissors Game with Voice Output

## Description
This is a simple **Rock-Paper-Scissors** game implemented in Python. The game allows a player to compete against the computer. The program uses the `pyttsx3` library to provide voice output for an interactive experience.

## Features
- User vs Computer gameplay
- Random choice generation for the computer
- Input validation with error handling
- Voice feedback for user and computer choices using `pyttsx3`
- Option to play multiple rounds until the user chooses to exit

## Requirements
Ensure you have Python installed (Python 3.x recommended). You will also need the `pyttsx3` library, which can be installed using:

```bash
pip install pyttsx3
```

## How to Run the Game
1. Clone or download the script.
2. Open a terminal or command prompt in the script's directory.
3. Run the following command:

```bash
python rock_paper_scissors.py
```

4. Enter your choice (`rock`, `paper`, or `scissors`) when prompted.
5. The computer will randomly choose its move.
6. The winner will be announced both in text and voice.
7. Choose whether to play again (`y` for yes, `n` for no).

## Code Overview
- The script initializes a text-to-speech engine using `pyttsx3`.
- The player inputs their choice, which is validated.
- The computer randomly selects an option.
- The game determines the winner and provides voice feedback.
- The user is prompted to play again.

## Example Gameplay
```
Enter a choice (rock, paper, scissors): rock
Player: rock
Computer: scissors
You Win
Do you want to play again? (y/n): y
```

## Future Improvements
- Add GUI for better user experience.
- Implement difficulty levels.
- Allow multiplayer support.

## Author
Created by **[Boddu Sai Akhil]**.

