# Generated by Django 4.2.7 on 2025-03-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_candidate_approval_candidate_role_staff_candidate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='role',
            field=models.CharField(default='no_role', max_length=50),
        ),
    ]
