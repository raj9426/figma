from bs4 import BeautifulSoup
import requests

# Make a request to the website and get the HTML
url = "https://en.m.wikipedia.org/wiki/Ajith_Kumar"
html = requests.get(url).content

# Create a Beautiful Soup object from the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all the elements with the class 'example-class'
elements = soup.find_all(id ='content-collapsible-block-0')

# Print the text of each element
for element in elements:
    print(1)
    print(element.text)