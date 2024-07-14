from rest_framework import serializers
from .models import Forms, Questions, QuestionsInForms, Responses
from django.contrib.auth.models import User


class FormSerializers(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = Forms
        fields = ['f_id', 'form_name', 'created_by', 'created_at', 'created_by_name']

    def get_created_by_name(self, obj):
        return obj.created_by.username


class QuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['q_id', 'question', 'opt1', 'opt2', 'opt3', 'opt4', 'answers']




class QuestionsInFormsSerializers(serializers.ModelSerializer):
    form_name = serializers.CharField(source='form_fk.form_name', read_only=True)

    class Meta:
        model = QuestionsInForms
        fields = ['qif_id', 'form_fk', 'question_fk', 'form_name']

    def get_form_name(self, obj):
        return obj.form_fk.form_name

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['form_fk'] = instance.form_fk.form_name
        return representation


class ResponsesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = ['response_id', 'response_mail', 'response', 'response_at']



