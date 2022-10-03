#Python Setup Link https://code.visualstudio.com/docs/python/python-tutorial

import openai
openai.api_key = "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"

# list engines
engines = openai.Engine.list()

# print the first engine's id
print(engines.data[0].id)

# create a completion
completion = openai.Completion.create(engine="ada", prompt="Hello world")

# print the completion
print(completion.choices[0].text)

def helloWorld(args):
    print(args);
    
helloWorld("howdy");