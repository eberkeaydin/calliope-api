# Generated by Django 4.1.4 on 2023-06-02 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '0003_conference'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferencePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_editor_url', models.URLField(max_length=512, verbose_name='Code Editor URL')),
                ('directive_text', models.TextField(default='', verbose_name='Directives')),
                ('is_active', models.BooleanField(default=True)),
                ('related_conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lesson.conference', verbose_name='Related Conference')),
            ],
            options={
                'verbose_name': 'Conference Page',
                'verbose_name_plural': 'Conference Pages',
                'ordering': ['id'],
            },
        ),
    ]
