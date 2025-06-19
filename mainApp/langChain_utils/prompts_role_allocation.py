# task_allocation/langchain_utils/prompts.py
from django.shortcuts import get_object_or_404
from langchain.prompts import PromptTemplate

# Prompt for employee for role prediction and explanation


role_allocation_prompt = PromptTemplate(
    input_variables=["first_name", "last_name", "role", "institution_name", "degree", "field_of_study", "start_year", "end_year", "job_titles", "company_name", "start_date", "end_date", "responsibilities", "position", "job_description"],
    template="""
        The following employees and their detials are contesting for the position
        of a {position} with the position's descripton as {job_description}. 
        Analysis their details and predict the one that merits this position.
        The follow details list their names, educations background and working experiences
        Their first names are {first_name} and last names are {last_name} respectively,
        their roles in the company are as {role} respectively,
        they hold various certificates in {degree} in the study of {field_of_study} from 
        these institutions {institution_name} respectively,
        and lastly, they worked as {job_titles} in the companies {company_name} with
        the responsibilities {responsibilities} from the year {start_date} to {end_date} respectively,
        Note, the details of these employees correspond respectively to their names, working
        experiences and education background as presented.
        Finally, for the answer, mention only the first name and last name of the employee 
        who best fit this position and was predicted without explaination.
    """
)
role_allocation_explanation_prompt = PromptTemplate(
    input_variables=[ "predicted_employee", "position"],
    template="""
    Explain why {predicted_employee} was predicted as the right winner or candidate
    for the position as {position}  and why he or she merits this position,   
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

