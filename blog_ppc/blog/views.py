import markdown

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from PIL import Image

from .models import BlogPost, Author

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = "blog_posts"
	model = BlogPost

	def get_queryset(self):
		return BlogPost.objects.order_by('-published')

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['author_list'] = Author.objects.order_by('-author')
		return context


class PostView(DetailView):
    model = BlogPost
    context_object_name = "blog_post"
    template_name = 'post.html'


class PublishedByView(ListView):
	template_name = 'published_by.html'
	context_object_name = "blog_posts"
	model = BlogPost

	def get_queryset(self):
		return BlogPost.objects.order_by('-published')

	def get_context_data(self, **kwargs):
		self.author = get_object_or_404(BlogPost, name=self.args[1])
		context['published_by'] = BlogPost.objects.filter(author=self.author)
		return context

	'''

	def get_queryset(self):
		self.author = get_object_or_404(BlogPost, name=self.args[0])
		return BlogPost.objects.filter(author=self.author) '''