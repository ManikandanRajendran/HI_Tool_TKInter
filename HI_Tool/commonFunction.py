import datetime
import random
import string
import re

buildingCover = ''
contentCover = ''
has = ''
lec = ''
key = ''
coverFor = ''
promoCode = ''


def applyPromo(value):
    global promoCode
    if not value:
        promoCode = "null"
    else:
        promoCode = value
    # return promoCode


def check_opex(var3, var4, var5):
    global has, lec, key
    has = 'false'
    lec = 'false'
    key = 'false'
    if var3.get() == 1:
        has = "true"
    if var4.get() == 1:
        if promoCode == 'null':
            lec = "true"
    if var5.get() == 1:
        key = "true"
    # print(has, " : ", lec, " : ", key)


def check_accidentalDamage_b(var1):
    global buildingCover
    buildingCover = 'false'
    if var1.get() == 1:
        buildingCover = "true"
    # print(buildingCover)


def check_accidentalDamage_c(var2):
    global contentCover
    contentCover = 'false'
    if var2.get() == 1:
        contentCover = "true"
    # print(contentCover)


def check_coverDetails(var6, var7, var8):
    global coverFor
    if var6.get() == 1:
        coverFor = "building"
    else:
        if var7.get() == 1:
            coverFor = "content"
        else:
            if var8.get() == 1:
                coverFor = "both"
            else:
                coverFor = "both"


def generate_date():
    x = datetime.datetime.now()
    date = str(x).split(" ")
    return date[0]


def generate_string():
    chars = "".join([random.choice(string.ascii_lowercase) for i in range(5)])
    return chars


def random_numbers():
    number = random.randrange(1, 2000)
    return number


def get_api_environment(arg, endpoint):
    if "QA" in arg:
        match = re.match(r"([a-z]+)([0-9]+)", arg, re.I)
        if match:
            items = match.groups()
            x = int(items[1]) + 1
        url = "https://api" + str(x) + ".bgo.bgdigitaltest.co.uk/v1/" + endpoint
    else:
        url = "https://api1.bgo.bgdigitaltest.co.uk/v1/" + endpoint
    return url


def get_UI_environment(arg, id):
    if "QA" in arg:
        match = re.match(r"([a-z]+)([0-9]+)", arg, re.I)
        if match:
            items = match.groups()
            x = int(items[1]) + 1
        url = "https://www" + str(
            x) + ".bgo.bgdigitaltest.co.uk/home-services/insurance/home-insurance/your-quote?match-id=" + id + "&branch=8e0b02bdcf65fdac5346a2fa0d97769b0b6d8851"
    else:
        url = "https://www1.bgo.bgdigitaltest.co.uk/home-services/insurance/home-insurance/your-quote?match-id=" + id
    return url


get_headers = {
    'x-client-id': "cbdcfa43-dd67-4c38-b418-83572a936fca",
    'Accept': "application/vnd.api+json",
    'cache-control': "no-cache",
    'Postman-Token': "72babe38-cba5-4bcf-8d0a-bdca5f8a9cb5"
}

post_headers = {
    'x-client-id': "cbdcfa43-dd67-4c38-b418-83572a936fca",
    'X-skip-reCAPTCHA-check': "true",
    'Content-Type': "application/vnd.api+json",
    'Origin': "http://www.britishgas.co.uk",
    'cache-control': "no-cache",
    'Postman-Token': "5219e7e2-357d-4e83-95bc-93ecc85d408d"
}
