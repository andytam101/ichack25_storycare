from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_image(summary_text: str, commands):
  # returns dictionary of revised_prompt (maybe useful?) and url of image
  result = client.images.generate(
    model = "dall-e-3",
    prompt = f"{commands["image_generation"]}. {summary_text}",
    n = 1,
    size="1024x1024",
    style="natural"
  ).data[0]

  print(result.url)

  return {
    "revised_prompt": result.revised_prompt,
    "url": result.url
  }


commands = {
  "image_generation": "Generate an image for the following statement."
}

print(generate_image("Jack has asthma and uses his inhaler twice a day", commands))
