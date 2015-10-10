from django.test import TestCase

from .models import FarmGroup, FarmEvent

from django.core.urlresolvers import reverse
from django.test import Client

from django.utils import timezone


class CoreIndexTest(TestCase):
    '''
    Basic sanity check to see if the site stands up and verify the display with basic data.
    http://127.0.0.1:8000/
    '''

    def test_core_index_with_empty(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DiabloFarm")
        self.assertQuerysetEqual(response.context['farm_groups'], [])

    def test_core_index_with_small_group(self):
        farm_group = FarmGroup.objects.create(title='Test farm group')
        farm_group2 = FarmGroup.objects.create(title='Another group')

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, farm_group.title)
        self.assertContains(response, farm_group2.title)
        self.assertQuerysetEqual(response.context['farm_groups'], ['<FarmGroup: FarmGroup object>', '<FarmGroup: FarmGroup object>'])
        # using repr??? http://stackoverflow.com/questions/11610943/django-1-4-assertquerysetequal-how-to-use-method
        self.assertQuerysetEqual(response.context['farm_groups'], map(repr, [farm_group, farm_group2]))


class CoreFarmGroupTest(TestCase):
    '''
    Basic sanity check of the farm group page
    http://127.0.0.1:8000/farm_group/1/
    '''

    def test_farm_group(self):
        # Check what happens when nothings in the system yet.
        response = self.client.get(reverse('farm_group', kwargs={'farm_group_id':1}))
        self.assertEqual(response.status_code, 404)

        # Create a group, but no events.
        farm_group = FarmGroup.objects.create(title='Test farm group')
        response = self.client.get(reverse('farm_group', kwargs={'farm_group_id':farm_group.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, farm_group.title)

        # Add an event and check that it dumps out some of the event data.
        farm_event = FarmEvent.objects.create(
            group=farm_group,
            start_time=timezone.now(),
            end_time=timezone.now(),
            death_breath_count=3333,
            legendary_count=2212,
            bounty_count=None,
            blood_shard_count=None,
            experience_count=None)
        response = self.client.get(reverse('farm_group', kwargs={'farm_group_id':farm_group.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, farm_group.title)
        self.assertContains(response, 3333)
        self.assertEqual(response.context['farm_group'], farm_group)
        self.assertQuerysetEqual(response.context['farm_events'], map(repr, [farm_event]))