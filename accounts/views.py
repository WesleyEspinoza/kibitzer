from django.shortcuts import render
from django.views import generic
from kibi.models import Post


class RegisterView(generic.CreateView):
    form_class = 'django.auth.forms.UserCreationForm'

    def get(self, request):
        return render(request, 'registration/signup.html')
