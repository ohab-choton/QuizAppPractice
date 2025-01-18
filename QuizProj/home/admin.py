from django.contrib import admin
from .models import Choice,Question,Quiz ,UserResponse

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2

class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline]
    list_display=('quiz',)


admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz)
admin.site.register(UserResponse)