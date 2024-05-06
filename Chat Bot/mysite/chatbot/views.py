from django.http import HttpResponse
from django.shortcuts import render
from .bot import get_bot_response

def chat_response(request):
    user_input = request.GET.get('message', '')
    if user_input:
        return HttpResponse(get_bot_response(user_input))
    else:
        return HttpResponse("No message provided", status=400)



def chat_view(request):
    return render(request, 'chatbot/chat.html')
