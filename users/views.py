from django.contrib.auth.models import User, Group
from .models import Teacher, Student
from rest_framework import serializers, viewsets, permissions
# Create your views here.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['url', 'created_at', 'id', 'is_active', 'is_online', 'teacher_address', 'teacher_code', \
                  'teacher_email', 'teacher_gender', 'teacher_id', 'teacher_job', 'teacher_name', 'teacher_phone', \
                    'teacher_photo', 'updated_at', 'user', 'user_id']


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('teacher_name')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'academic_year', 'created_at', 'id', 'student_address', 'student_batch', \
                  'student_birth_date', 'student_birth_place', 'student_class', 'student_email', \
                    'student_gender', 'student_name', 'student_nik', 'student_nis', 'student_nisn', \
                        'student_phone', 'student_photo', 'student_status', 'updated_at']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('student_class', 'student_name')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]