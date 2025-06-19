""" # team_task_allocation_proj/mainApp/views.py

# Create your views here.
from django.shortcuts import render
from .models import Candidate, Task
from .langChain_utils.chains import explain_task_allocation, explain_team_formation
import joblib
import os

def create_candidate(request):
    if request.method == "POST":
        firstName = request.POST['first_name']
        candidate = Candidate.objects.create(
        first_name=firstName, last_name="Doe", email="john@example.com")
        if request.is_valid():
            render(request=request, template_name="", context={"message":"Successful"})
        else:
            render(request=request, template_name="", context={'message':"Faild"})

def allocate_task(request):
    if request.method == 'POST':
        # Load the trained model
        model_path = os.path.join(os.path.dirname(__file__), 'ml_models', 'model.pkl')
        model = joblib.load(model_path)

        # Get employee data from the form
        employee_id = request.POST.get('employee_id')
        employee = Employee.objects.get(id=employee_id)

        # Prepare input for the model
        input_data = [[employee.skill_level, employee.experience, employee.rating, employee.contributions]]

        # Predict task allocation
        predicted_task = model.predict(input_data)[0]

        print(predicted_task)

        # Get the task object
        task = Task.objects.get(name=predicted_task)

        return render(request, 'results.html', {'employee': employee, 'task': task})

    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})


def lang_chain_allocate_task(request):
    if request.method == 'POST':
        # Get employee data from the form
        employee_id = request.POST.get('employee_id')
        employee = Employee.objects.get(id=employee_id)

        # Get task data (for simplicity, assume the task is already assigned)
        task = Task.objects.first()

        # Generate explanation using LangChain
        explanation = explain_task_allocation(
            employee_name=employee.name,
            task_name=task.name,
            skills=employee.skill_level,
            experience=employee.experience,
            rating=employee.rating
        )

        return render(request, 'task_allocation/langChainResult.html', {
            'employee': employee,
            'task': task,
            'explanation': explanation
        })

    employees = Employee.objects.all()
    return render(request, 'task_allocation/index.html', {'employees': employees})

# task_allocation/views.py
def form_team(request):
    if request.method == 'POST':
        # Get team members and project name from the form
        team_member_ids = request.POST.getlist('team_members')
        team_members = Employee.objects.filter(id__in=team_member_ids)
        project_name = request.POST.get('project_name')

        # Generate explanation using LangChain
        explanation = explain_team_formation(
            team_members=", ".join([member.name for member in team_members]),
            project_name=project_name
        )

        return render(request, 'task_allocation/langChainTeamResult.html', {
            'team_members': team_members,
            'project_name': project_name,
            'explanation': explanation
        })

    employees = Employee.objects.all()
    return render(request, 'task_allocation/langChainFormTeam.html', {'employees': employees}) """