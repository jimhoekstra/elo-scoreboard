# Generated by Django 4.0.4 on 2022-04-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='current_elo',
            field=models.IntegerField(default=800),
        ),
    ]