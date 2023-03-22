    
import requests
import time
import os

    
def sending_picture_small(data_prompt):
    import openai 
    import os

    openai.api_type = "open_ai"
    openai.api_base = "https://api.openai.com/v1"
    openai.api_version = "2020-11-07"
    openai.api_key = os.getenv("REAL_OPENAI")
    
    
    response = openai.Image.create(
        prompt=data_prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url   
    

def sending_picture(data_prompt):
    import openai 
    import os

    openai.api_type = "open_ai"
    openai.api_base = "https://api.openai.com/v1"
    openai.api_version = "2020-11-07"
    openai.api_key = os.getenv("REAL_OPENAI")
    
    
    response = openai.Image.create(
        prompt=data_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def sending_picture_azure(data_prompt,res="1024x1024"):
    api_base = 'https://dalliwix.openai.azure.com/'
    api_key = "3205cc0a3d1540dda9c3c9def1097c65"
    api_version = '2022-08-03-preview'
    url = "{}dalle/text-to-image?api-version={}".format(api_base, api_version)
    headers= { "api-key": api_key, "Content-Type": "application/json" }
    body = {
        "caption": data_prompt,
        "resolution": res
    }
    submission = requests.post(url, headers=headers, json=body)
    operation_location = submission.headers['Operation-Location']
    retry_after = submission.headers['Retry-after']
    status = ""
    while (status != "Succeeded"):
        time.sleep(int(retry_after))
        response = requests.get(operation_location, headers=headers)
        status = response.json()['status']
    image_url = response.json()['result']['contentUrl']
    return image_url




