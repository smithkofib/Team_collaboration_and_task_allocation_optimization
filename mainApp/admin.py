from django.contrib import admin
from .models import (Candidate, SkillCategory, Skill, CandidateSkill, 
                     WorkExperience, Education, CulturalFit, CandidateAssessment,
                     CandidateFeedback, Job, Departement, Staff, StaffDepartement)



# Register your models here.
admin.site.register(Candidate)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(CandidateSkill)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(CulturalFit)
admin.site.register(CandidateAssessment)
admin.site.register(CandidateFeedback)
admin.site.register(Job)
admin.site.register(Departement)
admin.site.register(Staff)
admin.site.register(StaffDepartement)
