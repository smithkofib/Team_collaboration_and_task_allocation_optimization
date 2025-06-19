# task_allocation/langchain_utils/prompts.py
from django.shortcuts import get_object_or_404
from langchain.prompts import PromptTemplate

# Prompt for employee for role prediction and explanation

#upload of cV
#Uplaad of certificates
#gender allocation during registration
#filter, segrigation staff by gender
#selecting a group of staffs the best fit a selected position based on their gender
#and their working experiences, education in oder of prefrences
# def explain_role_allocation(position, predicted_employee):
#     return role_allocation_explanation_chain.invoke({
#         "position" : position,
#         "predicted_employee": predicted_employee,
#     })


group_role_allocation_prompt = PromptTemplate(
    input_variables=["first_name", "last_name", "candidate_gender", "role", "institution_name", "degree", "field_of_study", "start_year", "end_year", "job_titles", "company_name", "start_date", "end_date", "responsibilities", "position", "number_of_staffs", "gender", "job_description"],
    template="""
        Our compnay is shortlisting {number_of_staffs} of his {gender} employees base on 
        their details for 
        the position as a {position} with the position's descripton as {job_description}. 
        Analysis their details and predict {number_of_staffs} {gender}s  that merits this position.
        The follow details list their names, educations background, and working experiences
        Their first names are {first_name}, last names are {last_name} and genders {candidate_gender} respectively,
        their roles in the company are as {role} respectively,
        they hold various certificates in {degree} in the study of {field_of_study} from 
        these institutions {institution_name} respectively,
        and lastly, they worked as {job_titles} in the companies {company_name} with
        the responsibilities {responsibilities} from the year {start_date} to {end_date} respectively,
        Note, the details of these employees correspond respectively to their names, working
        experiences and education background as presented.
        Also, as mentioned, select {number_of_staffs} {gender}s from the pool of the above employees details.
        
        Again, for your answer, mention only their first names and last names of these employees that you
        have selected or shortlisted as the best fit, without explainations.
        If there are no males or females with the group, notify as there are no males or females.
        Also if the number of employees selected is less than the number of employees
        shortlisted, return those that fit and notify as there are not enough employees to select from.
        Also, don't select duplicates of the same names, and if there are duplicates,
        select only one of them.
        Finally, they must be listed in order of prefrences, and in a simply array format example ["Smith Jones", "Fred Stones", "Eric Greaterson"].
    """
)
group_role_allocation_explanation_prompt = PromptTemplate(
    input_variables=[ "predicted_employee", "position"],
    template="""
    Explain why these employees {predicted_employee} was shortlisted as among the pool of employees
    for the position as {position}  and why each of them merits this position.
    Give explaination for each of the shortlisted employees you have selected based on each of their
    details.  
    """
)

#upload of cV
#Uplaad of certificates
#gender allocation during registration
#filter, segrigation staff by gender
#selecting a group of staffs the best fit a selected position based on their gender
#and their working experiences, education in oder of prefrences
# def explain_role_allocation(position, predicted_employee):
#     return role_allocation_explanation_chain.invoke({
#         "position" : position,
#         "predicted_employee": predicted_employee,
#     })

