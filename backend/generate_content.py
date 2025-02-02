from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_image(prompt):
    result = client.images.generate(
        model="dall-e-3",
        prompt="You are generating an image for a children's story book for the following section with no words, illustration only. " + prompt,
        size="1024x1024",
        style="vivid"
    ).data[0]
    
    return result


def generate_short_story(prompt):
    result = client.chat.completions.create(
        model="gpt-4o",
        messages= [
            {"role": "developer", "content": "Write a short story on the given prompt. Write 5 paragraphs, maximum 20 words each. Split them up in 2 newlines"},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=150
    ).choices[0].message.content

    return result


def generate_dalle_prompt(story):
    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are prompting Dall-e. Ensure all text references are removed from the generated image."},
            {"role": "user", "content": story},
        ],
        temperature=1,
        max_tokens=150
    ).choices[0].message.content

    return result

story = generate_short_story(".")
print(story)
paragraphs = story.split("\n\n")
dalle_prompts = list(map(lambda x: generate_dalle_prompt(x), paragraphs))
print(dalle_prompts)
images = list(map(lambda x: generate_image(x), dalle_prompts))
print(images)
