from .models import Grade
from rest_framework import serializers, viewsets, permissions
# Create your views here.


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ['url', 'academic_year', 'created_at', 'grade', 'id', 'student', 'student_id', 'updated_at']

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all().order_by('student')
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]
