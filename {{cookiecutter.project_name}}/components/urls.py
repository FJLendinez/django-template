from django.urls import path
from .timer.timer import TimerComponent

urlpatterns = [
    path('timer/', TimerComponent.as_view()),
]