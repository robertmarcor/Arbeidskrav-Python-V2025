from questions import QUESTIONS
from utils import colored_text, lineDiv


def ask_input():
    allowed_answers = {"a", "b", "c", "d"}
    while True:
        user_answer = input(f"{lineDiv()} {colored_text('Your Answer: ', 'cyan')}")
        if user_answer.strip().lower() in allowed_answers:
            break
        else:
            print(f"{lineDiv()} {colored_text('Invalid input. Please enter A, B, C, or D.', 'red')}")
    return user_answer

def ask_questions():
    score = 0
    wrong_questions = []
    right_questions = []

    print(colored_text("╔══════════════════════════[QUIZ]════════════════════════╗", "magenta"))
    print(f"{lineDiv()} This is a multiple choice quiz")
    print(f"{lineDiv()} You need to answer either:")
    print(f"{lineDiv()} A, B, C or D (lowercase is fine)")
    print(f"{lineDiv()} There will be a series of questions")
    print(f"{lineDiv()} and you will be evaluated after finishing")

    for q in QUESTIONS:
        print(colored_text(f"╠══════════════════════════[Q{q['id']}]══════════════════════════", "magenta"))
        print(f"{lineDiv()} \033[4mQ{q['id']}. {q['question']}\033[0m")
        
        for choice, text in q["choices"].items():
            print(f"{lineDiv()} {choice}) {text}")
            
        print(colored_text("╠════════════════════════════════════════════", "magenta"))
        user_answer = ask_input()
        if user_answer.lower() == q["answer"].lower():
            score += 1
            right_questions.append((q["id"], q["question"], user_answer, q["choices"][user_answer.upper()], q["answer"], q["choices"][q["answer"]]))
        else:
            wrong_questions.append((q["id"], q["question"], user_answer, q["choices"][user_answer.upper()], q["answer"], q["choices"][q["answer"]]))

    display_score(score, wrong_questions, right_questions)
    
    

def display_score(score, wrong_answers, right_answers):
    print(colored_text("╠══════════════════════════[Score]══════════════════════════╗", "magenta"))
    print(f"{lineDiv()} You got {colored_text(str(score), 'cyan')} out of {colored_text(str(len(QUESTIONS)), 'cyan')}")
    if score > 5:
        print(f"{lineDiv()} Very good!")
    else:
        print(f"{lineDiv()} Practice more!")

    print("")
    print(f"{lineDiv()} You answered these incorrectly:\n")
    for q_id, text, user_answer, wrong_text, q_answer, correct_text in wrong_answers:
        print(f"{lineDiv()} {q_id}. {text}")
        print(f"{lineDiv()} Correct answer was: {colored_text(q_answer + ') ' + correct_text, 'green')}")
        print(f"{lineDiv()} You entered: {colored_text(user_answer.upper() + ') ' + wrong_text , 'red')}")
        print("")
    print(f"{lineDiv()} You answered these correctly:\n")
    for q_id, text, user_answer, right_text, q_answer, correct_text in right_answers:
        print(f"{lineDiv()} {q_id}. {text}")
        print(f"{lineDiv()} Correct answer was: {colored_text(q_answer + ') ' + correct_text, 'green')}")
        print(f"{lineDiv()} You entered: {colored_text(user_answer.upper() + ') ' + right_text , 'cyan')}")
        print("")
        
    print(colored_text("╚═══════════════════════════════════════════════════════════╝", "magenta"))