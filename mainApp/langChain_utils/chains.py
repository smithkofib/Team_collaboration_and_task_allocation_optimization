# task_allocation/langchain_utils/chains.py
from langchain.chains import LLMChain
#from langchain_community.llms import OpenAI
#from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
#from langchain import OpenAI

from .prompts_copy import job_allocation_prompt, job_allocation_explanation_prompt
from .config import OPENAI_API_KEY

from .prompts_role_allocation import role_allocation_prompt, role_allocation_explanation_prompt

from .prompts_group_role_allocation import group_role_allocation_prompt, group_role_allocation_explanation_prompt

# Initialize OpenAI LLM
#llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.7,)
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, openai_api_key=OPENAI_API_KEY)

# Task Allocation Chain
job_allocation_chain = LLMChain(llm=llm, prompt=job_allocation_prompt)
# Role Allocation Chain
role_allocation_chain = LLMChain(llm=llm, prompt=role_allocation_prompt)
# Group Staff Role Allocation Chain
group_role_allocation_chain = LLMChain(llm=llm, prompt=group_role_allocation_prompt)

# Task Allocation Explanation Chain
job_allocation_explanation_chain = LLMChain(llm=llm, prompt=job_allocation_explanation_prompt)

# Role Allocation Explanation Chain
role_allocation_explanation_chain = LLMChain(llm=llm, prompt=role_allocation_explanation_prompt)

# Group Role Allocation Explanation Chain
group_role_allocation_explanation_chain = LLMChain(llm=llm, prompt=group_role_allocation_explanation_prompt)


role = []
candidate_gender = []
firstName = []
institutionName = []
degree = []
fieldOfStudy = []
startYear = []
endYear = []
jobTitle = []
companyName = []
startDate = []
endDate = []
responsibilities = [] 

def predict_job_allocation(school_names, heighest_degrees, fields_studied, companies, job_titles):
    return job_allocation_chain.invoke({
        "school_names": school_names,
        "heighest_degrees": heighest_degrees,
        "fields_studied": fields_studied,
        "companies": companies,
        "job_titles": job_titles,
    })

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


def predict_role_allocation(eduction, working_experience, position, job_description):
    print("eductionnnnnnnnn >>>>>>>> ", eduction)
    print("working_experienceeeeeee >>>>> ", working_experience[1]['job_title'])
    # Extracting data from the eduction and working_experience objects
  
    

    education_result = list(eduction.values())
    working_experience_result = list(working_experience.values())   

    # Extracting data from the eduction object
    for item in education_result:
        role.append(item["role"])
        institutionName.append(item["institution_name"])
        degree.append(item["degree"])
        fieldOfStudy.append(item["field_of_study"])
        startYear.append(item["start_year"])
        endYear.append(item["end_year"])
    
    # Extracting data from the working_experience object
    for item in working_experience_result:
        jobTitle.append(item["job_title"])
        companyName.append(item["company_name"])
        startDate.append(item["start_date"])
        endDate.append(item["end_date"])
        responsibilities.append(item["responsibilities"])
    
    

    # Print all 'first_name' values
    for item in education_result:
        #print("firstName >>>>> ", item['first_name'])
        firstName.append(item['first_name'])

    print("firstName >>>>> ", endDate)
    #print("firstName1111 >>>>> ", result[0]['first_name'])
    

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
        "position" : position,
        "job_description" : job_description
    
    })

def explain_role_allocation(position, predicted_employee):
    return role_allocation_explanation_chain.invoke({
        "position" : position,
        "predicted_employee": predicted_employee,
    })

def group_role_predict_allocation(eduction, working_experience, position, number_of_staffs, gender, job_description):
    # Extracting data from the eduction and working_experience objects
    education_result = list(eduction.values())
    working_experience_result = list(working_experience.values())   

    # Extracting data from the eduction object
    for item in education_result:
        role.append(item["role"])
        candidate_gender.append(item["gender"])
        institutionName.append(item["institution_name"])
        degree.append(item["degree"])
        fieldOfStudy.append(item["field_of_study"])
        startYear.append(item["start_year"])
        endYear.append(item["end_year"])
    
    # Extracting data from the working_experience object
    for item in working_experience_result:
        jobTitle.append(item["job_title"])
        companyName.append(item["company_name"])
        startDate.append(item["start_date"])
        endDate.append(item["end_date"])
        responsibilities.append(item["responsibilities"])
    
    

    # Print all 'first_name' values
    for item in education_result:
        #print("firstName >>>>> ", item['first_name'])
        firstName.append(item['first_name'])

    print("firstName >>>>> ", endDate)
    #print("firstName1111 >>>>> ", result[0]['first_name'])
    

    return group_role_allocation_chain.invoke({

        "first_name": education_result[0]['first_name'],
        "last_name": education_result[0]['last_name'],
        "candidate_gender" : candidate_gender,
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
        "position" : position,
        "number_of_staffs": number_of_staffs,
        "gender": gender,
        "job_description" : job_description
    
    })

def explain_group_role_allocation(position, predicted_employee):
    return group_role_allocation_explanation_chain.invoke({
        "position" : position,
        "predicted_employee": predicted_employee,
    })

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def explain_role_allocation11111(eduction, working_experience, predicted_employee):
    
    education_result = list(eduction.values())
    working_experience_result = list(working_experience.values())   

    # Extracting data from the eduction object
    for item in education_result:
        role.append(item["role"])
        institutionName.append(item["institution_name"])
        degree.append(item["degree"])
        fieldOfStudy.append(item["field_of_study"])
        startYear.append(item["start_year"])
        endYear.append(item["end_year"])
    
    # Extracting data from the working_experience object
    for item in working_experience_result:
        jobTitle.append(item["job_title"])
        companyName.append(item["company_name"])
        startDate.append(item["start_date"])
        endDate.append(item["end_date"])
    
    return role_allocation_explanation_chain.invoke({
        "first_name": education_result[0]['first_name'],
        "last_name": education_result[0]['last_name'],
        "school_names": institutionName,
        "degrees": degree,
        "fieldOfStudies": fieldOfStudy,
        "companies": companyName,
        "job_titles": jobTitle,
        "company_names": companyName,
        "start_date": startDate,
        "end_date": endDate,
        "predicted_employee": predicted_employee,
    })



print("--------------------------------------------------------------------------")

# print(explain_task_allocation("Computer Science", ["Software Engineer", "HR"]))

print("--------------------------------------------------------------------------")

# print(explain_task_allocation("Computer Science", ["Software Engineer", "HR"])['text'])
