from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama 
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

information = """Donald John Trump (born June 14, 1946) is an American politician, media personality, and businessman who served as the 45th president of the United States from 2017 to 2021.

Trump received a Bachelor of Science in economics from the University of Pennsylvania in 1968. His father named him president of his real estate business in 1971. Trump renamed it the Trump Organization and reoriented the company toward building and renovating skyscrapers, hotels, casinos, and golf courses. After a series of business failures in the late 1990s, he launched successful side ventures, mostly licensing the Trump name. From 2004 to 2015, he co-produced and hosted the reality television series The Apprentice. He and his businesses have been plaintiffs or defendants in more than 4,000 legal actions, including six business bankruptcies.

Trump won the 2016 presidential election as the Republican Party nominee against Democratic Party candidate Hillary Clinton while losing the popular vote.[a] A special counsel investigation established that Russia had interfered in the election to favor Trump. During the campaign, his political positions were described as populist, protectionist, isolationist, and nationalist. His election and policies sparked numerous protests. He was the only U.S. president without prior military or government experience. Trump promoted conspiracy theories and made many false and misleading statements during his campaigns and presidency, to a degree unprecedented in American politics. Many of his comments and actions have been characterized as racially charged, racist, and misogynistic.

"""

if __name__ == '__main__':
    print("hello Langchain!")
    summary_template = """
    given the information {information} about a person from I want to create:
    1. a short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    #llm = ChatOpenAI(temperature=0, model_name= "gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)
    #print(os.getenv('OPENAI_API_KEY'))

