from flask import Flask, request, jsonify
from generate_content import generate_image, generate_short_story, generate_dalle_prompt

app = Flask(__name__)

@app.route("/prompt", methods=["POST"])
def handle_prompt():
    user_prompt = request.json.get("prompt")  # Use request.json instead of request.form for JSON body
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate output when the API is called, NOT at startup
    paragraphs = generate_short_story(user_prompt).split("\n\n")
    dalle_prompts = [generate_dalle_prompt(p) for p in paragraphs]
    images = [generate_image(p) for p in dalle_prompts]

    return jsonify({
        "captions": paragraphs,
        "images": images
    })

if __name__ == "__main__":
    app.run(debug=False)

