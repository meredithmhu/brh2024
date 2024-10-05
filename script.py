#List of user data that we'll call on to make the ChatGPT query
class user:
    gender = 'female'
    race = 'Asian'
    age = '23'
    height = '5\'4\"'
    size = '6'
    skincolor = 'very pale'
    haircolor = 'black'
    hairlength = 'shoulder-length'

meredith_user_profile = """I am an Asian female in her early 20's. 
My height is 5'4 and my dress size is a size 6. 
I am very pale-skinned and I have shoulder length black hair.
"""

user_input = "wedding"
zara_codes = []

def main():
    print("Hello World")

main()

#Obtain the most general query from the user through user input. This will be replaced by another form of user input through the developed UI later on.
user_geninput = input('Enter a general query to start looking for clothes: ')

#Given a person's profile information and the general query, construct a detailed query to pass to the LLM.
"""
How a query can be structured?
'What should I wear for a ' + user_geninput + '? I am a + user.race + ' ' + user.gender + ' aged ' + user.age + '. My height is ' + user.height + ' and I am a size ' + user_size + '. My skin is ' + user.skincolor + ' and my hair is ' + user.haircolor + ' and ' + user.hairlength + '.'
"""

#Import the LLM and pass the query to  
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

#take the output Chat gives, and use the output to search the database of choice (Zara? H&M? Amazon etc.) for matching items

#get the image data and links and pass it to the fun visual output on the user interface.
