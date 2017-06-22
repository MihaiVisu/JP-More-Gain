# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retrospective', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamCoders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager', models.BooleanField(default=False)),
                ('memeber', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='retrospective.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teamuser',
            name='member',
        ),
        migrations.RemoveField(
            model_name='teamuser',
            name='team',
        ),
        migrations.DeleteModel(
            name='TeamUser',
        ),
        migrations.AddField(
            model_name='item',
            name='creationDate',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
