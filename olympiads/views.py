from .models import OlympiadField, OlympiadStudent, OlympiadReport
from rest_framework import serializers, viewsets, permissions
# Create your views here.


class OlympiadFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OlympiadField
        fields = ['url', 'created_at', 'id', 'olympiad_field_name', 'olympiad_field_schedule',\
                   'olympiad_field_teacher', 'olympiad_field_teacher_id', 'slug', 'updated_at']

class OlympiadFieldViewSet(viewsets.ModelViewSet):
    queryset = OlympiadField.objects.all().order_by('olympiad_field_name')
    serializer_class = OlympiadFieldSerializer
    permission_classes = [permissions.IsAdminUser]



class OlympiadStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OlympiadStudent
        fields = ['url', 'created_at', 'id', 'olympiad_field', 'olympiad_field_id', 'olympiad_student', 'olympiad_student_id', 'updated_at']

class OlympiadStudentViewSet(viewsets.ModelViewSet):
    queryset = OlympiadStudent.objects.all().order_by('olympiad_field', 'olympiad_student')
    serializer_class = OlympiadStudentSerializer
    permission_classes = [permissions.IsAuthenticated]



class OlympiadReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OlympiadReport
        fields = ['url', 'created_at', 'id', 'notes', 'olympiad_field', 'olympiad_field_id', 'olympiad_practice_date',\
                   'olympiad_teacher', 'olympiad_teacher_id', 'photo', 'students', 'updated_at']

class OlympiadReportViewSet(viewsets.ModelViewSet):
    queryset = OlympiadReport.objects.all().order_by('-olympiad_practice_date')
    serializer_class = OlympiadReportSerializer
    permission_classes = [permissions.IsAuthenticated]