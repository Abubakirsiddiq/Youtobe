from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from app1.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Bu loyha Youtube",
      contact=openapi.Contact(email="Nabiyev Abubakirsiddiq: <nabiyevabubakirsiddiq@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('accountlar/', AccountCreate.as_view()),
    path('account/<int:pk>/', Account.as_view()),
    path('videolar/', VideoCreate.as_view()),
    path('video/<int:pk>/', Video.as_view()),
    path('pleylistlar/', PleylistCreate.as_view()),
    path('pleylist/<int:pk>/', Pleylist.as_view()),
    path('obunalar/', ObunaCreate.as_view()),
    path('obuna/<int:pk>/', Obuna.as_view()),
    path('likelar/', LikeCreate.as_view()),
    path('like/<int:pk>/', Like.as_view()),
    path('historylar/', HistoryCreate.as_view()),
    path('history/<int:pk>/', History.as_view()),
]

