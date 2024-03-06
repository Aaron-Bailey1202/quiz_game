Here's a README template for your quiz program:

---

# Quiz Game

This is a simple Python quiz game where users are presented with a series of true/false questions and have to answer them. The program tracks the user's score and provides feedback on their performance.

## Features

- **Question Bank**: The program includes a predefined set of true/false questions stored in the `question_data` list.
- **User Interaction**: Users can answer questions interactively via the command line interface.
- **Scoring**: The program keeps track of the user's score and provides feedback on their performance at the end of the quiz.
- **Question Randomization**: Questions are presented in random order to keep the quiz engaging and challenging.

## Usage

1. **Running the Program**: Execute the `main.py` file using Python 3.
   ```
   python main.py
   ```
2. **Answering Questions**: Follow the prompts to answer each true/false question.
3. **Scoring**: At the end of the quiz, the program displays the user's final score.

## File Structure

- `main.py`: Main Python script containing the quiz game logic.
- `question_model.py`: Defines the `Question` class to represent individual quiz questions.
- `quiz_brain.py`: Contains the `QuizBrain` class responsible for managing the quiz flow, including question presentation and scoring.
- `data.py`: Stores the list of true/false questions in the `question_data` variable.
