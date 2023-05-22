# import streamlit as st
# import openai
# # from daliegenerator import sending_picture ,sending_picture_small ,sending_picture_azure
# from daliegenerator import sending_picture ,sending_picture_small ,sending_picture_azure
# st.set_page_config(page_title="generating template", page_icon="📈")
# import os
# st.markdown("# Generating Template")


# openai.api_type = "azure"
# openai.api_base = "https://dalliwix.openai.azure.com/"
# openai.api_version = "2022-12-01"
# openai.api_key = os.environ['KEY_AZURE_AI'] 
# # Set up OpenAI API credentials

# # Define a function to generate text using OpenAI
# def generate_text(prompt):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     return response.choices[0].text


# def generate_text_dali(prompt):
#     _prompt = f'Generate Dali-E descriptions from this statements "{prompt}" website template'
#     response = openai.Completion.create(  
       
#         engine="davinci",
#         prompt=_prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=1,
#     )
#     return response.choices[0].text

# # Define the Streamlit app



# def generate_html(prompt):
#     response = openai.Completion.create(
#             engine="code",
#             prompt= prompt, #"<!-- Create a web page for online shop sells milkshake ' -->\n<!DOCTYPE html>",
#             temperature=1,
#             max_tokens=6218,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#             best_of=1,
#             stop=None)
#     return response.choices[0].text



# # @st.cache_data
# def app():
#     st.sidebar.title("OpenAI Web Page Generator")

#     prompt = st.sidebar.text_input("Enter a prompt to generate web page content:",key="prompt")

#     if st.sidebar.checkbox("Generate"):
  
#         col1, col2, col3= st.columns([5,5,5])
#         with st.spinner(text='In progress'):
#             with col1:
#                 _prompt = generate_text_dali(prompt)
#                 title =  generate_text(f'create simple title {_prompt} ')
#                 st.image(sending_picture_azure(_prompt),caption=title,use_column_width="always")
#                 with st.expander("generate code"):
#                     __prompt = f"<!-- Create a web page for {prompt} ' -->\n<!DOCTYPE html>"
#                     st.markdown(generate_html(__prompt), unsafe_allow_html=True)
#             with col2:
#                 _prompt = generate_text_dali(prompt)
#                 title =  generate_text(f'create simple title {_prompt} ')
#                 st.image(sending_picture_azure(_prompt),caption=title,use_column_width="always")
#                 with st.expander("generate code"):
#                     __prompt = f"<!-- Create a web page for {prompt} ' -->\n<!DOCTYPE html>"
#                     st.markdown(generate_html(__prompt), unsafe_allow_html=True)
#             with col3:
#                 _prompt = generate_text_dali(prompt)
#                 title =  generate_text(f'create simple title {_prompt} ')
#                 st.image(sending_picture_azure(_prompt),caption=title,use_column_width="always")
#                 with st.expander("generate code"):
#                     __prompt = f"<!-- Create a web page for {prompt} ' -->\n<!DOCTYPE html>"
#                     st.markdown(generate_html(__prompt), unsafe_allow_html=True)

                
# app()