# Generated by Django 4.1.4 on 2022-12-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advance')], default=0, verbose_name='Difficulty'),
        ),
    ]