from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_story_text(prompt, commands):                                                                                                          
    # generate simple story to pass into LLM -> return n paragraphs#
    messages = [
        {"role": "developer", "content": commands["story_generation"] + f" You must separate the story into {commands["chapters_count"]} paragraphs. Separate each paragraph with 2 newlines."},
        {"role": "user", "content": prompt}
    ]
    model = "gpt-4o"
    story = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    paragraphs = story.choices[0].message.content
    return paragraphs


def generate_section_to_prompt(chapter, commands):
    messages = [
        {"role": "developer", "content": commands["prompt_generation"]},
        {"role": "user", "content": chapter}
    ]
    model = "gpt-4o"
    prompt = client.chat.completions.create(
        model=model,
        messages=messages
    )

    prompt_text = prompt.choices[0].message.content
    return prompt_text


def shorten_text(chapter, commands):
    messages = [
        {"role": "developer", "content": commands["summary_generation"] + f" Your response should be at most {commands["summary_words_limit"]} words"},
        {"role": "user", "content": chapter}
    ]
    model = "gpt-4o"
    summary = client.chat.completions.create(
        model=model,
        messages=messages
    )

    summmary_text = summary.choices[0].message.content
    return summmary_text
