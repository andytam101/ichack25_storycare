from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from generate_content import generate_image, generate_short_story, generate_dalle_prompt
from utils import generate_starting_prompt

app = Flask(__name__)

# 🔹 Allow requests from React frontend
CORS(app, resources={r"/generate-story": {"origins": "http://localhost:3000"}}, supports_credentials=True)

@app.route("/generate-story", methods=["POST"])
def generate_story():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "")
        user_prompt_2 = data.get("prompt2", "")
        prompt_type = data.get("promptType", "")
        username = data.get("username", "")

        # might add type in later (i.e. test, disease or treatment)
        starting_prompt = generate_starting_prompt(username, prompt_type, user_prompt, user_prompt_2)
        if not user_prompt or not prompt_type:
            return jsonify({"error": "Prompt is required"}), 400

        paragraphs, images = generate_output(starting_prompt)
        return jsonify({
            "captions": paragraphs,
            "images": images
        })
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


def generate_output(prompt):
    paragraphs = generate_short_story(prompt).split("\n\n")
    dalle_prompts = [generate_dalle_prompt(p) for p in paragraphs]
    images = [generate_image(p) for p in dalle_prompts]

    return paragraphs, images


if __name__ == "__main__":
    app.run(debug=False)
