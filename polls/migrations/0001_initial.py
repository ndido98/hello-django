# Generated by Django 5.2 on 2025-04-30 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'poll',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=255)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.poll')),
            ],
            options={
                'db_table': 'poll_option',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('pk', models.CompositePrimaryKey('poll_id', 'user_id', blank=True, editable=False, primary_key=True, serialize=False)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.polloption')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.user')),
            ],
            options={
                'db_table': 'vote',
                'unique_together': {('poll', 'user')},
            },
        ),
    ]
