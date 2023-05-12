from apps.trucks.models import TruckModel, Trip


def get_truck_models() -> list[tuple]:
    return TruckModel.objects.only('id', 'name').values_list('id', 'name')


def get_truck_trips(model: str | None = None):
    qs = Trip.objects.select_related(
        'truck', 'truck__model'
    ).filter(date_ended=None)

    if model:
        qs = qs.filter(truck__model__id=model)

    return qs
