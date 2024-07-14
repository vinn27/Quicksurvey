from django.contrib import admin
from .models import Forms, Questions, QuestionsInForms, Responses

# Register your models here.

@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ['f_id', 'form_name', 'created_by', 'created_at']

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['q_id', 'question', 'opt1', 'opt2', 'opt3', 'opt4', 'answers']

@admin.register(QuestionsInForms)
class QuestionsInFormsAdmin(admin.ModelAdmin):
    list_display = ['qif_id', 'form_fk', 'question_fk']

@admin.register(Responses)
class ResponsesAdmin(admin.ModelAdmin):
    list_display = ['response_id', 'response_mail', 'response', 'response_at']

