# Generated by Django 4.0.3 on 2022-04-04 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0003_jobdetails_alter_company_logo_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobDetails',
        ),
    ]