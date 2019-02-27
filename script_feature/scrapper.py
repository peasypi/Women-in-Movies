# import libraries
from bs4 import BeautifulSoup
import requests
import sys
import argparse

parser = argparse.ArgumentParser(description="Film-Title")
parser.add_argument("film", help="display the element of speech of specific characters in a chosen film", type = str)
args = parser.parse_args()

page = requests.get("https://www.imsdb.com/scripts/{}.html".format(args.film))
soup = BeautifulSoup(page.content, 'html.parser')

for tag in soup.find_all('pre'):
    script = tag.text

print(script)