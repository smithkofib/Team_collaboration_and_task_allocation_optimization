from django import forms
from .models import (Candidate, Skill, WorkExperience, Education, 
                     CandidateAssessment, CandidateFeedback, Job,
                     Departement, Staff)

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = "__all__"

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class CandidateAssessmentForm(forms.ModelForm):
    class Meta:
        model = CandidateAssessment
        fields = '__all__'

class CandidateFeedbackForm(forms.ModelForm):
    class Meta:
        model = CandidateFeedback
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
