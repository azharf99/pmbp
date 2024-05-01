from .models import Menu
from rest_framework import serializers, viewsets, permissions
# Create your views here.


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['url', 'created_at', 'icon_data', 'id', 'menu_arabic_title', 'menu_title', 'updated_at', 'url_name']

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('menu_title')
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]
