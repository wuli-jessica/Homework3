# Generated by Django 2.0.5 on 2018-05-27 15:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0005_userstock'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userstock',
            unique_together={('user', 'stock')},
        ),
    ]
