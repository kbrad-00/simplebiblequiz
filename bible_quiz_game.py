# BibleQuest: A Scriptural Trivia Challenge

import random

# ---------------------------
# Unique Question Data
# ---------------------------
questions = [
    {
        "question": "Who was swallowed by a great fish?",
        "options": ["A. Jonah", "B. Paul", "C. Peter", "D. Moses"],
        "answer": "A"
    },
    {
        "question": "What was turned into blood in Egypt?",
        "options": ["A. Milk", "B. Wine", "C. Water", "D. Oil"],
        "answer": "C"
    },
    {
        "question": "Which book contains the Ten Commandments?",
        "options": ["A. Genesis", "B. Exodus", "C. Leviticus", "D. Deuteronomy"],
        "answer": "B"
    },
    {
        "question": "Who led the Israelites into the Promised Land?",
        "options": ["A. Moses", "B. Aaron", "C. Joshua", "D. Samuel"],
        "answer": "C"
    },
    {
        "question": "Which apostle doubted Jesus' resurrection?",
        "options": ["A. John", "B. Peter", "C. Thomas", "D. James"],
        "answer": "C"
    },
    {
        "question": "What is the last book of the New Testament?",
        "options": ["A. Revelation", "B. Acts", "C. Jude", "D. Hebrews"],
        "answer": "A"
    },
    {
        "question": "Who interpreted Pharaoh's dreams?",
        "options": ["A. Joseph", "B. Daniel", "C. Moses", "D. Samuel"],
        "answer": "A"
    },
    {
        "question": "What did Jesus feed 5,000 people with?",
        "options": ["A. Fish and figs", "B. Bread and fish", "C. Bread and wine", "D. Loaves and grapes"],
        "answer": "B"
    },
    {
        "question": "What river did John the Baptist baptize people in?",
        "options": ["A. Jordan", "B. Nile", "C. Euphrates", "D. Tigris"],
        "answer": "A"
    },
    {
        "question": "What did God create on the first day?",
        "options": ["A. Earth", "B. Light", "C. Animals", "D. Plants"],
        "answer": "B"
    }
]

# ---------------------------
# Player Class
# ---------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increase_score(self):
        self.score += 1

# ---------------------------
# QuizGame Class
# ---------------------------
class QuizGame:
    def __init__(self, player, questions):
        self.player = player
        self.questions = random.sample(questions, 5)  # Select 5 unique questions

    def start(self):
        print(f"\nWelcome to BibleQuest, {self.player.name}!")
        print("You will be asked 5 unique questions. Let's test your Bible knowledge!\n")

        for i, question in enumerate(self.questions):
            prompt = f"\nQuestion {i+1}: {question['question']}\n"
            for option in question['options']:
                prompt += f"{option}\n"
            prompt += "Type your answer (A, B, C, or D): "

            answer = input(prompt).strip().upper()

            if answer == question['answer']:
                print("✅ Correct!\n")
                self.player.increase_score()
            elif answer in ['A', 'B', 'C', 'D']:
                correct_option = [opt for opt in question['options'] if opt.startswith(question['answer'])][0]
                print(f"❌ Incorrect. The correct answer was: {correct_option}\n")
            else:
                print("❌ Invalid input. No points awarded.\n")

        print(f"Game Over! {self.player.name}, your final score is: {self.player.score}/5\n")

# ---------------------------
# Main Game Logic
# ---------------------------
def main():
    name = input("Enter your name: ")
    player = Player(name)
    game = QuizGame(player, questions)
    game.start()

if __name__ == "__main__":
    main()   
  
