from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_story_text(prompt, n=10):                                                                                                          
    # generate complex story to pass into LLM -> return n paragraphs#
    print(n)
    messages = [
        {"role": "developer", "content": f"You are a story teller to a child. This child has a disease and you need to describe this disease in the form of a story, and in a friendly, empathetic tone. The story must be informative and can teach the child about the disease they have. Make it cute and child-friendly, but it must be an accurate representation of the disease. Generate it into {n} short paragraphs. Separate each paragraph with two newlines."},
        {"role": "user", "content": prompt}
    ]
    model = "gpt-4o"
    story = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    paragraphs = story.choices[0].message.content
    return paragraphs


def generate_chapter_to_prompt(chapter):
    messages = [
        {"role": "developer", "content": "You are a translater that takes in a chapter of the story and transforming that into a prompt that can be fed to an image generator that generates a cute image displayed to a child. The story will be about a disease, ensure the prompt tells the image generator to come up with an image that teaches the child about the disease, and that the image is related. Do not tell the AI to generate dialogue."},
        {"role": "user", "content": chapter}
    ]
    model = "gpt-4o"
    prompt = client.chat.completions.create(
        model=model,
        messages=messages
    )

    prompt_text = prompt.choices[0].message.content
    return prompt_text


def shorten_text(chapter, word_count=12):
    messages = [
        {"role": "developer", "content": f"You are summarising a story to a kid. You will be given a story and I want you to summarise it no more than {word_count} words."},
        {"role": "user", "content": chapter}
    ]
    model = "gpt-4o"
    summary = client.chat.completions.create(
        model=model,
        messages=messages
    )

    summmary_text = summary.choices[0].message.content
    return summmary_text
