from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Hypothesis(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    alg = models.CharField(max_length=2,
                           choices=[("NB", "Naive Bayes")])
    params = models.TextField()
