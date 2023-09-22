class processing :
    def __init__(self,list) :
        self.question_no = 0
        self.score = 0
        self.question_list = list

    def if_question_left(self):
        return self.question_no < len(self.question_list)
    
    def next_question(self):
        current = self.question_list(self.question_no)
        self.question_no += 1
        user_answer = input(f"Q.(self.question_no): (current.backend): (True/False)")
        self.check(user_answer,current.answer)

    def check(self,user_answer,answer):
        if user_answer.lower() == answer.lower():
         self.score +=2

        else:
            self.score -=1
