# task_allocation/langchain_utils/prompts.py
from langchain.prompts import PromptTemplate
from jinja2 import Template
# Prompt for task allocation explanation

job_allocation_jinja_prompt=Template("""
    A job candidate how attended the following schools -
                                      
    {% for school_name in school_names %} 
    {{ school_name }} 
    {% endfor %},
                                     
    holding these listed degress
                                     
    {% for heighest_degree in heighest_degrees %} 
    {{ heighest_degree }}
    {% endfor %},
                                     
    offered the following listed fields of study
                                     
    {% for field_studied in fields_studied %} 
    {{ field_studied }}
    {% endfor %}
                                     
    and worked in companies as
                                                                 
    {% for company in companies %} 
    {{ company }}
    {% endfor %}
                                                                    
    with various job positions as followed
                                     
    {% for job_title in job_titles %} 
    {{ job_title }} 
    {% endfor %}.
                                                                    
    What job position best fits this candidate?
    Please only mention the job position that best fits this candidate without explanation. 
    """)

job_allocation_explanation_jinja_prompt=Template("""
    Explain why {employee_fullname} how attended the following schools - {% for school_name in school_names %} {{school_name}} {% endfor %}, with these
    degress {heighest_degrees}, offered the listed fields of study {fields_studied} and worked in companies as {companies} with various job positions {job_titles} was assigned for the position {predicted_job}.
    Please give a full explanation as why {employee_fullname} deserved the position as a {predicted_job}.
    """)

