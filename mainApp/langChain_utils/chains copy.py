# task_allocation/langchain_utils/chains.py
from langchain.chains import LLMChain
#from langchain_community.llms import OpenAI
#from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

#from langchain import OpenAI

from .prompts import job_allocation_jinja_prompt, job_allocation_explanation_jinja_prompt
from .config import OPENAI_API_KEY

# Initialize OpenAI LLM
#llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.7,)
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, openai_api_key=OPENAI_API_KEY)


# Team Formation Chain
def predict_job_allocation(school_names, heighest_degrees, fields_studied, companies, job_titles):
    
    formatted_prompt = job_allocation_jinja_prompt.render(
        schools= school_names,
        heightest_degrees= heighest_degrees,
        fields_studied= fields_studied,
        companies= companies,
        job_titles= job_titles,)
    
    prompt = PromptTemplate(
    input_variables=[],
    template=formatted_prompt) 
    # Task Allocation Chain
    job_allocation_chain = LLMChain(llm=llm, prompt=prompt)
    response = job_allocation_chain.run({})
    return response


def explain_job_allocation(employee_fullname, school_names, heighest_degrees, fields_studied, companies, job_titles, predicted_job):
    
    formatted_prompt = job_allocation_explanation_jinja_prompt.render(
        employee_fullname = employee_fullname,
        schools = school_names,
        heightest_degree = heighest_degrees,
        fields_studied = fields_studied,
        companies = companies,
        job_title = job_titles,
        predicted_job = predicted_job,
    )
    prompt = PromptTemplate(
    input_variables=[],
    template=formatted_prompt) 
    job_allocation_explanation_chain = LLMChain(llm=llm, prompt=prompt)

    response = job_allocation_explanation_chain.run({})

    return response


print("--------------------------------------------------------------------------")

# print(explain_task_allocation("Computer Science", ["Software Engineer", "HR"]))

print("--------------------------------------------------------------------------")

# print(explain_task_allocation("Computer Science", ["Software Engineer", "HR"])['text'])
