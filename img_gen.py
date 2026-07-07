from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=KEY)

result = client.images.edit(
    model="gpt-image-1",
    image=open("./test_images/stock.png", "rb"),
    prompt="Create a line art of this face, this means using only lines without colour filling. Use minimal lines, with the same opacity and thickness. Imagine as if the drawing was done by a sharpie.",
)

image_base64 = result.data[0].b64_json
with open("output_image.png", "wb") as f:
    f.write(base64.b64decode(image_base64))