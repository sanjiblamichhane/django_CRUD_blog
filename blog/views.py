from django.views.generic import ListView, DetailView #new
from django.views.generic.edit import CreateView, UpdateView, DeleteView  #added by sl
from django.urls import reverse_lazy

#import Post from models
from .models import Post

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name='all_posts_list'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'
	context_object_name='indiv_post'

class BlogCreateView(CreateView):
	model = Post #database model
	template_name = 'post_new.html'
	fields = '__all__'

class BlogUpdateView(UpdateView): #new
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body'] # we're assuming the author is not changing

class BlogDeleteView(DeleteView):
	model = Post #database model
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home') # we used reverse_lazy() as opposed to reverse() becasuse it wont execute the url redirect until out view has finished deleteting the blog post.
