import requests
from requests_html import HTMLSession

### https://requests.readthedocs.io/projects/requests-html/en/latest/

# BIG geldig maar geen HA
#BIG = 59919419601
# BIG huisarts
#BIG = 19059287401
# BIG ongeldig
#BIG = 59919419602

BIG_list = [59919419601, 19059287401, 59919419602]

for BIG in BIG_list:
    print("https://zoeken.bigregister.nl/bignummer/%s" % str(BIG))
    url = ("https://zoeken.bigregister.nl/bignummer/%s" % str(BIG))

    session = HTMLSession()
    response = session.get(url)

    response.html.render(sleep=0.2)

    text = response.html.text
    print(text)

    Check_BIG_Naam = text.find("Naam")
    #print("BIG_naam: " + str(Check_BIG_Naam))
    Check_BIG_Huisartsgeneeskunde = text.find("Huisartsgeneeskunde")

    if Check_BIG_Huisartsgeneeskunde > -1:
        print("BIG is gekoppeld aan huisarts")
    elif Check_BIG_Naam > -1:
        print("BIG is geldig, maar geen huisarts")
    else:
        print("BIG levert geen resultaat op")


