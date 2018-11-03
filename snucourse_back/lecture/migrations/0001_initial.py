# Generated by Django 2.0.5 on 2018-11-01 10:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=20)),
                ('grade', models.CharField(blank=True, max_length=10)),
                ('lecture_num', models.CharField(max_length=20)),
                ('class_num', models.IntegerField(default=1)),
                ('credit_Total', models.IntegerField()),
                ('credit_Theory', models.IntegerField(blank=True)),
                ('credit_Practice', models.IntegerField(blank=True)),
                ('time', models.CharField(blank=True, max_length=20)),
                ('composition', models.CharField(blank=True, max_length=20)),
                ('classroom', models.CharField(blank=True, max_length=20)),
                ('lecturer', models.CharField(blank=True, max_length=20)),
                ('capacity', models.CharField(max_length=20)),
                ('optional', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
                ('area', models.CharField(blank=True, max_length=20)),
                ('easy', models.IntegerField(blank=True, default=0)),
                ('useful', models.IntegerField(blank=True, default=0)),
                ('credit', models.IntegerField(blank=True, default=0)),
                ('avg_review_score', models.FloatField(blank=True, default=0)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.College')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Department')),
            ],
        ),
        migrations.CreateModel(
            name='LectureName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('credit', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='LectureOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('easy', models.IntegerField()),
                ('useful', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture', to='lecture.LectureName'),
        ),
    ]
