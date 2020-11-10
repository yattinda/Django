from django.shortcuts import render, redirect

from .forms import PostCreateForm
from .models import Post

def post_list(request):
    #dict
    context = {
        'post_list': Post.objects.all(),
    }
    return render(request, 'post_template/post_list.html', context)

def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            #urls.pyのapp_nameとname
            return redirect('post:post_list')
    else:
        form = PostCreateForm()
    return render(request, 'post_template/post_create.html', {'form': form})
