# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'


class Poll(models.Model):
    question = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'poll'


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, models.DO_NOTHING)
    option_text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'poll_option'


class Vote(models.Model):
    pk = models.CompositePrimaryKey('poll_id', 'user_id')
    poll = models.ForeignKey(Poll, models.DO_NOTHING)
    option = models.ForeignKey(PollOption, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vote'
        unique_together = (('poll', 'user'),)
