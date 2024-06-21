examples = [ 
   {
       "menu" : {
        "menu_item" : "Just Veggie Omelet",
        "menu_description" : "Sauteed spinach and mushrooms, goat cheese."    
       },
        "attrib_structure" : {
            "primary_protein" : "veggie",
            "secondary_protein" :  "egg",
            "tertiary_protein" : "",
            "Cheese Types": "Cheese",
            "Lettuce Types": "Spinach"
        }
    },
   {
        "menu" : {
            "menu_item" : "Buddha bowl",
            "menu_description" : "Assorted vegetables with egg, bacon, chicken, Spinach, Cheddar and black red bean sausage",
        },
        "attrib_structure" : {
            "primary_protein": "chicken",
            "secondary_protein": "bacon",
            "tertiary_protein": "egg",
            "Cheese Types": "Cheddar",
            "Lettuce Types": "Spinach"
        }
    },
   {
        "menu" : {
            "menu_item" : "Bacon topped grilled Organic Chicken Breast",
            "menu_description" : "Tomato, Spring Mix with American cheese, suasage and avacado",
        },
        "attrib_structure" : {
            "primary_protein": "Chicken",
            "secondary_protein": "Bacon",
            "tertiary_protein": "sausage",
            "Cheese Types": "American Cheese",
            "Lettuce Types": "Spring Mix"
        }
    }
]

from langchain.prompts import (
    FewShotChatMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

# This is a prompt template used to format each individual example
example_prompt =ChatPromptTemplate.from_messages(
    [
        ("system", "Enter Menu Description:"),
        ("human", "{menu}"),
        ("ai", "{attrib_structure}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt = example_prompt,
    examples = examples,
)

print(few_shot_prompt.format())

final_prompt = ChatPromptTemplate.from_meesages(
    [
        ("system", "You are a wondrous menu ingredient mapper."),
        ("human", "{menu}"),
        ("ai", "{attrib_structure}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt = example_prompt,
    examples = examples,
)

print(few_shot_prompt.format())