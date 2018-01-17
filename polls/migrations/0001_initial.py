# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-17 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'choice',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'question',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
