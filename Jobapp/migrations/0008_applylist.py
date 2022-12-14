# Generated by Django 4.0.3 on 2022-04-12 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0007_jobdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('min_salary', models.CharField(max_length=200)),
                ('max_salary', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='app/resume')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jobapp.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jobapp.jobdetails')),
            ],
        ),
    ]
