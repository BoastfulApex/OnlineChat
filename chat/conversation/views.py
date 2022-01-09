import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import *

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
def chat(request):
    data = json.loads(request.body)

    user1 = User.objects.get(id=data['sender'])
    profile1, created = Profile.objects.get_or_create(user=user1)
    user2 = User.objects.get(id=data['resiver'])
    profile2, created = Profile.objects.get_or_create(user=user2)
    m1 = Message.objects.filter(user1=profile1).filter(user2=profile2)
    m2 = Message.objects.filter(user2=profile1).filter(user1=profile2)
    messages = []
    for mess in m1:
        messages.append(mess)
    for mess in m2:
        messages.append(mess)
    messages.sort(key=lambda x: x.time_to_int)
    send_data = []
    for message in messages:
        d = dict()
        d['text'] = message.text
        d['time'] = message.time
        d['image'] = message.user1.imageURL
        if message.user1 == Profile.objects.get(user=request.user):
            d['me'] = True
        else:
            d['me'] = False
        send_data.append(d)
    print(data['sender'])
    return JsonResponse({'messages':send_data})
def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'conversation/profiles.html', context)
def profiles_redirect(request, id):
    user1 = User.objects.get(id=request.user.id)
    profile1, created = Profile.objects.get_or_create(user=user1)
    user2 = User.objects.get(id=id)
    profile2, created = Profile.objects.get_or_create(user=user2)
    m1 = Message.objects.filter(user1=profile1).filter(user2=profile2)
    m2 = Message.objects.filter(user1=profile2).filter(user2=profile1)
    messageform = MessageForm()
    messages = []
    for i in m1:
        messages.append(i)
    for i in m2:
        messages.append(i)
    messages.sort(key=lambda x: x.time_to_int)
    if request.POST.get('text'):
        text = request.POST.get('text')
        message = Message.objects.create(user1=profile1, user2=profile2, text=text)
        message.save()
    context = {
        'forms': messageform,
        'messages': messages,
        'profile1': profile1,
        'profile2': profile2,
    }
    return render(request, 'conversation/chat.html', context)
def message(request):
    data = json.loads(request.body)

    user1 = User.objects.get(id=data['sender'])
    profile1, created = Profile.objects.get_or_create(user=user1)
    user2 = User.objects.get(id=data['resiver'])
    profile2, created = Profile.objects.get_or_create(user=user2)
    message = Message.objects.create(user1=profile1, user2=profile2, text=data['message'])
    message.save()
    return JsonResponse({'message': message.text, 'image': message.user1.imageURL, 'time': message.time})
class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('profiles')
    template_name = 'conversation/form.html'
    # form_cl   ass = ProfileForm