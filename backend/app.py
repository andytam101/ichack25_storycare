from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from generate_content import generate_image, generate_short_story, generate_dalle_prompt
from utils import generate_starting_prompt

app = Flask(__name__)

# 🔹 Allow requests from React frontend
CORS(app, resources={r"/generate-story": {"origins": "http://localhost:3000"}}, supports_credentials=True)

@app.route("/generate-story", methods=["POST"])
def generate_story():

    # return jsonify({
    #     "captions": ["Once there was a brave child named Dummy who was going to the doctor for a special test called an ECG. Dummy was curious but also a little nervous. So, the doctor explained it simply.", "The doctor said, \"An ECG is like a camera for your heart! It takes a special picture by using stickers on your skin, but it doesn't hurt at all.\"", "Dummy felt better knowing it was just a friendly heart picture. Once it was done, Dummy smiled and said, \"That was easy peasy!\" The heart picture showed Dummy's heart was as strong as a superhero!"],
    #     "images": ["https://oaidalleapiprodscus.blob.core.windows.net/private/org-f90WsAXXoT74C7KIrKHfQNLF/user-aPZnYv1fPc18oeNp5tW2GGSL/img-vQ5MeNF0H7MkMgZDaiPwRKoS.png?st=2025-02-02T05%3A26%3A40Z&se=2025-02-02T07%3A26%3A40Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-02-01T15%3A30%3A32Z&ske=2025-02-02T15%3A30%3A32Z&sks=b&skv=2024-08-04&sig=Ycj5/9rnr3jqTzTaRiJi20Aus56qnQAMTrsivvUJj4c%3D", "https://oaidalleapiprodscus.blob.core.windows.net/private/org-f90WsAXXoT74C7KIrKHfQNLF/user-aPZnYv1fPc18oeNp5tW2GGSL/img-F3HisUVZTrPTzrJERENYztvX.png?st=2025-02-02T05%3A26%3A56Z&se=2025-02-02T07%3A26%3A56Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-02-02T00%3A33%3A41Z&ske=2025-02-03T00%3A33%3A41Z&sks=b&skv=2024-08-04&sig=JZEfNgcrz3s/mnQcLOUblJeXQhC2iO2JsDCzOs0fr3s%3D", "https://oaidalleapiprodscus.blob.core.windows.net/private/org-f90WsAXXoT74C7KIrKHfQNLF/user-aPZnYv1fPc18oeNp5tW2GGSL/img-XZ0SMhZJnJFcburn9w57AVxa.png?st=2025-02-02T05%3A27%3A08Z&se=2025-02-02T07%3A27%3A08Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-02-02T00%3A32%3A01Z&ske=2025-02-03T00%3A32%3A01Z&sks=b&skv=2024-08-04&sig=1j7iSjkOA29ncjA8a06V9eQh60g47Yb3tG6nfLo/EU0%3D"]
    # })

    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "")
        user_prompt_2 = data.get("prompt2", "")
        prompt_type = data.get("promptType", "")

        # # depends on frontend
        # child_name = request.form["child_name"]

        # might add type in later (i.e. test, disease or treatment)
        starting_prompt = generate_starting_prompt("Dummy", prompt_type, user_prompt, user_prompt_2)
        if not user_prompt or not prompt_type:
            return jsonify({"error": "Prompt is required"}), 400

        paragraphs, images = generate_output(starting_prompt)

        print(paragraphs)
        print(images)
        return jsonify({
            "captions": paragraphs,
            "images": images
        })
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


def generate_output(prompt):
    print("generating story")
    paragraphs = generate_short_story(prompt).split("\n\n")
    print("generating dalle prompts")
    dalle_prompts = [generate_dalle_prompt(p) for p in paragraphs]
    print("generating images")
    images = [generate_image(p) for p in dalle_prompts]

    return paragraphs, images


if __name__ == "__main__":
    app.run(debug=True)
