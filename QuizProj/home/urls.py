from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homePage'),
    path('quiz/', views.quiz, name='quizCategory'),
    path('quizd/<int:quiz_id>/', views.quiz_details, name='quizDetailsPage'),
    path('quizd/<int:quiz_id>/submit/', views.submit, name='sumbitPage'),
   
    ]