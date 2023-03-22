import streamlit as st
import openai
from streamlit_chat import message
from daliegenerator import sending_picture ,sending_picture_small ,sending_picture_azure



st.set_page_config(page_title="Generating Page Content", page_icon="📈")
st.markdown("# Generating Page Content")

# Set up OpenAI API credentials
openai.api_type = "azure"
openai.api_base = "https://dalliwix.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "3205cc0a3d1540dda9c3c9def1097c65"

# Define a function to generate text using OpenAI
def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text


# Define a function to generate text using OpenAI
def generate_gpt(prompt):
    response = openai.Completion.create(
        engine="gpeta",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text


# Define a function to generate text using OpenAI
def generate_gpt_chat(prompt):
    response = openai.Completion.create(
        engine="gpeta",
        prompt=prompt,
        temperature=0.9,
        max_tokens=1024
        
        
    )
    return response.choices[0].text

def generate_text_dali(prompt):
    _prompt = f'Generate Dali-E descriptions from this statements "{prompt}" website template'
    response = openai.Completion.create(  
       
        engine="davinci",
        prompt=_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    return response.choices[0].text

# Define the Streamlit app



def generate_html(prompt):
    response = openai.Completion.create(
            engine="code",
            prompt= prompt, #"<!-- Create a web page for online shop sells milkshake ' -->\n<!DOCTYPE html>",
            temperature=1,
            max_tokens=6218,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=None)
    return response.choices[0].text



# @st.cache_data
def app():
    st.sidebar.title("OpenAI Web Page Content")

    prompt = st.sidebar.text_input("Enter a prompt to generate web page content:",key="prompt")

    if st.sidebar.checkbox("Generate"):

        home, catalog, community , about , support ,soe= st.tabs(["Home", "Catalog", "Community","About","Support","Soe"])

        with home:
            tmp_home_prompt = "generate website home page data for:"+prompt
            tmp_home_icon = "generate icon for :"+prompt
            _prompt = generate_text_dali(tmp_home_prompt)
            title =  generate_text(f'create simple title {tmp_home_prompt} ')
            st.header(title)
            st.image(sending_picture_azure(tmp_home_icon),caption='icon', width=200)
            st.image(sending_picture_azure(tmp_home_prompt),caption=title, width=400)
            _prompt =  generate_text(f'generate homepage information for: {prompt} ')
            st.write(_prompt)
            
        with catalog:
           title =  generate_text(f'create catalog title for: {prompt} ')
           st.header(title)
           
           data =  generate_text(f'generate catalog for 10 product max: {prompt} ')
           if "-" in data:
                __data = data.split('-')
           else:
                __data = data.split('•')
           for i in __data:
               st.write(i)
               if ":" in i:
                   st.image(sending_picture_azure(i),caption='icon', width=150)
               else:
                   st.image(sending_picture_azure(i),caption='icon', width=150)
 
        with community:
           st.write(generate_gpt(f'can you write customer recommendation on {prompt} , please write 10 recommendation '))
        
        with about:
           st.write(generate_text(f'generate about information add year of openning , some words abount the stuff: {prompt} '))  
 
        with soe:
           st.write(generate_text(f'generate key words for soe for : {prompt} '))
        
        with support:
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
        
        
        
        
        
        
#8-6<>6*8
        
  

        
        






        
        
        
        
        
        
        
        
        
        

                
app()