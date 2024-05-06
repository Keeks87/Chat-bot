from django.http import HttpResponse
from .bot import get_bot_response

def chat_response(request):
    user_input = request.GET.get('message')
    return HttpResponse(get_bot_response(user_input))
