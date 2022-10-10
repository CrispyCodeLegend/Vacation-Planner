#Python Setup Link https://code.visualstudio.com/docs/python/python-tutorial
import os
import openai
openai.api_key = "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"
searchRequest ="Give me a list of Hotels in Cabo San Lucas, Mexico that cost less than $1000 per day and have a 4 star rating"
response = openai.Completion.create(
  model="text-davinci-002",
  prompt=searchRequest,
  max_tokens=256,
  temperature=0.7
)
print(response)
