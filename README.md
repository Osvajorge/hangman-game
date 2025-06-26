# 🎯 Hangman Game

A classic word-guessing game implemented in Python with bilingual support (English/Spanish). Test your vocabulary and deduction skills in this terminal-based recreation of the timeless hangman game!

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Language Support](https://img.shields.io/badge/Languages-EN%20|%20ES-orange.svg)

</div>

## 🎮 Game Preview

<div align="center">
  
![Hangman Game Screenshot](https://i.imgur.com/LiEvCyv.png)

*Main game interface showing the classic hangman drawing*

![Language Selection](https://i.imgur.com/GT7lPx1.png)
*Bilingual support - Choose between English and Spanish*

</div>

## ✨ Features

- 🌍 **Bilingual Support** - Play in English or Spanish
- 🎨 **ASCII Art** - Classic hangman drawing that updates with each wrong guess
- 📝 **Word Categories** - Diverse vocabulary from different topics
- ⚡ **Terminal-Based** - Lightweight, no additional dependencies required
- 🔄 **Replay Option** - Play multiple rounds without restarting
- 📊 **Game Statistics** - Track your wins and losses

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Terminal/Command Prompt

### Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/osvajorge/hangman_game.git
   cd hangman_game
   ```

2. **Run the game**
   ```bash
   python hangman.py
   ```

3. **Choose your language and start playing!**

## 🎯 How to Play

1. Select your preferred language (English/Spanish)
2. The game will display blanks representing the letters in the hidden word
3. Guess letters one at a time
4. Correct guesses reveal the letter's position(s) in the word
5. Wrong guesses add a body part to the hangman drawing
6. Win by guessing the complete word before the drawing is finished!
7. You have **6 wrong guesses** before the game ends

## 🛠️ Technical Details

### Game Logic
- **Word Selection**: Random selection from predefined word lists
- **Input Validation**: Ensures only valid single letters are accepted
- **Game State Management**: Tracks guessed letters, remaining attempts, and win/loss conditions
- **Bilingual Implementation**: Separate word dictionaries for each supported language

### Code Structure
```python
# Main components:
├── Word lists (English & Spanish)
├── Hangman ASCII art stages
├── Game logic functions
├── Input validation
└── Main game loop
```

## 📁 Project Structure
```
hangman_game/
├── hangman.py          # Main game file
├── README.md           # Project documentation
└── assets/             # Game screenshots (if any)
```

<div align="center">
  
**Enjoy the game and happy coding! 🎉**

*Made with ❤️ by Jorge Osva*

</div>
