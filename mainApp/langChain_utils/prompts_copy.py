# task_allocation/langchain_utils/prompts.py
from langchain.prompts import PromptTemplate

# Prompt for task allocation explanation
job_allocation_prompt = PromptTemplate(
    input_variables=["school_names", "heighest_degrees", "fields_studied", "companies", "job_titles"],
    template="""
    A job candidate how attended the following schools - 
    {school_names} 
    holding these listed degress {heighest_degrees}, offered the following listed fields of 
    study {fields_studied} and worked in companies as {companies} with various 
    job positions as followed {job_titles}. What job position best fits this candidate?
    Only mention the job position that best fits this candidate without explianation. 
    """
)
job_allocation_explanation_prompt = PromptTemplate(
    input_variables=["employee_fullname", "school_names", "heighest_degrees", "fields_studied", "companies", "job_titles", "predicted_job"],
    template="""
    Explain why {employee_fullname} who attended the following schools - {school_names}, with these
    degress {heighest_degrees}, offered the listed fields of study {fields_studied} 
    and worked in companies as {companies} with various job positions as {job_titles} 
    was assigned for the position {predicted_job}.
    Give a full explanation as why {employee_fullname} 
    deserved the position as a {predicted_job}.
    """
)
