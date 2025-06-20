# Generated by Django 4.2.7 on 2025-03-24 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_candidate_candidateassessment_candidatefeedback_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement_name', models.CharField(blank=True, max_length=255)),
                ('departement_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('departement_room_number', models.IntegerField(help_text="The departement room's number")),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(max_length=255)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='mainApp.departement')),
            ],
        ),
        migrations.CreateModel(
            name='StaffDepartement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_departement', to='mainApp.departement')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departement_manager', to='mainApp.staff')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_departement', to='mainApp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_staff', to='mainApp.candidate')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_staff', to='mainApp.staff')),
            ],
        ),
    ]
