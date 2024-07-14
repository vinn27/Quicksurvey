
from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('forms/', FormsCreateView.as_view(), name='form-list-create'),
    path('ques/', QuestionsCreateView.as_view(), name='ques-list-create'),
    path('qinf/', QuestionsInFormsCreateView.as_view(), name='queinfm-list-create'),
    path('resp/', ResponsesCreateView.as_view(), name='response-list-create'),

    path('forms/<int:pk>/', FormsView.as_view(), name='form-detail'),
    path('ques/<int:pk>/', QuestionsView.as_view(), name='questions-detail'),
    path('quinf/<int:pk>/', QuestionsInFormsView.as_view(), name='quesinfm-detail'),
    path('resp/<int:pk>/', ResponsesView.as_view(), name='resp-detail'),

    path('login/',login, name='login'),
]
