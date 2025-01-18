from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title=models.CharField(max_length=100)
    is_ready_to_publish=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Quizzes"
class Question(models.Model):
    text=models.CharField(max_length=200)
    quiz=models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    def __str__(self):
        return self.text
class Choice(models.Model):
    text=models.CharField(max_length=200)
    question=models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    def __str__(self):
        return self.text
    
class UserResponse(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE)
def __str__(self) -> str:
        return  f"{self.user.username}'s response to  - {self.question.text} in- {self.quiz.title} is {self.choice.text}"

def calculate_score(self):
    total_score=sum(choice.score for choice in self.choices.all())
    return total_score