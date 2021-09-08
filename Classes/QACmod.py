class Student:
    def __init__(self, name, age, student_class = "student"):
        self.name = name
        self.age = age
        self.student_class = student_class
    
    def average(self, score1, score2, score3):
        av_score = (score1 + score2 + score3) / 3
        return av_score
    