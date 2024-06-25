from django.contrib import admin
from django.urls import path, include, re_path
from character.api import viewsets as charactersviewset
from rest_framework import routers, permissions
from character import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

route = routers.DefaultRouter()


route.register(r'characters', charactersviewset.CharacterViewSet, basename="Characters")




schema_view = get_schema_view(
   openapi.Info(
      title="API's do sistema",
      default_version='v1',
      description="API's para estudo."
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.character_list, name='home'),
    path('apis/', include(route.urls)),
    path('chars/', views.character_list, name='character_list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
