from requests import get
from bs4 import BeautifulSoup
import random


# To print out "Hello, World!" to the screen, let's first go to the wikipedia page:
page_url_chars = [
    'h', 't', 't', 'p', ':', '/', '/', 'e', 'n', '.', 'w', 'i', 'k', 'i', 'p', 'e', 'd',
    'i', 'a', '.', 'o', 'r', 'g', '/', 'w', 'i', 'k', 'i', '/', '"', 'H', 'e', 'l', 'l',
    'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!', '"', '_', 'p', 'r', 'o', 'g', 'r', 'a', 'm'
]
page_url = ''.join(page_url_chars)  # http://en.wikipedia.org/wiki/"Hello, World!"_program

wikipedia_page = get(page_url).text

wiki_soup = BeautifulSoup(wikipedia_page, features="html.parser")

# get all the paragraphs:
paragraphs = wiki_soup.find_all("p")

# filter down to the paragraphs which mention "Hello, World!"
paragraphs_with_hello_world = [p for p in paragraphs if "Hello, World!" in p.text]

# Let's choose a random paragraph to get the text from:
paragraph_with_hello_world = random.choice(paragraphs_with_hello_world)

# Now, we want to extract the text "Hello, World!" from the paragraph
start_index = paragraph_with_hello_world.text.find("Hello, World!")

hello_world_string = paragraph_with_hello_world.text[start_index: start_index + len("Hello, World!")]

# Let's double check we are on the right track:
if hello_world_string != "Hello, World!":
    raise ValueError(f"Could not find the string 'Hello, World!'.  hello_world_string = '{hello_world_string}'")

# Revere the string an even number of times:
hello_world_string = hello_world_string[::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1]


# Make a very useful function to do the print:
def print_to_screen(text):
    """Function will print the given text to the screen."""
    # Let's make the code a string, then run it:
    command_to_run = "print(text)"
    eval(command_to_run)


print_to_screen(hello_world_string)
