from django.shortcuts import render
from django.utils import timezone
from .models import Post
# from django.http import HttpResponse

# Create your views here.
def post_list(request):
    # return "Hello, World!"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = { 'posts': posts }
    return render(request, 'blog/post_list.html', context)
