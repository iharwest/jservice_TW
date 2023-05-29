from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionSerializer
from .utils import get_questions, question_obj, validate_int


class QuestionView(APIView):
    """
    Вью для модели Question.
    """
    def post(self, request):
        request_number = request.data['questions_num']
        if validate_int(request_number):
            data = get_questions(request_number)
            serializer = QuestionSerializer(data=data, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                previous_question = Question.objects.all().order_by('-id')[:1]
                response = question_obj(previous_question)
                return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
