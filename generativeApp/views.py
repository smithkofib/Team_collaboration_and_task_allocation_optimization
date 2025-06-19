""" # team_task_allocation_proj/mainApp/views.py

# Create your views here.
from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee, Task

import json
import torch
from sentence_transformers import SentenceTransformer, util


# Load Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for all employees
def get_employee_embeddings():
    employees = Employee.objects.all()
    employee_dict = {}
    
    for emp in employees:
        emp_vector = model.encode(emp.skills, convert_to_tensor=True)
        employee_dict[emp.id] = (emp_vector, emp)
    
    return employee_dict

# Predict best employee for a task
def allocate_task(task_id):
    task = Task.objects.get(id=task_id)
    task_vector = model.encode(task.required_skills, convert_to_tensor=True)
    employees = get_employee_embeddings()
    
    best_match = None
    best_score = -1
    
    for emp_id, (emp_vector, emp) in employees.items():
        similarity = util.pytorch_cos_sim(task_vector, emp_vector).item()
        if similarity > best_score:
            best_score = similarity
            best_match = emp
    
    return best_match

# API Endpoints
@csrf_exempt
def allocate_task_view(request, task_id):
    if request.method == 'GET':
        employee = allocate_task(task_id)
        return JsonResponse({'employee_id': employee.id, 'employee_name': employee.name})

# Dashboard View
def dashboard(request):
    employees = Employee.objects.all()
    tasks = Task.objects.all()
    return render(request, 'dashboard.html', {'employees': employees, 'tasks': tasks})
 """