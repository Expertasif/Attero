# Generated by Django 2.0.1 on 2018-01-10 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attero', '0008_remove_project_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('view_Project', 'View Project'),)},
        ),
    ]