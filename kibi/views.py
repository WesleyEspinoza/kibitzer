from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from kibi.models import Post


class PostListView(ListView):
    """ Renders a list of all posts. """
    model = Post

    def get(self, request):
        """ GET a list of posts. """
        posts = self.get_queryset().all()
        return render(request, 'list.html', {
          'posts': posts
        })

class PostDetailView(DetailView):
    """ Renders a specific post based on it's slug."""
    model = Post

    def get(self, request, slug):
        """ Returns a specific kibi post by slug. """
        post = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'post.html', {
          'post': post
        })
