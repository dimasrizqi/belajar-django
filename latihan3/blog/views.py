from django.shortcuts import render

# Create your views blog here.

from .models import Post


def index(request):
	#query ke databasenya
	posts = Post.objects.all()
	#untuk ngeluarin debugnya
	#print(posts)
	
	context = {
		'Title':'Blog',
		'Heading':'ini blog di my website',
		'Posts':posts,
	}

	return render(request,'blog/index.html',context)