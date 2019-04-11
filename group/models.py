from django.utils import timezone
from django.db import models
from authentication.models import Party, Profile, Usertype


class Group(models.Model):
    name = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=5000)
    admin_id = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'admin_id')


class GroupMembers(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('group_id', 'user_id')


class Event(models.Model):
    name = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

    class Meta:
        unique_together = ('name', 'group_id')


class Arch_Event(models.Model):
    name = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

    class Meta:
        unique_together = ('name', 'group_id')