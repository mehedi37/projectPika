import os
import openai
from dotenv import load_dotenv
load_dotenv()
import requests
from PIL import Image



# AI token
openai.api_key = os.getenv("OPENAI_API_KEY")

def talk(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    return (response.choices[0].message.content)


# def image_gen(prompt):
#     print(prompt)
#     image_resp = openai.Image.create(
#         prompt= prompt,
#         n=4,
#         size="1024x1024"
#     )
#     response = requests.post(
#     API_ENDPOINT,
#     headers={
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {openai.api_key}',
#     },
#     data=json.dumps(data),
#     )

def image_gen(text):
    print(text)
    res = openai.Image.create(
        prompt=text,
        n=1,
        size="256x256",
    )
    url1 = generate(res["data"][0]["url"])
    response = requests.get(url1)
    Image.open(response.raw)
    return
    # return res["data"][0]["url"]

