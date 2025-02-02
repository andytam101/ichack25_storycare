from openai import OpenAI
client = OpenAI(api_key="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")

result = client.images.generate(
  model="dall-e-3",
  prompt="Create an image of a cute, anthropomorphic heart named Piper, full of joy and radiating vibrant colors. Piper is in a whimsical, magical kingdom called Heartland, where everything around is heart-themed and happy. Include a kindly, wise Heart Doctor observing Piper with a look of admiration, surrounded by an atmosphere of love and life in the kingdom. Do not use dialogue and fit for a children's story.",
  n=1,
  size="1024x1024",
  style="vivd"
)

print(result.data)
