import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client with API key from environment
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("⚠️  Warning: GEMINI_API_KEY not found in environment variables.")
    print("Please set your Google Gemini API key in the .env file as GEMINI_API_KEY=your_api_key_here")
    print("Get your API key at: https://makersuite.google.com/app/apikey")
    exit(1)

client = genai.Client(api_key=api_key)

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))

        image.save("generated_image.png")
        image.show()