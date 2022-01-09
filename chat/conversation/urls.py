from django.urls import path
from .views import *
urlpatterns = [
    path('chat/', chat, name='chat'),
    path('message/', message, name='message'),
    path('profiles/', profiles, name='profiles'),
    path('form/', CreateView.as_view(), name='form'),
    # path('profiles/<int:id>', profiles_redirect, name='profiles'),
]