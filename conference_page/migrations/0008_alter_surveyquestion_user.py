# Generated by Django 4.1.4 on 2023-06-02 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_role'),
        ('conference_page', '0007_alter_surveyquestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='User'),
        ),
    ]
