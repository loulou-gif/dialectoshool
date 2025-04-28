from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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
    level = models.ForeignKey(LevelClass,on_delete=models.CASCADE, related_name="classes")
    def __str__(self):
        return f"{self.name} - {self.level.name}"
    
    
class AffectationStudents(models.Model):
    classroom = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    
class diffusionList(models.Model):
    name=models.CharField(max_length=50)
    email = models.ManyToManyField(User)

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
    
    
# class APILogEntry(models.Model):
#     path = models.CharField(max_length=500)
#     method = models.CharField(max_length=10)
#     user = models.CharField(max_length=50)
#     Statut = models.CharField(max_length=10)
#     body = models.CharField(max_length=2500)
#     body = models.DateField(auto_now=False, auto_now_add=False)
    
    
User = get_user_model()

class APILogEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    path = models.CharField(max_length=500)  # L'URL appelée
    method = models.CharField(max_length=10)  # GET, POST, PUT, DELETE
    status_code = models.IntegerField()  # 200, 404, 500...
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    request_body = models.TextField(null=True, blank=True)  # Corps envoyé par l'utilisateur
    duration = models.FloatField(help_text="Durée de la requête en secondes")
    created_at = models.DateTimeField(auto_now_add=True)  # Date/heure où la requête a été faite

    def __str__(self):
        return f"{self.method} {self.path} ({self.status_code})"