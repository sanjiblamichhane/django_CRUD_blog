from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
	form_class = UserCreationForm #built in feature
	success_url = reverse_lazy('login') # use reverse_lazy instead of reverse bc for all generic class-based views URLs are not loaded when the file is imported
	template_name = 'signup.html'