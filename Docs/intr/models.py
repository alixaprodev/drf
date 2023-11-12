from django.db import models

# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    report = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    

class Question(models.Model):
    question_text = models.TextField()
    pub_date= models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete= models.CASCADE,related_name='choice')
    votes = models.IntegerField(default=0)

    
