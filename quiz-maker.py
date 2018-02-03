import csv

class Question():
    def __init__(self, question, choices, answers):
        self.question = question
        self.choices = choices
        self.answers = answers
    def save_answer(self, q_answer):
        self.q_answer = q_answer
    def eval_answer(self):
        print self.q_answer
        print self.answers
        if (len(self.q_answer) == len(self.answers)):
            for ans in self.q_answer:
                if ((ord(ans) >= 65) and (ord(ans) <= (65 + len(self.choices) - 1))):
                    if (str(ord(ans) - 65) not in self.answers):
                        return 0
                elif ((ord(ans) >= 97) and (ord(ans) <= (97 + len(self.choices) - 1))):
                    if (str(ord(ans) - 97) not in self.answers):
                        return 0
                else:
                    return -1
            return 1
        else:
            return 0

def load(path):
    questions = []
    with open(path, 'rb') as m_file:
        reader = csv.reader(m_file)
        contents = reader
        for row in contents:
            question = ""
            choices = []
            answers = []
            for i in range(0, len(row)):
                if i == 0:
                    question = row[i]
                if i > 0 and "ANS|" not in row[i]:
                    choices.append(row[i])
                if "ANS|" in row[i]:
                    temp = row[i].split("ANS|")[1]
                    answers.append(temp)
            questions.append(Question(question, choices, answers))
    return questions

questions = load("1.csv")
print "Questions loaded: " + str(len(questions))
score = 0
for q in questions:
    print q.question
    choice = 65
    for c in q.choices:
        print chr(choice) + ") " + c
        choice += 1
    answer = raw_input("> ")
    answers = []
    if "," in answer:
        temp = answer.split(",")
        for t in temp:
            answers.append(t)
    else:
        answers.append(answer)
    q.save_answer(answers)
    if q.eval_answer() == 1:
        score += 1
    print ""
print "Score: " + str(score) + "/" + str(len(questions))

    
            
    

