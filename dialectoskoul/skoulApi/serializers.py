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
        
        
class PackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = '__all__'
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        
class AffectationStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AffectationStudents
        fields = '__all__'
        
class ResponsesSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = '__all__'
class QuestionsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
class CoursesAffectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursAffectation
        fields = '__all__'
        
class TestsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
class categorieSerializers(serializers.ModelSerializer):
    class Meta:
        model = categorie
        fields = '__all__'
        
class diffusionListSerializers(serializers.ModelSerializer):
    emails = serializers.SerializerMethodField() 

    class Meta:
        model = diffusionList
        fields = ['id', 'name', 'emails', 'recipients'] 

    def get_emails(self, obj):
        return list(obj.recipients.values_list('email', flat=True))


class SendMailSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailSendModel
        fields = '__all__'
class APILogEntrySeriallizers(serializers.ModelSerializer):
    class Meta:
        model = APILogEntry
        fields = '__all__'