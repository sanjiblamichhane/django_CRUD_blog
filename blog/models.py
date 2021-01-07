from django.db import models #importing models
from django.urls import reverse # added by sl

# Create your models here.
class Post(models.Model): #creating submodels
	title = models.CharField(max_length = 200) #limiting the character of the title to be 200
	author = models.ForeignKey( # we're using ForeignKey because it allows for many-to-one relationship --> i.e 
		'auth.User',
		on_delete = models.CASCADE, # for many-to-one relationship, we must also specify an on_delete option
	)
	body = models.TextField() #body of the blog will be text-type --> which will automatically expand based on the users' need

	def __str__(self):
		return self.title

	def get_absolute_url(self): #new
		return reverse('post_detail', args=[str(self.id)])
