import requests
from requests_html import HTMLSession

### https://requests.readthedocs.io/projects/requests-html/en/latest/

BIG = 59919419601

url = ("https://zoeken.bigregister.nl/bignummer/%s" % BIG)

session = HTMLSession()
response = session.get(url)

response.html.render()

print(response.html.text)

# (reponse.html.search("Naam"))

