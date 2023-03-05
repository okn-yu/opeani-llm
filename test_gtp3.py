                                                                                                                                                                                                           
import os
import openai

from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

openai.api_key = os.getenv("OPENAI_API_KEY")

gpt_prompt = "日本の首都を教えて下さい。ただし回答は日本語です。"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


print(response['choices'][0]['text'])

