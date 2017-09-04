from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.
def index(request):
    latest_message_list = Message.objects.order_by('-id')
    context = {
        'latest_message_list': latest_message_list
    }
    return render(request, 'welcome/index.html', context);
