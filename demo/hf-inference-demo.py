import os
from huggingface_hub import InferenceClient

from dotenv import load_dotenv
load_dotenv()

client = InferenceClient(
    provider="replicate",
    api_key=os.environ["HF_TOKEN"],
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="tencent/HunyuanImage-2.1",
)

image.show()