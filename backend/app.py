from flask import Flask, request, jsonify
from generate_content import generate_image, generate_short_story, generate_dalle_prompt
from utils import generate_starting_prompt

app = Flask(__name__)


@app.route("/prompt", methods=["POST"])
def prompt():
    # depends on frontend
    prompt1 = request.form["prompt1"]
    prompt2 = request.form.get("prompt2")
    child_name = request.form["child_name"]
    prompt_type = request.form["prompt_type"]

    # might add type in later (i.e. test, disease or treatment)
    starting_prompt = generate_starting_prompt(child_name, prompt_type, prompt1, prompt2)
    paragraphs, images = generate_output(starting_prompt)

    return jsonify({
        "captions": paragraphs,
        "images": images
    })


def generate_output(prompt):
    paragraphs = generate_short_story(prompt)
    paragraphs = paragraphs.split("\n\n")
    dalle_prompts = list(map(lambda x: generate_dalle_prompt(x), paragraphs))
    images = list(map(lambda x: generate_image(x), dalle_prompts))
    
    return paragraphs, images


if __name__ == "__main__":
    app.run(debug=True)
