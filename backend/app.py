from flask import Flask, request, jsonify
from text_generation import generate_story_text, generate_chapter_to_prompt, shorten_text
from img_generation import generate_image


app = Flask(__name__)

@app.route("/prompt", methods=["POST"])
def prompt():
    if request.method == "POST":
        prompt = request.form["prompt"] # change this to whatever matches the frontend
        
        # list of dictionaries containing (revised_prompt, url)
        all_images_data, all_captions = get_images_and_captions_from_user_prompt(prompt)   
        return jsonify({
            "all_images": all_images_data,
            "all_captions": all_captions
        })


def get_images_and_captions_from_user_prompt(prompt, n=3):
    paragraphs = generate_story_text(prompt, n=n)
    print(paragraphs)
    paragraphs = paragraphs.split("\n\n")
    assert len(paragraphs) == n
    print("=" * 100)
    img_prompts = list(map(generate_chapter_to_prompt, paragraphs))
    print(img_prompts)
    print("=" * 100)
    images_data = list(map(generate_image, img_prompts))
    print(images_data)
    summarised_text = list(map(shorten_text, paragraphs))
    print("=" * 100)
    print(summarised_text)
    return images_data, summarised_text


if __name__ == "__main__":
    # app.run(debug=True)
    result = get_images_and_captions_from_user_prompt("My child has asthma. Show me the diagnosis")
