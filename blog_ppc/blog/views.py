from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from PIL import Image

from .models import BlogPost, Author

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = "blog_posts"
	model = BlogPost

	def get_queryset(self):
		return BlogPost.objects.order_by('-published')