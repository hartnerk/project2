from django.db import models

# Create your models here.
class MailingList(models.Model):
        # fields of the model
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)   
    message = models.CharField(max_length=1000)   
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.name


class SurveyQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1000)

    def __str__(self):
        return self.question

class SurveyAnswer(models.Model):
    question = models.ForeignKey("SurveyQuestion", on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.answer