# Generated by Django 3.1.7 on 2021-05-31 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noon',
            name='offercode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
