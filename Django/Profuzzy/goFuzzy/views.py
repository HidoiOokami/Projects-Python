from django.shortcuts import render

from blog.models import Post


# Rotas para os Cards
def accidents(request):
    return render(request, 'partials/accidents.html')

def calculation(request):
    return render(request, 'partials/calculation.html')

def lessons(request):
    return render(request, 'partials/lessons.html')

def mobility(request):
    return render(request, 'partials/mobility.html')

def search(request):
    return render(request, 'partials/search.html')

def system(request):
    return render(request, 'partials/system.html')

def training(request):
    return render(request, 'partials/training.html')

def transport(request):
    return render(request, 'partials/transport.html')

def story(request):
    return render(request, 'partials/fuzzy.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'partials/blog.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'partials/post.html', {'post': post})
