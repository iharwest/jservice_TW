import requests

from .models import Question

URL = 'https://jservice.io/api/random?count='


def validate_int(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        raise ValueError('Введите целое число!')


def get_questions(request_number):
    api_url = f'{URL}{request_number}'
    response = requests.get(api_url).json()
    data = []
    for result in response:
        data.append(
                {
                    'id_question': result['id'],
                    'question': result['question'],
                    'answer': result['answer'],
                    'created_at': result['created_at'],
                },
            )
    id_question = list()
    for id in data:
        id_question.append(id['id_question'])
    same_questions = Question.objects.filter(
        id_question__in=id_question).count()
    if same_questions > 0:
        get_questions(same_questions)
    return data


def question_obj(previous_question):
    if len(previous_question) > 0:
        response = previous_question.values('question')
        return response
    else:
        return {'question': []}
