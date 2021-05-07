from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.
def post_list(requests):
    return render(requests, 'blog/post_detail.html', {})

