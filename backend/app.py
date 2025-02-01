from flask import Flask, request



app = Flask(__name__)

@app.route("/")
def index():
    pass


@app.route("/prompt", methods=["POST"])
def prompt():
    if request.method == "POST":
        # takes in prompt from frontend

        # pass into LLM to get complex story split into n short chapters

        # convert chapters into text-to-image prompt

        # pass into image generator to get images

        # pass into LLM again to make story simpler

        # output result

        pass


if __name__ == "__main__":
    app.run(debug=True)
