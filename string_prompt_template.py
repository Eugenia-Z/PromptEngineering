from langchain.prompts import PromptTemplate


# create a template and specify input variables
prompt_template = PromptTemplate(
    input_variables = ["adjective", "content"],
    template = "Tell me a {adjective} joke about {content}. "
)

# to format the template
prompt_template.format(adjective = "funny", content = "chickens")