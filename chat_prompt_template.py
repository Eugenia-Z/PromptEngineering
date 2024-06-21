# chat_prompt_template is for multi-turn conversations with chat history
from langchain.prompt import chatPromptTemplate

template = chatPromptTemplate.from_messages([
    ("system", "Your are a helpful AI."),
    ("human", "Hello!"),
    ("ai", "Hi there!"),
    ("human", "{user_input}"),
])

template.format_messages(user_input = "What is your name?")