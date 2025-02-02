from app import get_images_and_captions_from_user_prompt
from argparse import ArgumentParser
import os
import json


PROMPT = "My child has asthma."


def get_args():
    parser = ArgumentParser()
    parser.add_argument("name", type=str)
    return parser.parse_args()


def main():
    args = get_args()
    filename = args.name + ".json"

    with open(filename, "r") as f:
        data = json.load(f)
        f.close()
   
    paras, prompts, images, summaries = get_images_and_captions_from_user_prompt(PROMPT, data)
    output_file = args.name + ".txt"
    
    output_str = "\n\n".join(paras)
    output_str += "\n" + ("=" * 100) + "\n"
    output_str += "\n\n".join(prompts)
    output_str += "\n" + ("=" * 100) + "\n"
    output_str += "\n".join(list(map(lambda x: x["url"], images)))
    output_str += "\n" + ("=" * 100) + "\n"
    output_str += "\n".join(summaries)

    with open(output_file, "w") as f:
        f.write(output_str)
    
if __name__ == "__main__":
    main()
