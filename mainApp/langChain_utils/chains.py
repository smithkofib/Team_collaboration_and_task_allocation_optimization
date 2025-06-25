# task_allocation/langchain_utils/chains.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from .config import OPENAI_API_KEY
from .prompts_copy import job_allocation_prompt, job_allocation_explanation_prompt
from .prompts_role_allocation import role_allocation_prompt, role_allocation_explanation_prompt
from .prompts_group_role_allocation import group_role_allocation_prompt, group_role_allocation_explanation_prompt

# Initialize OpenAI LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.7, api_key=OPENAI_API_KEY)

# Predefined Chains
job_allocation_chain = LLMChain(llm=llm, prompt=job_allocation_prompt)
role_allocation_chain = LLMChain(llm=llm, prompt=role_allocation_prompt)
group_role_allocation_chain = LLMChain(llm=llm, prompt=group_role_allocation_prompt)
job_allocation_explanation_chain = LLMChain(llm=llm, prompt=job_allocation_explanation_prompt)
role_allocation_explanation_chain = LLMChain(llm=llm, prompt=role_allocation_explanation_prompt)
group_role_allocation_explanation_chain = LLMChain(llm=llm, prompt=group_role_allocation_explanation_prompt)

# Predict Job Allocation
def predict_job_allocation(school_names, heighest_degrees, fields_studied, companies, job_titles):
    return job_allocation_chain.invoke({
        "school_names": school_names,
        "heighest_degrees": heighest_degrees,
        "fields_studied": fields_studied,
        "companies": companies,
        "job_titles": job_titles,
    })

# Explain Job Allocation
def explain_job_allocation(employee_fullname, school_names, heighest_degrees, fields_studied, companies, job_titles, predicted_job):
    return job_allocation_explanation_chain.invoke({
        "employee_fullname": employee_fullname,
        "school_names": school_names,
        "heighest_degrees": heighest_degrees,
        "fields_studied": fields_studied,
        "companies": companies,
        "job_titles": job_titles,
        "predicted_job": predicted_job,
    })

# Predict Role Allocation
def predict_role_allocation(eduction, working_experience, position, job_description):
    education_result = list(eduction.values())
    working_experience_result = list(working_experience.values())

    role = [item["role"] for item in education_result]
    institutionName = [item["institution_name"] for item in education_result]
    degree = [item["degree"] for item in education_result]
    fieldOfStudy = [item["field_of_study"] for item in education_result]
    startYear = [item["start_year"] for item in education_result]
    endYear = [item["end_year"] for item in education_result]
    jobTitle = [item["job_title"] for item in working_experience_result]
    companyName = [item["company_name"] for item in working_experience_result]
    startDate = [item["start_date"] for item in working_experience_result]
    endDate = [item["end_date"] for item in working_experience_result]
    responsibilities = [item["responsibilities"] for item in working_experience_result]

    return role_allocation_chain.invoke({
        "first_name": education_result[0]['first_name'],
        "last_name": education_result[0]['last_name'],
        "role": role,
        "institution_name": institutionName,
        "degree": degree,
        "field_of_study": fieldOfStudy,
        "start_year": startYear,
        "end_year": endYear,
        "job_titles": jobTitle,
        "company_name": companyName,
        "start_date": startDate,
        "end_date": endDate,
        "responsibilities": responsibilities,
        "position": position,
        "job_description": job_description
    })

# Explain Role Allocation
def explain_role_allocation(position, predicted_employee):
    return role_allocation_explanation_chain.invoke({
        "position": position,
        "predicted_employee": predicted_employee,
    })

# Predict Group Role Allocation
def group_role_predict_allocation(eduction, working_experience, position, number_of_staffs, gender, job_description):
    education_result = list(eduction.values())
    working_experience_result = list(working_experience.values())

    role = [item["role"] for item in education_result]
    candidate_gender = [item["gender"] for item in education_result]
    institutionName = [item["institution_name"] for item in education_result]
    degree = [item["degree"] for item in education_result]
    fieldOfStudy = [item["field_of_study"] for item in education_result]
    startYear = [item["start_year"] for item in education_result]
    endYear = [item["end_year"] for item in education_result]
    jobTitle = [item["job_title"] for item in working_experience_result]
    companyName = [item["company_name"] for item in working_experience_result]
    startDate = [item["start_date"] for item in working_experience_result]
    endDate = [item["end_date"] for item in working_experience_result]
    responsibilities = [item["responsibilities"] for item in working_experience_result]

    return group_role_allocation_chain.invoke({
        "first_name": education_result[0]['first_name'],
        "last_name": education_result[0]['last_name'],
        "candidate_gender": candidate_gender,
        "role": role,
        "institution_name": institutionName,
        "degree": degree,
        "field_of_study": fieldOfStudy,
        "start_year": startYear,
        "end_year": endYear,
        "job_titles": jobTitle,
        "company_name": companyName,
        "start_date": startDate,
        "end_date": endDate,
        "responsibilities": responsibilities,
        "position": position,
        "number_of_staffs": number_of_staffs,
        "gender": gender,
        "job_description": job_description
    })

# Explain Group Role Allocation
def explain_group_role_allocation(position, predicted_employee):
    return group_role_allocation_explanation_chain.invoke({
        "position": position,
        "predicted_employee": predicted_employee,
    })
