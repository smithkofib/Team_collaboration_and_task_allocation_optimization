# task_allocation/langchain_utils/chains.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from .prompts import job_allocation_jinja_prompt, job_allocation_explanation_jinja_prompt
from .config import OPENAI_API_KEY

# Initialize OpenAI LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.7, api_key=OPENAI_API_KEY)

# Team Formation Chain
def predict_job_allocation(school_names, heighest_degrees, fields_studied, companies, job_titles):
    formatted_prompt = job_allocation_jinja_prompt.render(
        schools=school_names,
        heightest_degrees=heighest_degrees,
        fields_studied=fields_studied,
        companies=companies,
        job_titles=job_titles,
    )

    prompt = PromptTemplate(
        input_variables=[],
        template=formatted_prompt
    )

    # Chain using pipe syntax
    job_allocation_chain = prompt | llm
    response = job_allocation_chain.invoke({})
    return response


def explain_job_allocation(employee_fullname, school_names, heighest_degrees, fields_studied, companies, job_titles, predicted_job):
    formatted_prompt = job_allocation_explanation_jinja_prompt.render(
        employee_fullname=employee_fullname,
        schools=school_names,
        heightest_degree=heighest_degrees,
        fields_studied=fields_studied,
        companies=companies,
        job_title=job_titles,
        predicted_job=predicted_job,
    )

    prompt = PromptTemplate(
        input_variables=[],
        template=formatted_prompt
    )

    job_allocation_explanation_chain = prompt | llm
    response = job_allocation_explanation_chain.invoke({})
    return response


print("--------------------------------------------------------------------------")

print("--------------------------------------------------------------------------")
