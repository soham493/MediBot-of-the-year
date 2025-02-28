# setup GROQ API key
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# print("API Key:", GROQ_API_KEY)



#convert image to required format
import base64 

# image_path = "acn_image.jpg"
def encoded_image(image_path):
    image_file = open(image_path, "rb") #read binary
    return base64.b64encode(image_file.read()).decode('utf-8') #encoded image function



#setup multimedia LLM
from groq import Groq


query = "Is this somethig wrong with my face?"
model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):

    client = Groq()

    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model 
    )

    return chat_completion.choices[0].message.content