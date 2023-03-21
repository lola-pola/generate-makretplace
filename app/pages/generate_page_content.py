import streamlit as st
import openai
# from daliegenerator import sending_picture ,sending_picture_small ,sending_picture_azure
from daliegenerator import sending_picture ,sending_picture_small ,sending_picture_azure
st.set_page_config(page_title="Generating Page Content", page_icon="📈")
st.markdown("# Generating Page Content")


openai.api_type = "azure"
openai.api_base = "https://dalliwix.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "3205cc0a3d1540dda9c3c9def1097c65"
# Set up OpenAI API credentials

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

        home, catalog, community , about , support = st.tabs(["Home", "Catalog", "Community","About","Support"])

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
           data =  generate_text(f'generate catalog for : {prompt} ')
           st.write(data)

        with community:
           st.header("An owl")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        
        with about:
           st.header("An owl")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)       
        
        with support:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)       
#8-6<>6*8
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                
app()