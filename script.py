#!/usr/bin/python3

#imported libraries 
import json
from openai import OpenAI
"""
script.py
~Proof-of-Concept for the DressMe.ai~
Script that already contains the profile information of the user, takes in a query from the user
and asks an LLM for clothing recommendations for the user's profile and query. 
Script then searches the database of a particular clothing brand's in-stock items for the recommended
items and returns the found products. 
""" 

#Class that defines a user profile. User profile will be hard-coded for now
class user:
    name = 'Meredith'
    gender = 'female'
    race = 'Asian'
    age = '23'
    height = '5\'4\"'
    dress_size = '6'
    skincolor = 'very pale'
    haircolor = 'black'
    hairlength = 'shoulder-length'


meredith_user_profile = """
Asian female in her early 20's. 
Height is 5'4 and dress size is size 6. 
Very pale-skinned with shoulder length black hair.
"""

#Introduction. Script welcomes back user and reminds them of their data.
print("Welcome back, " + user.name + ". " + "Your user profile was " + meredith_user_profile + ". ")

user_store_input = input("What store are you interested in shopping at? ")

print("\n\n")
#Obtain the most general query from the user through user input. This will be replaced by another form of user input through the developed UI later on.
user_geninput = input('What event or scenario would you like clothing recommendations for?: ')
print("\n\n")

#Given a person's profile information and the general query, construct a detailed query to pass to the LLM.
query = 'What should I wear for a ' + user_geninput + '? I am a ' + user.race + " " + user.gender + ' aged ' + user.age + '. My height is ' + user.height + ' and I am a size ' + user.dress_size + '. My skin is ' + user.skincolor + ' and my hair is ' + user.haircolor + ' and ' + user.hairlength + '.' + \
" Give me a list of suggested clothing items in a python list format. "


# Initialize OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": query
        }
    ]
)

chat_output = completion.choices[0].message.content

# changing the chatGPT output into a python list of items
chat_output = chat_output.split("[")[1]
chat_output = chat_output.split("]")[0]
chat_output = "[" + chat_output + "]"
chat_output = json.loads(chat_output)

#Script tells client what the AI suggests.
print("Our intelligent clothes helper tool suggests you wear the following items to your " + user_geninput + ": ")
print("\n")

#generates search queries for online retailer based on chatGPT suggested clothing items
link_list = []
for clothing_item in chat_output:
    print(clothing_item)
    ai_reply = clothing_item.lower()
    search_query = "https://www.zara.com/us/en/search?searchTerm=" + ai_reply
    link_list.append(search_query)

print("\n\n")
#prompt the user on if they would like links to these items:
user_geninput2 = input('Would you like URLs corresponding to searches for each of these items on the Zara website? (y/n): ')
print("\n")
if user_geninput2 == "y":
    for link in link_list:
        print(link)

print("\n\n")
print("Thanks for using the DressMe.ai! Good luck at your " + user_geninput + ", " + user.name + ".\n")