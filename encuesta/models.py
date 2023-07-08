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
