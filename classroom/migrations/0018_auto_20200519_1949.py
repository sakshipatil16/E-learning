# Generated by Django 3.0.6 on 2020-05-19 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0017_answer_ass_dashboard_ass_question_ass_quiz_ass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer_ass',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_ass', to='classroom.Question_ass'),
        ),
        migrations.AlterField(
            model_name='dashboard_ass',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='q', to='classroom.Quiz_ass'),
        ),
        migrations.AlterField(
            model_name='question_ass',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_ass', to='classroom.Quiz_ass'),
        ),
        migrations.AlterField(
            model_name='quiz_ass',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chap_q_ass', to='classroom.Chapterass'),
        ),
        migrations.AlterField(
            model_name='quiz_ass',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_q_ass', to='classroom.Assignmentmain'),
        ),
    ]