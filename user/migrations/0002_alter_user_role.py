# Generated by Django 4.1.4 on 2023-04-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'No role'), (1, 'Learner'), (2, 'Tutor')], default=0, verbose_name='Role'),
        ),
    ]