######## team_task_allocation_proj/mainApp/urls.py
# from django.urls import path
# from . import views
# 
# urlpatterns = [
#     path('allocate/', views.allocate_task, name='allocate_task'),
#     path('exp_allocate/', views.lang_chain_allocate_task, name='exp_allocate_task'),
# 
# 
# ]
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainApp import views
#from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Uploading of files
    path('files/', views.file_list, name='file_list'),
   
    
    # Candidate URLs
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/add/', views.add_candidate, name='add_candidate'),
    path('candidates/<int:candidate_id>/', views.view_candidate, name='view_candidate'),
    path('candidates/<int:candidate_id>/edit/', views.edit_candidate, name='edit_candidate'),
    path('candidates/<int:candidate_id>/delete/', views.delete_candidate, name='delete_candidate'),
    path('candidates/<int:candidate_id>/<str:predicted_job>/approved/', views.approve_candidate, name='approve_candidate'),
    path('candidates/approved_list/', views.approved_candidate_list, name='approved_candidate_list'),


    # Candidate Registration URLs
    path('candidate-registration/', views.register_list, name='register_list'),
    #path('candidate-registration/<int:candidate_id>/register/', views.register_candidate, name='register_candidate'),

    # Skills URLs
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.add_skill, name='add_skill'),
    path('skills/<int:skill_id>/delete/', views.delete_skill, name='delete_skill'),

    # Work Experience URLs
    path('work-experience/<int:candidate_id>/', views.work_experience_list, name='work_experience_list'),
    path('work-experience/<int:candidate_id>/add/', views.add_work_experience, name='add_work_experience'),

    path('work-experience/<int:workExpo_id>/<int:candidate_id>/view_details/', views.view_workExpo_details, name='work_experience_detail'),
    path('work-experience/<int:workExpo_id>/<int:candidate_id>/delete/', views.delete_workExpo, name='delete_work_experience'),
    path('work-experience/<int:workExpo_id>/<int:candidate_id>/edit/', views.edit_workExpo, name='edit_work_experience'),

    # Education URLs
    path('education/<int:candidate_id>/', views.education_list, name='education_list'),
    path('education/<int:candidate_id>/add/', views.add_education, name='add_education'),
    path('education/<int:education_id>/<int:candidate_id>/view_details/', views.view_education_details, name='view_education_details'),
    path('education/<int:education_id>/<int:candidate_id>/delete/', views.delete_education, name='delete_education'),
    path('education/<int:education_id>/<int:candidate_id>/edit/', views.edit_education, name='edit_education'),
    # Assessments & Feedback
    path('assessments/<int:candidate_id>/', views.assess_candidate, name='assess_candidate'),
    path('feedback/<int:candidate_id>/add/', views.add_feedback, name='add_feedback'),

    # Job URLs
    path("job/add/", views.add_job, name='add_job'),

    # Departement URLs
    path('departement/', views.departement_list, name='departement_list'),
    path('departement/add/', views.add_departement, name='add_departement'),
    path('departement/all_staffs/<int:departement_id>/', views.departement_staff_list, name='departement_staff_list'),
    path('departement/delete/<int:departement_id>/', views.delete_departement, name='delete_departement'),

    # Staff URLs   gender_filtering
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/edit/<int:staff_id>/<int:candidate_id>s/', views.staff_edit, name='staff_edit'),
    path('staff/delete/<int:staff_id>/', views.delete_staff, name='delete_staff'),
    path('staff/<int:staff_id>/<int:candidate_id>/', views.staff_detail, name='staff_detail'),
    path('staff/<int:candidate_id>/', views.staff_detail_approved, name='staff_detail_approved'),
    path('filter/', views.gender_filtering, name='gender_filtering'),


    # LangChain Predictor URLs
    path("langchain/predict_job/<int:candidate_id>/", views.predict_job, name='predict_job'),
    path("langchain/predict_role/<int:departement_id>/", views.predict_role, name='predict_role'),
    path("langchain/group_predict_role/<int:departement_id>/", views.group_role_predict, name='group_role_predict'),

]

#This ensures files are accessible when DEBUG=True.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
