class Questions:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        
    def check_answer(self, answer):
        return self.answer == answer
    
class Quiz:
    def __init__(self, question):
        print("12")
        self.question =  question
        self.score = 0
        self.index = 0
        
    def increase_score(self):
        self.score += 100
        
        
    def getQuestionInfo(self):
        return self.question[self.index]
    
    def showQuestion(self):
        question_info = self.getQuestionInfo()
        
        print(f"Soru {self.index + 1}: {question_info.question}")
        
        for i in question_info.choices:
            print("-->" + i)
            
        user_answer = input("Lütfen cevap gir.")
        
        if question_info.check_answer(user_answer):
            print("Tebrikler, doğru bildiniz.")
            self.increase_score()
        else:
            print(f"Üzgünüz cevap yanlıs. Doğru Cevap {question_info}")
            
        self.index += 1
        
        if len(self.question) != self.index:
            self.showQuestion()
            
        else:
            print(f"Tebrikler, {self.score} ile yarısmayı bitirdiniz.")