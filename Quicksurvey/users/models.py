from django.contrib.auth.models import User
from django.db import models


class Forms(models.Model):
    f_id = models.CharField(max_length=10, unique=True, help_text="Example FID27")
    form_name = models.CharField(max_length=100, blank=False, help_text="Enter name of Form")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter name of Form Creator")
    created_at = models.DateTimeField(auto_now_add=True)


class Questions(models.Model):
    q_id = models.CharField(max_length=10, unique=True, help_text="Example QID27")
    question = models.TextField(help_text="Enter your Question")
    opt1 = models.CharField(max_length=255, blank=False, help_text="Enter Option 1 for question ")
    opt2 = models.CharField(max_length=255, blank=False, help_text="Enter Option 2 for question ")
    opt3 = models.CharField(max_length=255, blank=False, help_text="Enter Option 3 for question ")
    opt4 = models.CharField(max_length=255, blank=False, help_text="Enter Option 4 for question ")
    answers = models.TextField(help_text="Enter Answer for Question")


class QuestionsInForms(models.Model):
    qif_id = models.CharField(max_length=10, unique=True, help_text="Example QFID27")
    form_fk = models.ForeignKey(Forms, on_delete=models.CASCADE, help_text="Select form Creator")
    question_fk = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.form_name

class Responses(models.Model):
    response_id = models.CharField(max_length=10, unique=True, help_text="Example RID27")
    response_mail = models.EmailField(unique=True, blank=False, null=False, help_text="Enter Email of Respondent")
    response = models.CharField(max_length=1000, blank=False, help_text="Response String")
    response_at = models.DateTimeField(auto_now_add=True)
