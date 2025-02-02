from combined_text_generation import *
from combined_img_generation import *

def get_images_and_captions_from_user_prompt(prompt, commands):
    print("Generating story")
    paragraphs = generate_story_text(prompt, commands)
    paragraphs = paragraphs.split("\n\n")
    print("Generating summaries")
    summarised_text = list(map(lambda x: shorten_text(x, commands), paragraphs)) 
    print("Generating images")
    images_data = list(map(lambda x: generate_image(x, commands), summarised_text))   

    return paragraphs, images_data, summarised_text


commands = {
    "story_generation": "You are an author of a children's short story book about a disease or illness that they have. You will need to explain this illness or disease to them in a short story format that is informative, empathetic and avoids the use of overly complicated unexplained jargon. The story must teach the child about what the disease is and what they may expect now that they are diagnosed. Make it cute, child-friendly and not scary but it should be an accurate representation of the disease.",
    "chapters_count": 2,
    "summary_generation": "You are summarising a short story that informs a child of a disease or illness that they have. You will be given a story of this illness or disease that is affecting this kid. Remain informative but child-friendly. This summary will be used to make an image.",
    "summary_words_limit": 8,
    "image_generation": "You will take each chapter of the summary text and transform it into an image. The image will be a cartoon that will form a part of a cohesive story that will be shown to a child. The story will be about a disease and ensure the image generator comes up with an image that will be a part of a series of images that teach the child about a disease. This will be like what is seen in a picture book. Ensure the generator comes up with an image that teaches the child about the disease, and that the image is related to that disease and the summary text. Tell the image generator to not generate any dialogue, text, letters, typography or anything that resembles written language onto the image. The image should only include cartoon drawings only, not real-life humans."
}

# thing that user types in
user_prompt = "Jack has acute lymphocytic leukemia. He does not know what that is. Please explain it to him."
print(get_images_and_captions_from_user_prompt(user_prompt, commands))