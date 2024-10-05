#!/usr/bin/python3

#imported libraries 

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
    gender = 'female'
    race = 'Asian'
    age = '23'
    height = '5\'4\"'
    dress_size = '6'
    skincolor = 'very pale'
    haircolor = 'black'
    hairlength = 'shoulder-length'

'''
meredith_user_profile = """I am an Asian female in her early 20's. 
My height is 5'4 and my dress size is a size 6. 
I am very pale-skinned and I have shoulder length black hair.
"""
'''

#user input, hard-coded for now 
user_input = "wedding"
#Obtain the most general query from the user through user input. This will be replaced by another form of user input through the developed UI later on.
user_geninput = input('What event or scenario would you like clothing recommendations for?: ')

#Given a person's profile information and the general query, construct a detailed query to pass to the LLM.
query = 'What should I wear for a ' + user_geninput + '? I am a ' + user.race + " " + user.gender + ' aged ' + user.age + '. My height is ' + user.height + ' and I am a size ' + user.dress_size + '. My skin is ' + user.skincolor + ' and my hair is ' + user.haircolor + ' and ' + user.hairlength + '.'


#Import the LLM (in this case, Meta LLaMa)
"""
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)

"""

#take the output Chat gives, and use the output to search the database of choice (Zara? H&M? Amazon etc.) for matching items

#get the image data and links and pass it to the fun visual output on the user interface.

#main function for testing 
def main():
    print("Hello World")
    print(query)

main()