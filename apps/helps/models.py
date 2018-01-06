from django.db import models

# Create your models here.
class CommonProblem(models.Model):
    questionId = models.IntegerField(primary_key=True)
    questionName = models.CharField(max_length=300,default='')
    questionSolution = models.TextField(max_length=3000,default='')
class SystemRule(models.Model):
    ruleId = models.IntegerField(primary_key=True,default=10000000)
    ruleDetail = models.CharField(max_length=300,default='')