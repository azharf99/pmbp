"""
URL configuration for pmbp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import routers
from users.views import UserViewSet, GroupViewSet, TeacherViewSet, StudentViewSet
from reports.views import ReportViewSet
from olympiads.views import OlympiadFieldViewSet, OlympiadReportViewSet, OlympiadStudentViewSet
from menus.views import MenuViewSet
from grades.views import GradeViewSet
from extracurricular.views import ExtracurricularViewSet, StudentExtracurricularViewSet
from achievements.views import AchievementViewSet, AchievementPhotoViewSet, AchievementProgramViewSet
from utilities.seeds import seedDatabase

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'olympiads', OlympiadFieldViewSet)
router.register(r'olympiads_reports', OlympiadReportViewSet)
router.register(r'olympiads_students', OlympiadStudentViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'extracurricular', ExtracurricularViewSet)
router.register(r'extracurricular_students', StudentExtracurricularViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'achievements_photos', AchievementPhotoViewSet)
router.register(r'achievements_program', AchievementProgramViewSet)


def home(request):
    return HttpResponse("Home")


urlpatterns = [
    path('', home),
    path('seed/', seedDatabase),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)