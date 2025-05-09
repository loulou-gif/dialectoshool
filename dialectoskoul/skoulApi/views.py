from django.db import models
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from .services import serviceSendEmail
from .serializers import *
from .models import *

# Create your models here.

class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# class StudentsViews(viewsets.ModelViewSet):
#     # queryset = UserJoinRules.objects.filter(rules=UserJoinRules.rules)
#     serializer_class = UserJoinRuleSerializers
    
#     def get_queryset(self):
#         queryset = UserJoinRules.objects.all()
#         name_filter = self.request.query_params.get('students', None)
#         if name_filter:
#             queryset = queryset.filter(rules=name_filter)
#         return queryset
    
class UserJoinRules(viewsets.ModelViewSet):
    queryset = UserJoinRules.objects.all()
    serializer_class = UserJoinRuleSerializers
    
    
class RulesViewSet(viewsets.ModelViewSet):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    
class ResponsesViewset(viewsets.ModelViewSet): 
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerialiser
    
class QuestionsViewset(viewsets.ModelViewSet): 
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerialiser
    
class TestsViewset(viewsets.ModelViewSet): 
    queryset = Test.objects.all()
    serializer_class = TestsSerialiser
    
class diffusionListViewset(viewsets.ModelViewSet): 
    queryset = diffusionList.objects.all()
    serializer_class = diffusionListSerializers
    
class categorieViewset(viewsets.ModelViewSet): 
    queryset = categorie.objects.all()
    serializer_class = categorieSerializers

class CoursViewset(viewsets.ModelViewSet): 
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    
class CoursesAffectationViewset(viewsets.ModelViewSet): 
    queryset = CoursAffectation.objects.all()
    serializer_class = CoursesAffectationSerializer


class LevelClassViewSet(viewsets.ModelViewSet):
    queryset = LevelClass.objects.all()
    serializer_class = LevelClassSerializers
class APILogEntryViewset(viewsets.ModelViewSet):
    queryset = APILogEntry.objects.all().order_by('-created_at')
    serializer_class = APILogEntrySeriallizers
    
class PackViewset(viewsets.ModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = PackSerializers
    
class ClassesViewset(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    
class affectationStudentViewset(viewsets.ModelViewSet): 
    queryset = AffectationStudents.objects.all()
    serializer_class = AffectationStudentSerializers
    
class diffusionListViewset(viewsets.ModelViewSet): 
    queryset = diffusionList.objects.all()
    serializer_class = diffusionListSerializers
    

class EmailViewset(viewsets.ModelViewSet):
    queryset = EmailSendModel.objects.all()
    serializer_class = SendMailSerializers
    
    def perform_create(self, serializer):
        email_obj = serializer.save()
        serviceSendEmail(email_obj)
        
        
    @action(detail=True, methods=['post'])
    def resend(self, request, pk=None):
        email_obj = self.get_object()
        success = serviceSendEmail(email_obj)
        
        
        if success:
            return Response({'message': 'Email envoyé avec succes'}, status=status.HTTP_200_OK)
        return Response({"Statut": "Echec de l'envoie de mail"}, status=status.HTTP_400_BAD_REQUEST)
    

