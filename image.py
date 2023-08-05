import os
import openai
from dotenv import load_dotenv
load_dotenv()
import requests
from PIL import Image



# AI token
openai.api_key = os.getenv("OPENAI_API_KEY")
# function for text-to-image generation
# using create endpoint of DALL-E API
# function takes in a string argument
def generate(text):
    print(text)
    res = openai.Image.create(
        # text describing the generated image
        prompt=text,
        # number of images to generate
        n=1,
        # size of each generated image
        size="256x256",
    )
    # returning the URL of one image as
    # we are generating only one image
    return res["data"][0]["url"]

# prompt describing the desired image
text = "batman art in red and blue color"
# calling the custom function "generate"
# saving the output in "url1"
url1 = generate(text)
# using requests library to get the image in bytes
response = requests.get(url1)
# using the Image module from PIL library to view the image
Image.open(response.raw)