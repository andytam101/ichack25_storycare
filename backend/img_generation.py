from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_image(prompt: str):
  # returns dictionary of revised_prompt (maybe useful?) and url of image
  result = client.images.generate(
    model = "dall-e-3",
    prompt = f"Only visuals. {prompt}",
    n = 1,
    size="1024x1024",
    style="natural"
  ).data[0]

  return {
    "revised_prompt": result.revised_prompt,
    "url": result.url
  }
