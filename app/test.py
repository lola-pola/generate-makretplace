import streamlit as st
import openai



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




def app():
    # Set the app title
    st.sidebar.title("OpenAI Web Page Generator")

        # Prompt the user for input
    prompt = st.sidebar.text_input("Enter a prompt to generate web page content:",key="prompt")
    # description = st.sidebar.text_input("Enter a prompt to generate web page description:",key="description")
    # more = st.sidebar.text_input("Enter a prompt to generate web page more content:",key="more")

        # Generate the text using OpenAI
    if st.sidebar.checkbox("Generate"):
        #milkshake shop
        
        # text1 = f"generate web content for an online milkshake shop that specializes in healthy unique and delicious milkshakes"
        # text2 = f"generate a clear description of your milkshake shop and write descriptions for 5 of your milkshakes,for each milkshake, provide a prompt for generating Dali-esque descriptions"
        # text3= f"generate manu from all the ingredients with prices in $"
        # content = generate_text(prompts)
        prompt = f"<!-- Create a web page for online shop sells {prompt} ' -->\n<!DOCTYPE html>"
        content = generate_html(prompt)
        st.markdown(content, unsafe_allow_html=True)
app()