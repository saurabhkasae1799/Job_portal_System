# Generated by Django 4.0.3 on 2022-04-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0013_contact_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact',
        ),
        migrations.AlterField(
            model_name='contact',
            name='Message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Subject',
            field=models.TextField(),
        ),
    ]
