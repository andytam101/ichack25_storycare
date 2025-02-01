from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_image(prompt):
  # returns dictionary of revised_prompt (maybe useful?) and url of image
  result = client.images.generate(
    model = "dall-e-3",
    prompt = prompt + "Do not use dialogue and fit for a children's story.",
    n = 1,
    size="1024x1024"
  ).data[0]

  return {
    "revised_prompt": result.revised_prompt,
    "url": result.url
  }
