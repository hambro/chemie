from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class QuizTerm(models.Model):
    is_active = models.BooleanField(verbose_name='Aktiv Quiz')
    term = models.CharField(max_length=100, verbose_name='Quiz')

    def save(self, *args, **kwargs):
        if self.is_active:
            for quiz in QuizTerm.objects.exclude(pk=self.pk):
                quiz.is_active = False
                quiz.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.term


class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.ForeignKey(QuizTerm, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score)
