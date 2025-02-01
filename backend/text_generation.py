from openai import OpenAI
from api_key import API_KEY


client = OpenAI(api_key=API_KEY)


def generate_story_text(prompt, n=10):                                                                                                          
    # generate complex story to pass into LLM -> return n paragraphs
    messages = [
        {"role": "developer", "content": f"You are a story teller to a child. This child has a disease and you need to describe this disease in the form of a story, and in a friendly, empathetic tone. Generate it into {n} short paragraphs. Separate each paragraph with two newlines."},
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
        {"role": "developer", "content": "You are a translater that takes in a chapter of the story and transforming that into a prompt that can be fed to an image generator that generates a cute image displayed to a child."},
        {"role": "user", "content": chapter}
    ]
    model = "gpt-4o"
    prompt = client.chat.completions.create(
        model=model,
        messages=messages
    )

    prompt_text = prompt.choices[0].message.content
    return prompt_text


# generate_complex_text("My child has ventricular septal defect. Talk about the diagnosis.")


# story = 'Once upon a time in the magical kingdom of Heartland, there was a little heart named Piper. Piper was full of joy, always working hard to pump love and life through the kingdom. One day, the wise Heart Doctor, who cared for all the hearts in the kingdom, noticed something special about Piper.\n\nInside Piper\'s cozy chambers, there was a tiny door between two of her important rooms, the left ventricle and right ventricle. This door is called a "septal defect." It\'s a bit like a secret passageway that none of the other hearts had. In Heartland, sometimes hearts are born with these secret doors, and it\'s called a Ventricular Septal Defect, or VSD.\n\nThe wise Heart Doctor explained that this special door allowed some extra blood to swish around in Piper\'s rooms, making a gentle whooshing sound that could be heard with a magic listening device called a stethoscope. This swishing made Piper work a bit harder, but she was still full of spunk and kept the kingdom in good spirits.\n\nTo help Piper, the Heart Doctor kept an eye on her, listening to the swishes and watching if the secret door affected how she grew and played. Sometimes, the doctor\'s help was enough to let Piper live happily with her special door. Other times, they gathered a team of skilled heart builders to mend the door so Piper could work just like all the other hearts.\n\nThroughout this adventure, Piper was never alone. She had the love and care of her kingdom, and her family of little hearts cheered her on with every beat. And no matter what, Piper knew she was brave and strong, a unique heart with a story all her own. \n\nAnd so, through the power of love, friendship, and a bit of magical help, Piper thrived in Heartland, bringing joy and warmth wherever her beats were heard. And that, my dear friend, is the story of Piper and her special little door.💖'
# print(story)


# completion = client.chat.completions.create(
#     model="gpt-4o",                                                                                   
#     messages=[
#         {"role": "developer", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)
