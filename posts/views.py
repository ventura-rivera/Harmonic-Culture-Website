from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM POSTS!')

    return render(request, 'posts/index.html')
