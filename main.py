# Python Setup Link https://code.visualstudio.com/docs/python/python-tutorial
import os
from tkinter.messagebox import YES
import openai

print("For the best results when answering questions, follow the examples shown at the end of each message.")

qString = "Give me a list of "

location = input(
    "What type of location would you like to stay at?(E.G. hotel): ")
qString += location + "s in "
qString += input("Where do you want to go? (E.G. city, state or state, country): ")
days = float(input("How many days do you wish to stay? (E.G. 1,2,3,etc.): "))
people = float(
    input("How many people are you paying for? (E.G. 1,2,3,etc.): "))
cost = float(input("What is your budget?(E.G. 1000): "))
perDayCost = str(round(cost/people/days, 2))
qString += " that cost less than $" + perDayCost + " per day and have a "
qString += input("What rating(stars specifically) would you like the establishment to have?(E.G. 1,2,3-5,etc.): ") + " star rating."

if input("Would you like to answer additional questions to make the search more accurate?(E.G. yes or no): ") == "yes":
    print("For the following questions, answer with yes or no.")
    questions = ["Wifi", "Breakfast", "Cable",
                 "24 hour check in", "a Gym", "a Pool"]
    optionalString = ""
    atLeastOne = False
    loopIndex = 0
    yesResponses = []
    for x in questions:
        if input("Do you want " + x + "?: ").lower() == "yes":
            yesResponses.append(x)
            atLeastOne = True
    if len(yesResponses) > 1:
        for x in yesResponses:
            if loopIndex == len(yesResponses)-1:
                optionalString += "and " + x + "."
            else:
                optionalString += x + ", "
            loopIndex += 1
    elif len(yesResponses) == 1:
        optionalString += yesResponses[0] + "."
    if (atLeastOne):
        qString += " The " + location + "s should have " + optionalString

print(qString)

openai.api_key = "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"
searchRequest = qString
response = openai.Completion.create(
    model="text-davinci-002",
    prompt=searchRequest,
    max_tokens=256,
    temperature=0.7
)

print(response["choices"][0]["text"])
print(" ")

