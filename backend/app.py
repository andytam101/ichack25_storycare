from flask import Flask, request



app = Flask(__name__)

@app.route("/")
def index():
    pass


@app.route("/prompt", methods=["POST"])
def prompt():
    if request.method == "POST":
        # takes in prompt from frontend

        # pass into LLM to get complex story

        # pass into image generator to get stuff

        # pass into LLM again to make story simpler

        # output result

        pass
