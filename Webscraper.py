import requests
from requests_html import HTMLSession

### https://requests.readthedocs.io/projects/requests-html/en/latest/

url = "https://zoeken.bigregister.nl/bignummer/59919419601"

session = HTMLSession()
response = session.get(url)

response.html.render()

print(response.html.text)

