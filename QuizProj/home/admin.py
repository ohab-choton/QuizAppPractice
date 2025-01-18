from django.contrib import admin
from django.db.models import Sum  # Import Sum
from .models import Choice, Question, Quiz, UserResponse

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('quiz',)

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'score', 'choice', 'total_score', 'quiz_title')
    list_filter = ('quiz', 'user')
    search_filter = ('user__username',)

    def quiz_title(self, obj):
        return obj.quiz.title

    def score(self, obj):
        return obj.choice.score if obj.choice else 0

    def total_score(self, obj):
        user_responses = UserResponse.objects.filter(user=obj.user, quiz=obj.quiz)
        total = user_responses.aggregate(total_score=Sum('choice__score'))['total_score']
        return total if total else 0

admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)
