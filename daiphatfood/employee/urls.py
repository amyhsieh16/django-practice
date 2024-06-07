from django.urls import path, include
from employee import views as user_views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', user_views.EmployeeList.as_view()),
]

