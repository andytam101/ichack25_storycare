from flask import Flask, request, jsonify
from text_generation import generate_story_text, generate_chapter_to_prompt
from img_generation import generate_image


app = Flask(__name__)

@app.route("/prompt", methods=["POST"])
def prompt():
    if request.method == "POST":
        prompt = request.form["prompt"] # change this to whatever matches the frontend
        
        # list of dictionaries containing (revised_prompt, url)
        all_images_data = get_images_from_user_prompt(prompt)   
        return jsonify({
            "all_images": all_images_data
        })


def get_images_from_user_prompt(prompt):
    paragraphs = generate_story_text(prompt)
    img_prompts = list(map(generate_chapter_to_prompt, paragraphs.split("\n\n")))
    images_data = list(map(generate_image, img_prompts))
    return images_data


if __name__ == "__main__":
    app.run(debug=True)
