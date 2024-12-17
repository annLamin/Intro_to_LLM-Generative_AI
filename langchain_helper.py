from secret_key import openapi_key
import os
# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def get_country_and_university_name(university):
    prompt_template_country = PromptTemplate(
    input_variables = ['course'],
    template =  "I want to search for a PhD. position in Europe, recommend a country for a {course} graduate. give one sentence why that country is the best"
    )
    country_chain = LLMChain(llm=llm, prompt=prompt_template_country, output_key='country_name')

    prompt_template_items = PromptTemplate(
    input_variables = ['country_name'],
    template = "suggest three universities from {country_name} in a form of a list"
    )
    university_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="university_names")

    chain = SequentialChain(
    chains = [country_chain,university_item_chain],
    input_variables = ['course'],
    output_variables = ['country_name','university_names']
    )

    response = chain({'course': 'Data Science'})
    return response
if __name__ == '__main__':
    print(get_country_and_university_name('Data Science'))