# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game to practice string manipulation, loops, conditionals, and basic user input handling in Python.

## 📝 Tasks

### 🛠️ Core Hangman (CLI)

#### Description
Create a command-line Hangman game that chooses a random word from a predefined list and lets the player guess one letter at a time until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Store a list of at least 10 candidate words and randomly select one (e.g., using `random.choice`).
- Display the current progress using underscores for hidden letters (e.g., `_ _ a _ _`).
- Accept a single-letter guess per turn via `input()` and update the progress for correct guesses.
- Track and display remaining incorrect attempts (suggested: 6 mistakes allowed).
- Track and display letters already guessed.
- End the game when the word is fully revealed (win) or attempts are exhausted (lose), and show the target word.

Example interaction (simplified):

```
_ _ _ _ _    Misses left: 6    Guessed: -
Guess a letter: a
_ a _ _ _    Misses left: 6    Guessed: a
Guess a letter: e
_ a _ _ _    Misses left: 5    Guessed: a, e
...
You win! The word was "magic".
```


### 🛠️ Polishing and Robustness

#### Description
Improve user experience and reliability with input validation and quality-of-life features.

#### Requirements
Completed program should:

- Treat guesses case-insensitively (e.g., `A` equals `a`).
- Validate input: accept only a single alphabetic character; prompt again otherwise.
- Handle repeated guesses gracefully without penalizing the player; notify that the letter was already tried.
- Ask the player if they want to play again when a round ends and restart without exiting the program.
