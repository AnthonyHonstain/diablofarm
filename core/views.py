from django.shortcuts import render, get_object_or_404
from .models import FarmGroup, FarmEvent
import datetime


def index(request):
    farm_groups = FarmGroup.objects.all().order_by('id')

    return render(request, 'index.html', {'farm_groups':farm_groups})

def farm_group(request, farm_group_id):
    farm_group = get_object_or_404(FarmGroup, pk=farm_group_id)
    farm_events = FarmEvent.objects.filter(group=farm_group)

    # This feels super yucky slapping this on the object.
    for farm_event in farm_events:
        farm_event.time_diff = (datetime.datetime.min + (farm_event.end_time - farm_event.start_time)).time()
        print(farm_event.time_diff)

    return render(request, 'farm_group.html', {'farm_group':farm_group, 'farm_events': farm_events})