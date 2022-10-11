from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import Upload
# Create your views here.


def index(request):
    return render(request, 'index.html')


def index1(request):
    if request.method == 'POST':
        title = request.POST['title']
        upload1 = request.FILES['Upload']
        object = Upload.objects.create(title=title, Upload=upload1)
        object.save()
    context = Upload.objects.all()
    return render(request, 'index1.html', {'context': context})
