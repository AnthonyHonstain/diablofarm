from django.shortcuts import render, get_object_or_404
from .models import FarmGroup, FarmEvent
import datetime
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse

from django import forms
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.core import serializers

class FarmEventForm(ModelForm):
    death_breath_count = forms.IntegerField(validators=[MinValueValidator(0)])
    class Meta:
        model = FarmEvent

        fields = ['start_time', 'end_time', 'death_breath_count'] #, 'death_breath_count', 'legendary_count', 'bounty_count', 'blood_shard_count', 'experience_count']
        widgets = {'start_time': forms.DateTimeInput(attrs={'id':'datetimepicker_start', 'data-date-format':'yyyy-mm-dd hh:ii'}),
                   'end_time': forms.DateTimeInput(attrs={'id':'datetimepicker_end', 'data-date-format':'yyyy-mm-dd hh:ii'})}

def index(request):
    '''
    Root page for the site:
    * Dumps out a list of the groups you can work on.
    '''
    farm_groups = FarmGroup.objects.all().order_by('id')

    return render(request, 'index.html', {'farm_groups':farm_groups})

def _calculate_time_diff(start_time, end_time):
    return (datetime.datetime.min + (end_time - start_time)).time()

def farm_group(request, farm_group_id):
    '''
    List the most recent events.
    '''
    farm_group = get_object_or_404(FarmGroup, pk=farm_group_id)
    farm_events = FarmEvent.objects.filter(group=farm_group).order_by('start_time')[:10]

    # TODO - FIX DRY CODE

    # This feels super yucky slapping this on the object.
    for farm_event in farm_events:
        farm_event.time_diff = _calculate_time_diff(farm_event.start_time, farm_event.end_time)

    return render(request, 'farm_group.html', {'farm_group':farm_group, 'farm_events': farm_events})

def farm_group_export(request, farm_group_id):
    '''
    Ghetto dump of all the events in the group.
    '''
    farm_group = get_object_or_404(FarmGroup, pk=farm_group_id)
    farm_events = FarmEvent.objects.filter(group=farm_group).order_by('start_time')

    # This feels super yucky slapping this on the object.
    for farm_event in farm_events:
        farm_event.time_diff = _calculate_time_diff(farm_event.start_time, farm_event.end_time)

    farm_events_json = serializers.serialize('json', farm_events)

    return render(request, 'farm_group_export.html', {'farm_group':farm_group, 'farm_events_json': farm_events_json})

def farm_event(request, farm_group_id, farm_event_id=None):
    '''
    We are taking the group and option event via the url instead of in the form.

    This one endpoint handles the GET, INSERT, and UPDATE for the FarmEvent
    '''
    farm_group = get_object_or_404(FarmGroup, pk=farm_group_id)

    if request.method == 'GET':
        if (farm_event_id):
            farm_event = get_object_or_404(FarmEvent, pk=farm_event_id)
        else:
            farm_event = None
        form = FarmEventForm(instance=farm_event)
        return render(request, 'farm_event.html', {'farm_group':farm_group, 'farm_event': farm_event, 'form':form})

    elif request.method == 'POST':
        # Update
        if (farm_event_id):
            farm_event = get_object_or_404(FarmEvent, pk=farm_event_id)
            form = FarmEventForm(request.POST, instance=farm_event)
        # Insert
        else:
            farm_event = FarmEvent()
            farm_event.group = farm_group
            form = FarmEventForm(request.POST, instance=farm_event)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('farm_group', kwargs={ 'farm_group_id':farm_group.id }))
        else:
            # TODO - display validation errors.
            print(form.errors)
            print(request.POST)
            return render(request, 'farm_event.html', {'farm_group':farm_group, 'farm_event': farm_event, 'form':form})
