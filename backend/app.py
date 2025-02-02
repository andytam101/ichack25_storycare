from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from generate_content import generate_image, generate_short_story, generate_dalle_prompt

app = Flask(__name__)

# 🔹 Allow requests from React frontend
CORS(app, resources={r"/generate-story": {"origins": "http://localhost:3000"}}, supports_credentials=True)

@app.route("/generate-story", methods=["POST"])
def generate_story():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "")

        if not user_prompt:
            return jsonify({"error": "Prompt is required"}), 400

        paragraphs, images = generate_output(user_prompt)

        return jsonify({
            "captions": paragraphs,
            "images": images
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_output(prompt):
    paragraphs = generate_short_story(prompt).split("\n\n")
    dalle_prompts = [generate_dalle_prompt(p) for p in paragraphs]
    images = [generate_image(p) for p in dalle_prompts]

    return paragraphs, images

if __name__ == "__main__":
    app.run(debug=True)
