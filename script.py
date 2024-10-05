meredith_user_profile = """I am an Asian female in her early 20's. 
My height is 5'4 and my dress size is a size 6. 
I am very pale-skinned and I have shoulder length black hair.
"""

user_input = "wedding"
zara_codes = []

def main():
    print("Hello World")

main()
#Obtain the most general query from the user (e.g. "wedding")

#Given a person's profile info, ask ChatGPT the prompt user input, and give them the user's profile info. = "what would meredith look good in for a wedding"
#pass meredith user profile into ChatGPT 
#then pass in "what would I look good in at a wedding"
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
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
