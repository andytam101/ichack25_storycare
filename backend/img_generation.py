from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_image(prompt: str, commands):
  # returns dictionary of revised_prompt (maybe useful?) and url of image
  result = client.images.generate(
    model = "dall-e-3",
    prompt = f"{commands["image_generation"]}. {prompt}",
    n = 1,
    size="1024x1024",
    style="natural"
  ).data[0]

  return {
    "revised_prompt": result.revised_prompt,
    "url": result.url
  }



def generate_text(prompt):
  result = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "developer", "content": "Repeat exactly what the user say."},
      {"role": "user", "content": prompt}
    ]
  ).choices[0].message.content
  return result


commands = {
  "image_generation": "No text. No words. Just visuals. Make it cartoon, and for kids."
}

PROMPT = "Child playing outside with his inhaler."
print(generate_image(PROMPT, commands))
