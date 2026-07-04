from openai import OpenAI
import base64

client = OpenAI(api_key="YOUR_API_KEY")

result = client.images.edit(
    model="gpt-image-1",
    image=open("input_image.png", "rb"),
    prompt="Create a line art of this face. Use minimal lines, with the same opacity and thickness. Imagine as if the drawing was done by a sharpie.",
)

image_base64 = result.data[0].b64_json
with open("output_image.png", "wb") as f:
    f.write(base64.b64decode(image_base64))