from django.shortcuts import render
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})


def timer(request):
    return render(request, 'components/timer.html', {
        "time": timezone.now()
    })
