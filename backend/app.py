from flask import Flask, request, jsonify
from generate_content import generate_image, generate_short_story, generate_dalle_prompt

app = Flask(__name__)


@app.route("/prompt", methods=["POST"])
def prompt():
    user_prompt = request.form["prompt"]
    # might add type in later (i.e. test, disease or treatment)
    paragraphs, images = generate_output(user_prompt)

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
