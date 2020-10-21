from django.shortcuts import render


# Create your views here.

def posts_list(request):
    n= ['alish', 'dsdsd', 'scsscc', 'scscscsc/']

    return render (request, 'blog/index.html', context={'name': n})
