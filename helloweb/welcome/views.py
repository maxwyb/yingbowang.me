from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Message
from .forms import PostMessageForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        latest_message_list = Message.objects.order_by('-id')
        post_form = PostMessageForm()
        context = {
            'latest_message_list': latest_message_list,
            'post_form': post_form
        }
        return render(request, 'welcome/index.html', context);

    if request.method == 'POST':
        form = PostMessageForm(request.POST)
        if form.is_valid():
            new_message = Message(message_text=form.cleaned_data['msg'])
            new_message.save()
            return HttpResponseRedirect('/');
