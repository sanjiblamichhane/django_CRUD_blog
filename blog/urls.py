from django.urls import path
# we want to display our blogs on home page.
# So basically, we are importing BlogListView class from views.py of this app to point to the home url
from .views import (
	 BlogListView,
	 BlogDetailView, 
	 BlogCreateView, 
	 BlogUpdateView, #new
	 BlogDeleteView,
	)

urlpatterns = [
	path('post/<int:pk>/delete/',
		BlogDeleteView.as_view(), name='post_delete'),
	path('post/<int:pk>/edit/',
		BlogUpdateView.as_view(), name='post_edit'), #new
	path('post/new/', BlogCreateView.as_view(), name='post_new'), #added by sl
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #new
	path('', BlogListView.as_view(), name = 'home'),
]
