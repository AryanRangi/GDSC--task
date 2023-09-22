from Content import question_data
from Question_bank import backend
from proceeder import processing
bank = []
for q in question_data:
    text = q["backend"]
    question_answer = q["answer"]
    new = backend(text,question_answer)
    bank.append(new)

test = processing(bank)
while test.if_question_left():
    test.next_question()