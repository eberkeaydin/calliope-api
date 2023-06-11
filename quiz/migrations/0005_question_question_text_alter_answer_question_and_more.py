# Generated by Django 4.1.4 on 2022-12-25 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_answer_question_alter_question_difficulty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.TextField(default='', verbose_name='Question Text'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.quizzes'),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.category'),
        ),
    ]
