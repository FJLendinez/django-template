from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.core.cache import cache

# Create your views here.
def index(request):
    return render(request, "pages/index.html", {})


def timer(request):
    return render(request, "components/timer.html", {"time": timezone.now()})


def send_test_email(request):
    subject, from_email, to = "hello", "from@example.com", "to@example.com"
    text_content = "This is an important message."
    html_content = "<p>This is an <strong>important</strong> message.</p>"
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("<strong>Mail sent</strong>")

def store_in_cache(request):
    value = cache.get('from-cache')
    if not value:
        cache.set('from-cache', "Yes", timeout=3)
        value = "No"
    return HttpResponse(value)
