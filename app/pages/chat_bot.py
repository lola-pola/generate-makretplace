from streamlit_chat import message
import streamlit as st
import openai
import os

openai.api_type = "azure"
openai.api_base = "https://dalliwix.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.environ['KEY_AZURE_AI'] 



def generate_gpt_chat(prompt):
    response = openai.Completion.create(
        engine="gpeta",
        prompt=prompt,
        temperature=0.5,
        max_tokens=8000
        
        
    )
    print(response)
    return response.choices[0].text




if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input=st.text_input("You:",key='input')
if user_input:
    output=generate_gpt_chat(user_input)
    #store the output
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')     
