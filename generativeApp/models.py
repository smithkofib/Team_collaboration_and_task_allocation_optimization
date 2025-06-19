""" from django.db import models


# Models for storing employees and tasks
class Employee(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()  # Comma-separated list of skills
    experience = models.IntegerField()
    rating = models.FloatField(default=0.0)

class Task(models.Model):
    title = models.CharField(max_length=255)
    required_skills = models.TextField()  # Comma-separated list of skills
    complexity = models.IntegerField() """