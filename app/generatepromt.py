

import time


def sending_prompt(prompt):
    import openai
    import os
    openai.api_type = "azure"
    openai.api_base = "https://dine.openai.azure.com/"
    openai.api_version = "2022-12-01"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    response = openai.Completion.create(
        engine="textgeneration",
        prompt=prompt,
        temperature=0.8,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None
    )
    print(response)
    return response.choices[0].text


def generate_code(prompt):
    import openai
    import os
    openai.api_type = "azure"
    openai.api_base = "https://dine.openai.azure.com/"
    openai.api_version = "2022-12-01"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    response = openai.Completion.create(
        engine="code",
        prompt=prompt,
        temperature=0.8,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None
    )
    print(response)
    return response.choices[0].text




def generate_web(prompt):
    import os
    import openai
    openai.api_type = "azure"
    openai.api_base = "https://dfgdfgdf.openai.azure.com/"
    openai.api_version = "2022-12-01"
    openai.api_key =os.environ['KEY_AZURE_AI'] 

    response = openai.Completion.create(
    engine="gpt3chat",
    prompt=f"<|im_start|>from this data {prompt} generate html code<|im_end|>\n",
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["<|im_end|>"])
    return response.choices[0].text









def generate_data_from_turbo(prompt):
    import os
    import openai
    openai.api_type = "azure"
    openai.api_base = "https://dfgdfgdf.openai.azure.com/"
    openai.api_version = "2022-12-01"
    openai.api_key =os.environ['KEY_AZURE_AI'] 

    response = openai.Completion.create(
    engine="gpt3chat",
    prompt=f"<|im_start|>{prompt}<|im_end|>\n",
    temperature=0.9,
    max_tokens=40000,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["<|im_end|>"])
    return response.choices[0].text







