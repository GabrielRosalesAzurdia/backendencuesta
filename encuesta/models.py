from django.db import models

class Answer(models.Model):
    name = models.CharField(max_length=50, null=True)
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.IntegerField()
    question5 = models.IntegerField()
    question6 = models.IntegerField()
    question7 = models.IntegerField()
    question8 = models.IntegerField()
    question9 = models.IntegerField()
    question10 = models.IntegerField()
    question11 = models.IntegerField()
    question12 = models.IntegerField()
    question13 = models.IntegerField()
    question14 = models.IntegerField()
    question15 = models.IntegerField()

    def getQuestion(self, number):
        if(number == 1):
            return self.question1
        if(number == 2):
            return self.question2
        if(number == 3):   
            return self.question3
        if(number == 4):
            return self.question4
        if(number == 5):
            return self.question5
        if(number == 6):
            return self.question6
        if(number == 7):
            return self.question7
        if(number == 8):
            return self.question8
        if(number == 9):
            return self.question9
        if(number == 10):
            return self.question10
        if(number == 11):
            return self.question11
        if(number == 12):
            return self.question12
        if(number == 13):
            return self.question13
        if(number == 14):
            return self.question14
        if(number == 15):
            return self.question15
