from .models import Extracurricular, StudentExtracurricular
from rest_framework import serializers, viewsets, permissions
# Create your views here.


class ExtracurricularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Extracurricular
        fields = ['url', 'created_at', 'extracurricular_description', 'extracurricular_logo', 'extracurricular_name', \
                  'extracurricular_schedule', 'extracurricular_teacher', 'extracurricular_time', 'extracurricular_type', \
                    'id', 'slug', 'updated_at']

class ExtracurricularViewSet(viewsets.ModelViewSet):
    queryset = Extracurricular.objects.all().order_by('extracurricular_type', 'extracurricular_name')
    serializer_class = ExtracurricularSerializer
    permission_classes = [permissions.IsAdminUser]


class StudentExtracurricularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentExtracurricular
        fields = ['url', 'academic_year', 'created_at', 'extracurricular', 'extracurricular_id', 'id', 'student', 'student_id', 'updated_at']

class StudentExtracurricularViewSet(viewsets.ModelViewSet):
    queryset = StudentExtracurricular.objects.all().order_by('extracurricular', 'student')
    serializer_class = StudentExtracurricularSerializer
    permission_classes = [permissions.IsAuthenticated]
