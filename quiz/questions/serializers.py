from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Question.
    """
    class Meta:
        model = Question
        fields = '__all__'
