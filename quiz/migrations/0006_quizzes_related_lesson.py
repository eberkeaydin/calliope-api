# Generated by Django 4.1.4 on 2023-06-16 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_conference_is_active'),
        ('quiz', '0005_question_question_text_alter_answer_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzes',
            name='related_lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson'),
        ),
    ]
