from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rules(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"
    
class LevelClass(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}"
    
class UserJoinRules(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rules = models.ForeignKey(Rules, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.rules.name if self.rules else 'No Role'}"
    
class Classes(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.OneToOneField(LevelClass,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.level.name}"
    
    
class AffectationStudents(models.Model):
    classroom = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student = models.OneToOneField(User, on_delete=models.CASCADE)

class EmailSendModel(models.Model):
    subject = models.CharField(max_length=20)
    message = models.TextField()
    from_email = models.EmailField()
    to_email = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)
    criticality = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.subject} - {self.from_email} -> {self.to_email}"