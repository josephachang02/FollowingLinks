import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL: ")

response = urllib.request.urlopen(url)
html_content = response.read()

count = int(input("Enter Count:"))
position = int(input("Enter Position:"))


for name in range(count):
    response = urllib.request.urlopen(url)
    html_content = response.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    anchor_tags = soup.find_all('a')

    link = anchor_tags[position - 1].get('href')

    url = link

# Extract the last name from the final page loaded
last_name = url.split('/')[-1].split('.')[0]
print("Last name:", last_name)