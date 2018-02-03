import csv

class Question():
    def __init__(self, question, choices, answers):
        self.question = question
        self.choices = choices
        self.answers = answers
    def save_answer(self, q_answer):
        self.q_answer = q_answer
    def eval_answer(self):
        if ((ord(self.q_answer) >= 65) and (ord(self.q_answer) <= (65 + len(self.choices) - 1))):
            if ((ord(self.q_answer) - 65) == int(self.answers)):
                return 1
            else:
                return 0
        elif ((ord(self.q_answer) >= 97) and (ord(self.q_answer) <= (97 + len(self.choices) - 1))):
            if ((ord(self.q_answer) - 97) == int(self.answers)):
                return 1
            else:
                return 0
        else:
            return -1

def load(path):
    questions = []
    with open(path, 'rb') as m_file:
        reader = csv.reader(m_file)
        contents = reader
        for row in contents:
            question = ""
            choices = []
            answers = ""
            for i in range(0, len(row)):
                if i == 0:
                    question = row[i]
                if i > 0 and "ANS|" not in row[i]:
                    choices.append(row[i])
                if "ANS|" in row[i]:
                    answers = row[i].split("ANS|")[1]
            questions.append(Question(question, choices, answers))
    return questions

questions = load("example.csv")
print "Questions loaded: " + str(len(questions))
score = 0
for q in questions:
    print q.question
    choice = 65
    for c in q.choices:
        print chr(choice) + ") " + c
        choice += 1
    answer = raw_input("> ")
    q.save_answer(answer)
    if q.eval_answer() == 1:
        score += 1
    print ""
print "Score: " + str(score) + "/" + str(len(questions))

    
            
    

