# Generated by Django 3.0.8 on 2020-09-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='ddd',
            field=models.IntegerField(null=True),
        ),
    ]
