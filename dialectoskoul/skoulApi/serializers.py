from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .services import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    # userdetail = UserDetailSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'
        
class UserJoinRuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserJoinRules
        fields = '__all__'
        
class LevelClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = LevelClass
        fields = '__all__'
        
        
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        
class AffectationStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AffectationStudents
        fields = '__all__'
        

class SendMailSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailSendModel
        fields = '__all__'