from django_components import component
from django_components import types as t


@component.register("timer")
class TimerComponent(component.Component):
    template: t.django_html = """
    <div class="text-blue-500">
        {{ time.isoformat }}
    </div>
    """

    def get_context_data(self, time):
        return {"time": time}

    def get(self, request):
        from django.utils import timezone
        return self.render_to_response(args=[timezone.now()])
