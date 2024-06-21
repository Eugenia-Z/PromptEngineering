from langchain.prompts import PromptTemplate, StringPromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

template = """
Given the user's name, write them a personalized greeting.

User's name: {name}

Your response:
"""

prompt = PromptTemplate.from_template(template)
class NamePrompt(StringPromptTemplate):
    def format(self, **kwargs) -> str:
        name = kwargs["name"]
        return prompt.format(name = name)

name_prompt = NamePrompt(input_variables = ["name"])
print(name_prompt.format(name="John"))
openai = ChatOpenAI(model_name="gpt-3.5-turbo")
LLMChain = LLMChain(llm=openai, prompt=name_prompt)
LLMChain.invoke({"name":"John"})