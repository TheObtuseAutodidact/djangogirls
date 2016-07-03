from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    # return "Hello, World!"
    return render(request, 'blog/post_list.html', {})
