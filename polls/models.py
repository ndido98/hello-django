# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=255)
    voters = models.ManyToManyField(User, through='Vote', related_name='polls')

    class Meta:
        db_table = 'poll'

    def __str__(self):
        return self.question


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING, related_name='options')
    option_text = models.CharField(max_length=255)

    class Meta:
        db_table = 'poll_option'

    def __str__(self):
        return self.option_text


class Vote(models.Model):
    pk = models.CompositePrimaryKey('poll_id', 'user_id')
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING, related_name='votes')
    option = models.ForeignKey(PollOption, on_delete=models.DO_NOTHING, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'vote'
        unique_together = (('poll', 'user'),)
