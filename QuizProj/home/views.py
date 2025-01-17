from django.shortcuts import render,redirect,get_object_or_404
from . models import *


# Create your views here.

def home(request):
    return render(request,'base.html')

def quiz(request):
    quizes=Quiz.objects.filter(is_ready_to_publish=True)
    context={'quizes':quizes}
    return render(request,'index.html',context)

def quiz_details(request,quiz_id):
    quiz=get_object_or_404(Quiz, id=quiz_id)
    questions=quiz.questions.all()
    context={'quiz':quiz,'questions':questions}
    return render(request,'quiz.html',context)
    