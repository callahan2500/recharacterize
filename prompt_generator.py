import os
import openai
import pandas as pd
import csv 

#API KEYS
openai.api_key = os.environ.get("OPENAI_KEY")
assistant_key = os.environ.get("OPENAI_ASSISTANT_KEY")


#PROMPT#
get_prompts = "You are using an LLM. Write a common, one sentence prompt for it. Just provide the prompt"
get_text = "Write a 100 to 500 word text. The text should be creative. You can pick the topic. Ideally it should be written at a middle school reading level"

#FUNCTIONS#
def get_a_prompt(prompt):
    return(openai.chat.completions.create(
        model="gpt-4o",
        messages = [
            {"role":"system", "content": "You are an expert LLM prompt writer."},
            {"role":"user", "content":prompt}

        ]
    ))


#LIST OF PROMPTS#
prompts = []
texts = []

for i in range (0,500):
    test_prompts = get_a_prompt(get_prompts)
    test_character_loss = get_a_prompt(get_text)
    prompts.append(test_prompts.choices[0].message.content)
    texts.append(test_character_loss.choices[0].message.content)
    print("DONE")

#EXPORT PROMPTS

with open('test_prompts', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prompts)

with open('test_character_loss', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(texts)