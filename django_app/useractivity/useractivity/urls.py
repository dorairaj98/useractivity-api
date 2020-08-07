
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from data_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.users.as_view()),
]
