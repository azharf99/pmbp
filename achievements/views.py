from .models import Achievement, AchievementPhoto, AchievementProgram
from rest_framework import serializers, viewsets, permissions
# Create your views here.


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = ['url', 'achievement_category', 'certificate', 'champion_class', 'champion_level', \
                  'champion_name', 'competition_date', 'competition_level', 'competition_name', 'competition_organizer', \
                    'competition_type', 'created_at', 'id', 'school', 'updated_at']

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all().order_by('-created_at')
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAdminUser]



class AchievementPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AchievementPhoto
        fields = ['url', 'achievement', 'achievement_id', 'achievement_notes', 'achievement_photo', 'created_at', 'id', 'updated_at']

class AchievementPhotoViewSet(viewsets.ModelViewSet):
    queryset = AchievementPhoto.objects.all().order_by('-created_at')
    serializer_class = AchievementPhotoSerializer
    permission_classes = [permissions.IsAdminUser]



class AchievementProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AchievementProgram
        fields = ['url', 'achievement', 'achievement_program', 'created_at', 'id', 'notes', 'program_date', 'students', 'updated_at']

class AchievementProgramViewSet(viewsets.ModelViewSet):
    queryset = AchievementProgram.objects.all().order_by('program_date', 'achievement_program')
    serializer_class = AchievementProgramSerializer
    permission_classes = [permissions.IsAdminUser]
