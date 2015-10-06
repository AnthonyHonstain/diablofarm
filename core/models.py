from django.db import models


class FarmGroup(models.Model):
    title = models.CharField(max_length=20)

class FarmEvent(models.Model):
    group = models.ForeignKey(FarmGroup)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Optional fields, I guess they could fill none of them out if they wanted.
    death_breath_count = models.IntegerField(null=True, blank=True)
    legendary_count = models.IntegerField(null=True, blank=True)
    bounty_count = models.IntegerField(null=True, blank=True)
    blood_shard_count = models.IntegerField(null=True, blank=True)
    experience_count = models.IntegerField(null=True, blank=True)
