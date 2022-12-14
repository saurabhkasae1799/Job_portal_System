# Generated by Django 4.0.3 on 2022-04-04 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0006_delete_jobdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=250)),
                ('companyname', models.CharField(max_length=250)),
                ('companyaddress', models.CharField(max_length=250)),
                ('jobdescription', models.TextField(max_length=500)),
                ('qualification', models.CharField(max_length=250)),
                ('resposibilties', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('companywebsite', models.CharField(max_length=250)),
                ('companyemail', models.CharField(max_length=250)),
                ('companycontact', models.CharField(max_length=20)),
                ('salarypackage', models.CharField(max_length=250)),
                ('experience', models.IntegerField()),
                ('logo', models.ImageField(default='', upload_to='app/img/jobpost')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jobapp.company')),
            ],
        ),
    ]
