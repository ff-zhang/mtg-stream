# Generated by Django 3.0.7 on 2020-06-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0003_auto_20200619_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_id',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
