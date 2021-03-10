from requests_html import HTMLSession

url = ("https://zoeken.bigregister.nl/bignummer/09912495801")

session = HTMLSession()
response = session.get(url)

response.html.render(sleep=0.1)

text = response.html.text

Name = "Franken"
Letters_in_name = len(Name)

print(Letters_in_name)
Name_location = text.find(Name)
print(Name_location)
print(text.find(" ", (Name_location - 1), Name_location))

print(text.find("G", (Name_location + Letters_in_name + 1),
                (Name_location + Letters_in_name + 2)))
#print(text)
