# Generated by Django 4.1.4 on 2022-12-24 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='Has no category', max_length=255, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=255, verbose_name='Lesson Title')),
                ('difficulty', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advance')], default=1, verbose_name='Difficulty')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.category', verbose_name='Lesson Category')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField(max_length=512, verbose_name='Video URL')),
                ('content_header', models.CharField(max_length=255, verbose_name='Content Header')),
                ('content_text', models.TextField(verbose_name='Content Text')),
                ('related_lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.lesson', verbose_name='Related Lesson')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
                'ordering': ['id'],
            },
        ),
    ]
