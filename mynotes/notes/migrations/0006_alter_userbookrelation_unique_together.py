# Generated by Django 4.2.3 on 2023-07-15 22:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0005_alter_book_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userbookrelation',
            unique_together={('user', 'book')},
        ),
    ]
