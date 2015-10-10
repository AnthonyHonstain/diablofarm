from django.shortcuts import render, get_object_or_404
from .models import FarmGroup, FarmEvent
import datetime
from django.http.response import HttpResponseRedirect

from django import forms
from django.forms import ModelForm
from django.core.urlresolvers import reverse


class FarmEventForm(ModelForm):
    class Meta:
        model = FarmEvent
        fields = ['group', 'start_time', 'end_time'] #, 'death_breath_count', 'legendary_count', 'bounty_count', 'blood_shard_count', 'experience_count']
        widgets = {'group': forms.HiddenInput(),
                   'start_time': forms.DateTimeInput(attrs={'id':'datetimepicker_start', 'data-date-format':'yyyy-mm-dd hh:ii'}),
                   'end_time': forms.DateTimeInput(attrs={'id':'datetimepicker_end', 'data-date-format':'yyyy-mm-dd hh:ii'})}

def index(request):
    farm_groups = FarmGroup.objects.all().order_by('id')

    return render(request, 'index.html', {'farm_groups':farm_groups})

def farm_group(request, farm_group_id):
    farm_group = get_object_or_404(FarmGroup, pk=farm_group_id)
    farm_events = FarmEvent.objects.filter(group=farm_group).order_by('start_time')

    # This feels super yucky slapping this on the object.
    for farm_event in farm_events:
        farm_event.time_diff = (datetime.datetime.min + (farm_event.end_time - farm_event.start_time)).time()
        print(farm_event.time_diff)

    return render(request, 'farm_group.html', {'farm_group':farm_group, 'farm_events': farm_events})


def farm_event(request, farm_group_id, farm_event_id=None):
    farm_group = get_object_or_404(FarmGroup, pk=farm_group_id)

    if request.method == 'GET':
        farm_event = get_object_or_404(FarmEvent, pk=farm_event_id)
        form = FarmEventForm(instance=farm_event)
        return render(request, 'farm_event.html', {'farm_group':farm_group, 'farm_event': farm_event, 'form':form})

    elif request.method == 'POST':
        # Update
        if (farm_event_id):
            farm_event = get_object_or_404(FarmEvent, pk=farm_event_id)
            f = FarmEventForm(request.POST, instance=farm_event)
        # Insert
        else:
            f = FarmEventForm(request.POST)

        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse('farm_group', kwargs={ 'farm_group_id':farm_group.id }))
        else:
            # TODO - display validation errors.
            print(f.errors)
            print(request.POST)
            f.save()


