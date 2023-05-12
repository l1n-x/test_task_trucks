from django.views.generic import TemplateView

from apps.trucks.services.truck import get_truck_models, get_truck_trips


class TrucksView(TemplateView):
    template_name = 'trucks/trucks.html'

    def get(self, request, *args, **kwargs):
        model = request.GET.get('model', None)

        context = self.get_context_data()
        context.update({'truck_models': get_truck_models()})
        context.update({'truck_trips': get_truck_trips(model=model)})

        return self.render_to_response(context=context)
