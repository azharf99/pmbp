from .models import Report
from rest_framework import serializers, viewsets, permissions
# Create your views here.


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ['url', 'academic_year', 'created_at', 'extracurricular', 'extracurricular_id',\
                   'id', 'report_date', 'report_note', 'report_photo', 'students', 'teacher', 'teacher_id', 'updated_at']

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-report_date')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
