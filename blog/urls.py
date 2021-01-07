from django.urls import path
# we want to display our blogs on home page.
# So basically, we are importing BlogListView class from views.py of this app to point to the home url
from .views import BlogListView, BlogDetailView

urlpatterns = [
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #new
	path('', BlogListView.as_view(), name = 'home'),
]