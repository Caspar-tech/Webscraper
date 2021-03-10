import requests
from requests_html import HTMLSession

# BIG geldig maar geen HA
#BIG = 59919419601
# BIG huisarts
#BIG = 19059287401
# BIG ongeldig
#BIG = 59919419602

BIG_list = [59919419601, 19059287401, 59919419602]

# We loop trough all BIG-numbers in the list.
# For every number we load the website and check the content
for BIG in BIG_list:
    # We create the URL to load using the BIG-number from the list
    url = ("https://zoeken.bigregister.nl/bignummer/%s" % str(BIG))

    # This code block uses HTMLsession
    # https://requests.readthedocs.io/projects/requests-html/en/latest/
    session = HTMLSession()
    response = session.get(url)
    # With adding "sleep" we wait a short while while the script is executed
    # than after waiting we get the website as loaded
    # without sleep it renders too fast and we get the website before the script is executed
    response.html.render(sleep=0.1)

    # We place the rendered website in a variable called "text"
    text = response.html.text

    # We use parsing to searh the text
    # only when a BIG-number is true the word "Naam" occurs
    # only when a true Big-number belongs to a huisarts the word "Huisartsgeneeskunde" occurs
    # When the word does not occur it will produce "-1"
    Check_BIG_Naam = text.find("Naam")
    Check_BIG_Huisartsgeneeskunde = text.find("Huisartsgeneeskunde")

    print(BIG)
    if Check_BIG_Huisartsgeneeskunde > -1:
        print("BIG is gekoppeld aan huisarts")
    elif Check_BIG_Naam > -1:
        print("BIG is geldig, maar geen huisarts")
    else:
        print("BIG levert geen resultaat op")

    print("------------------------------------")


