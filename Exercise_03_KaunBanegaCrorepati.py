import random
class KBC:
    def __init__(self):
        self.questions = [
            {
                "question" : "Question 1 : \n Which country has the largest proven oil reserves in the world?",
                "options" : ["A)Saudi Arabia", "B)Venezuela", "C) Canada", "D)Iraq"],
                "answer" : "B"
            },
            {
                "question": "Question 2 : \n Which two countries are involved in the long-standing conflict over the region of Kashmir?",
                "options": ["A) India and Pakistan", "B) Israel and Palestine", "C) Russia and Ukraine",
                            "D) China and Taiwan"],
                "answer": "A"
            },
            {
                "question": "Question 3 : \n Which international organization is primarily responsible for maintaining global peace and security?",
                "options": ["A) NATO", "B) WTO", "C) UN", "D) IMF"],
                "answer": "C"
            },
            {
                "question": "Question 4 : \n What was the main reason behind Brexit, the United Kingdom's decision to leave the European Union?",
                "options": ["A) Economic disagreements", "B) Immigration control", "C) Environmental policies",
                            "D) Military alliances"],
                "answer": "B"
            },
            {
                "question": "Question 4 : \n Which sea is at the center of territorial disputes involving China, Vietnam, the Philippines, and other countries?",
                "options": ["A) Black Sea", "B) Baltic Sea", "C) South China Sea", "D) Caspian Sea"],
                "answer": "C"
            }
        ]
        self.prizes = ["1,000", "2,000", "5,000", "10,000", "20,000", "40,000", "80,000", "1,60,000", "3,20,000", "6,40,000", "12,50,000", "25,00,000", "50,00,000", "1 Crore", "7 Crores"]
        self.current_question_index = 0
        self.selected_questions = random.sample(self.questions,min(len(self.prizes),len(self.questions)))

    def ask_questions(self):
        question = self.selected_questions[self.current_question_index]
        print(f"Question for {self.prizes[self.current_question_index]}: {question['question']}")
        for option in question['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        return answer == question['answer']

    def play(self):
        print("WELCOME TO KAUN BANEGA CROREPATI! ")
        while self.current_question_index < len(self.selected_questions):
            if self.ask_questions():
                print("Correct Answer!")
                self.current_question_index += 1
                if self.current_question_index == len(self.selected_questions):
                    print(f"Congratulations! You've won {self.prizes[-1]}!")
            else:
                print("Wrong Answer! Game Over.")
                break

if __name__ == "__main__":
    game = KBC()
    game.play()