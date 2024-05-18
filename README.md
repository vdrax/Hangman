# Hangman Game
  Welcome to the Hangman Game! This is a simple word guessing game developed in Python. The objective of the game is to guess the hidden word by suggesting letters within a limited number of attempts.

## Table of Contents :
  Features
  Installation
  Usage
  Contributing

### Features :
 1. Single-player game against the computer.
 2. Random word selection from a predefined list.
 3. Display of guessed letters and remaining attempts.
 4. Simple command-line interface.
 5. Case-insensitive input handling.
  
### Installation :
    Clone the repository: git clone https://github.com/vdrax/Hangman.git
    cd hangman-game
  
#### Usage :
    Run the game: python Hangman.py
  
#### How to Play :
 1. The computer will randomly select a word, and you need to guess it letter by letter.
 2. You have a limited number of attempts to guess the word.
 3. Each incorrect guess reduces your remaining attempts.
 4. If you guess the word correctly within the allowed attempts, you win!
 5. If you run out of attempts before guessing the word, you lose.
#### Example :
        Welcome to Hangman!
      You have 6 attempts remaining.
      _ _ _ _ _ _ _
      Guess a letter: e
      _ e _ _ _ _ _
      You have 5 attempts remaining.
      Guess a letter: a
      _ e _ _ _ a _
      ...

#### Contributing

  Contributions are welcome! Please follow these steps to contribute:
  
   1. Fork the repository.
   2. Create a new branch: git checkout -b my-feature-branch
   3. Make your changes and commit them: git commit -m 'Add new feature'
   4. Push to the branch: git push origin my-feature-branch
   5. Create a pull request describing your changes.
