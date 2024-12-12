
def read_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        question = ""
        options = []
        answer = ""
        
        for line in lines:
            line = line.strip()
            if line.startswith("question"):
                if question:
                    questions.append((question, options, answer))
                question = line.split(":")[1].strip()
                options = []
                answer = ""
            elif line.startswith("Answer:"):
                answer = line.split(":")[1].strip()
            else:   
                options.append(line)
        
        # Append the last question
        if question:
            questions.append((question, options, answer))
    
    return questions

def ask_question(question, options, correct_answer):
    print(f"{question}")
    for option in options:
        print(option)
    
    user_answer = input("Your answer: ").strip().upper()
    if user_answer == correct_answer:
        return 1
    else:
        return 0

def save_score(score, filename):
    with open(filename, 'w') as file:
        file.write(f"Your final score is: {score}\n")

def main():
    questions = read_questions("questions.txt")
    score = 0

    for question, options, correct_answer in questions:
        score += ask_question(question, options, correct_answer)
    
    print(f"Your score is: {score}")
    save_score(score, "score.txt")

if __name__ == "__main__":
    main()
