from django.db import models


class FarmGroup(models.Model):
    title = models.CharField(max_length=20)

class FarmEvent(models.Model):
    group = models.ForeignKey(FarmGroup)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    death_breath_count = models.IntegerField()
    legendary_count = models.IntegerField()
    bounty_count = models.IntegerField()
    blood_shard_count = models.IntegerField()
    experience_count = models.IntegerField()
