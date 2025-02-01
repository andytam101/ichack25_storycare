from flask import Flask, request, jsonify
from text_generation import generate_story_text, generate_chapter_to_prompt, shorten_text
from img_generation import generate_image
import json


app = Flask(__name__)

@app.route("/prompt", methods=["POST"])
def prompt():
    if request.method == "POST":
        prompt = request.form["prompt"] # change this to whatever matches the frontend
        
        with open("sample.json", "r") as f:
            data = json.load(f)
            f.close()

        # list of dictionaries containing (revised_prompt, url)
        _, _, all_images_data, all_captions = get_images_and_captions_from_user_prompt(prompt, data)   
        return jsonify({
            "all_images": all_images_data,
            "all_captions": all_captions
        })


def get_images_and_captions_from_user_prompt(prompt, commands):
    print("Generating story")
    paragraphs = generate_story_text(prompt, commands)
    paragraphs = paragraphs.split("\n\n")
    print("Generating prompts")
    img_prompts = list(map(lambda x: generate_chapter_to_prompt(x, commands), paragraphs))
    print("Generating images")
    images_data = list(map(lambda x: generate_image(x, commands), img_prompts))
    print("Generating summaries")
    summarised_text = list(map(lambda x: shorten_text(x, commands), paragraphs))
    return paragraphs, img_prompts, images_data, summarised_text


if __name__ == "__main__":
    # app.run(debug=True)
    paras, prompts, images, summaries = get_images_and_captions_from_user_prompt("My child has asthma. Show me the diagnosis")

