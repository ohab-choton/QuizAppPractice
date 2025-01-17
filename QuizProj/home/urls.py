from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homePage'),
    path('quiz/', views.quiz, name='quizPage'),
    path('quizd/<int:quiz_id>/', views.quiz_details, name='quizDetailsPage'),
   
    ]