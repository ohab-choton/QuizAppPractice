from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'base.html')
@login_required(login_url='login')
def quiz(request):
    quizes=Quiz.objects.filter(is_ready_to_publish=True)
    context={'quizes':quizes}
    return render(request,'quizCategoy.html',context)

@login_required(login_url='login')
def quiz_details(request,quiz_id):
    quiz=get_object_or_404(Quiz, id=quiz_id)
    questions=quiz.questions.all()
    context={'quiz':quiz,'questions':questions}
    return render(request,'quiz.html',context)
@login_required(login_url='login')
def submit(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()
        erro_message = None  # Initialize the error message variable

        for question in questions:
            choice_id = request.POST.get(f"question_{question.id}", None)
            if choice_id:
                choice = get_object_or_404(Choice, id=choice_id)
                UserResponse.objects.create(
                    user=request.user, quiz=quiz, question=question, choice=choice
                )
            else:
                # Stop processing further and show the error
                messages.error(request, "You missed a question")
                context = {'quiz': quiz, 'questions': questions}
                return render(request, 'quiz.html', context)

        messages.success(request, "Quiz Submitted Successfully")
        return redirect('quizDetailsPage',quiz_id=quiz_id)

    return redirect('quizDetailsPage', quiz_id=quiz_id)