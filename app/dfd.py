from io import StringIO 
import streamlit as st
import openai
import json
import os


# Identify your target keywords: Start by researching and identifying the keywords that your potential customers are using to search for ice cream online. Use tools like Google Keyword Planner or Ahrefs to find relevant keywords that have a high search volume and low competition.

# Optimize your website content: Once you have identified your target keywords, you need to optimize your website content accordingly. This includes optimizing your meta titles and descriptions, headers, and body content to include your target keywords in a natural and engaging way.

# Build quality backlinks: Backlinks are an important factor in SEO, as they signal to search engines that your website is authoritative and relevant. Reach out to relevant websites and blogs to see if they would be willing to link to your ice cream website.

# Local SEO: If your ice cream business has a physical location, then you should also focus on local SEO. This includes optimizing your Google My Business listing, adding your business to local directories, and getting positive reviews from customers.

# Monitor and analyze your website performance: Use tools like Google Analytics and Google Search Console to track your website's performance and identify areas for improvement. Continuously analyze your website's data to see what's working and what's not, and adjust your SEO strategy accordingly.



# Set up API key
openai.api_key=st.text_input('here you need need to put azure open ai key', type="password")
openai.api_base=st.text_input('add your base end point')
openai.api_type = st.text_input('select type open_ai/azure')
openai.api_version = "2022-12-01"

def json_cutter(filename,split_length):
    json_str = str(filename)
    sub_strings = [json_str[i:i+split_length] for i in range(0, len(json_str), split_length)]
    master_list = []
    #with st.spinner('cutting data'):
    for sub in sub_strings:
       print('test')
       sub_list = list(sub)
       master_list.append(sub_list)
    st.success('Done!')
    return master_list




def sendin_to_gpt(text_data ,data,model):
    print(f'sending data {text_data} {data} ')
    response = openai.Completion.create(
        engine=model,
        prompt=text_data + data,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    keywords = response.choices[0].text
    return keywords.strip().split("\n")



data =None

filename = st.file_uploader("Upload json file to use in GPT ", type=["json"])


## main params
split_length = 4000
text_data = "sending you json: "

if filename is not None:
    filename = filename.getvalue()
    if st.checkbox('show file'):
        st.write(json.loads(filename))
    if st.checkbox('start coverting file'):
        with st.spinner('Wait for data spliting ...'):
        	chr_list = json_cutter(filename=json.loads(filename),split_length=split_length)
        print(chr_list)
        if chr_list:
            #model = st.selectbox('model',("text-davinci-002","text-davinci-003"))
            model = st.text_input('put model name')
            if st.checkbox('start sending to open ai'):
                with st.spinner('Wait data process it...'):
                    for chr in chr_list:
                        print(len(chr_list))
                        _chr = ''.join(chr)
                        if chr == chr_list[0]:
                            text_data=text_data
                            data = sendin_to_gpt(text_data,data=_chr,model=model)
                        elif chr == chr_list[-1]:
                            data = 'this is the end of the json'
                            text_data = _chr
                            data = sendin_to_gpt(text_data,data=data,model=model)
                        else:
                            text_data=''
                            data = sendin_to_gpt(text_data,data=_chr,model=model)
                        
print('wellcom to data explain')
if data is not None:
    q_models = st.text_input('put model name')
    question = st.text_input('ask a question')
    if question != '':
        st.write(sendin_to_gpt(text_data=question,data='in json that i sent ',model=q_models))

