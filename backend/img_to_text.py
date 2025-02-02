import openai
from api_key import API_KEY
# client = OpenAI(api_key=API_KEY)


PROMPT = "My child has asthma."
# response = client.chat.completions.create(
#     model="dall-e-3",
#     prompt=f"Create a storyboard with 3 images to come up with a story that teaches the child about the following disease. {PROMPT}"
#     n = 3,
#     size="1024x1024"
# )

openai.api_key = API_KEY

response = openai.images.generate(
    model="dall-e-3",
    prompt=f"Create a storyboard with 3 images to come up with a story that teaches the child about the following disease. {PROMPT}",
    size="1024x1024",
    n=1
)

data = response.data
print(len(data))
print(data[0].url)
print(data[1].url)
print(data[2].url)