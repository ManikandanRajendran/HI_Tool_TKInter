import random
import time
import traceback

import requests
import json
import commonFunction
from commonFunction import generate_date, generate_string, random_numbers

# from testFolder import UI

address_id = ''
response = ''
dob = ''
webref = ''
postcode = ''
match_id = ''
opex_payload = ''
# userAndPropsDetails = ''
bcPayload = ''
annualPremium = ''
paymentOrder = ''
ordercode = ''
policyRef = ''
flag = False


def annualPremiumRound():
    amount = float(annualPremium)*100
    amount = int(amount)
    return str(amount)


# def defineOpex():
#     global opex_payload
#     opex_payload = "[{\"amount\": \"45.00\", \"code\": \"HAS2\", \"applied\":" + commonFunction.has + ", \"description\": \"Home Assistance Cover (DAS)\"},{\"amount\": \"25.99\", \"code\": \"ELC\", \"applied\":" + commonFunction.lec + ", \"description\": \"Legal Expenses Cover\"},{\"amount\": \"17.99\", \"code\": \"KEY1\", \"applied\":" + commonFunction.key + ", \"description\": \"Key Cover\"}]"


def propDetails():
    userAndPropsDetails = "\"attributes\": {\n      \"policy-reference\": null,\n      \"source-of-business\": null,\n      \"click-through-id\": null,\n      \"inception-date\": \"" + \
                   generate_date() + "T00:00:00Z\",\n      \"contact-method\": \"Email\",\n      \"policy-type\": \"HOMEINSURANCE\",\n      \"status\": \"Quote\",\n      \"proposer\": {\n        \"title\": \"Mr\",\n        \"forenames\": \"" + generate_string() + "\",\n        \"surname\": \"" + generate_string() + "\",\n        \"gender\": \"M\",\n        \"date-of-birth\": \"1989-05-06T00:00:00Z\",\n        \"marital-status\": \"S\",\n        \"email-address\": \"stratatesting" + str(
        random_numbers()) + "@centrica.com\",\n        \"mobile\": \"07448267439\",\n        \"previous-building-insurance\": false,\n        \"previous-content-insurance\": false,\n        \"resident-since\": \"1989-05-06T00:00:00Z\",\n        \"full-time-occupation\": {\n          \"status\": \"LtdComp\",\n          \"profession\": \"\",\n          \"industry\": \"\"\n        },\n        \"part-time-occupation\": {\n          \"status\": \"None\",\n          \"profession\": null,\n          \"industry\": null\n        }\n      },\n      \"joint-policy-holders\": [\n        \n      ],\n      \"property\": {\n        \"type\": \"Detached\",\n        \"year-built\": 1997,\n        \"construction-type\": \"Standard\",\n        \"bedrooms\": 1,\n        \"door-and-window-locks\": false,\n        \"alarm\": \"No\",\n        \"listed\": \"NoGrade\",\n        \"wall-construction-type\": \"B\",\n        \"roof-construction-type\": \"C\",\n        \"ownership\": \"Owned\",\n        \"over18\": \"2\",\n        \"under18\": \"1\",\n        \"bathrooms\": 1,\n        \"time-spent\": 5,\n        \"flat-roof\": \"0\",\n        \"smoke-detector\": \"YesSmoke\",\n        \"occupancy\": \"DailyUnoc\"\n      },\n      \"individual-specified-items\": [\n        \n      ],\n      \"unspecified-items-cover\": \"0.00\",\n      \"building-claims\": [\n        \n      ],\n      \"content-claims\": [\n        \n      ]"
    return userAndPropsDetails


def defineBuildingContentDetails():
    global bcPayload
    coverType = commonFunction.coverFor
    if coverType == "building":
        bcPayload = "\"content-cover-details\": null,\n      \"building-cover-details\": {\n        \"compulsory-excess\": null,\n        \"voluntary-excess\": \"250.00\",\n        \"accidental-damage\": " + commonFunction.buildingCover + ",\n        \"ncb-years\": 0\n "
    elif coverType == "content":
        bcPayload = "\"building-cover-details\": null,\n      \"content-cover-details\": {\n        \"compulsory-excess\": null,\n        \"voluntary-excess\": \"250.00\",\n        \"accidental-damage\": " + commonFunction.contentCover + ",\n        \"ncb-years\": 0\n"
    else:
        bcPayload = "\"building-cover-details\": {\n        \"compulsory-excess\": null,\n        \"voluntary-excess\": \"250.00\",\n        \"accidental-damage\": " + commonFunction.buildingCover + ",\n        \"ncb-years\": 0\n      },\n      \"content-cover-details\": {\n        \"compulsory-excess\": null,\n        \"voluntary-excess\": \"250.00\",\n        \"accidental-damage\": " + commonFunction.contentCover + ",\n        \"ncb-years\": 0\n"
    return bcPayload


def insurance_policies_post_payloads():
    insurance_Policies_Post = "{\n  \"data\": {\n" + propDetails() + ",\n      " + defineBuildingContentDetails() + "},\n      \"annual-premium\": null,\n      \"monthly-premium\": null,\n      \"optional-extras\": [{\"amount\": \"45.00\", \"code\": \"HAS2\", \"applied\":" + commonFunction.has + ", \"description\": \"Home Assistance Cover (DAS)\"},{\"amount\": \"25.99\", \"code\": \"ELC\", \"applied\":" + commonFunction.lec + ", \"description\": \"Legal Expenses Cover\"},{\"amount\": \"17.99\", \"code\": \"KEY1\", \"applied\":" + commonFunction.key + ", \"description\": \"Key Cover\"}],\n      \"document-history\": [\n        \n      ],\n      \"campaign\":" + commonFunction.promoCode + ",\n      \"endorsements\": [\n        \n      ],\n      \"bank-details\": null,\n      \"marketing-consents\": null,\n      \"insurer\": null\n    },\n    \"relationships\": {\n      \"customer-address\": {\n        \"data\": {\n          \"type\": \"addresses\",\n          \"id\": \"" + address_id + "\"\n        }\n      },\n      \"property-address\": {\n        \"data\": {\n          \"type\": \"addresses\",\n          \"id\": \"" + address_id + "\"\n        }\n      }\n    },\n    \"type\": \"insurance-policies\"\n  },\n  \"brand\": \"britishgas\"\n}"
    return insurance_Policies_Post


def insurance_policies_matches_post_payloads():
    insurance_Policies_Post = "{\n  \"jsonapi\": {\n    \"version\": \"1.0\"\n  },\n  \"data\": {\n    \"type\": \"insurance-policy-matches\",\n    \"attributes\": {\n      \"web-reference\": \"" + webref + "\",\n      \"date-of-birth\": \"1989-05-06T00:00:00Z\",\n      \"match-found\": null,\n      \"policy-reference\": null,\n      \"customer-postcode\": \"" + postcode + "\"\n      }\n  }\n}"
    return insurance_Policies_Post


def marketingConsentUpdate():
    Insurance_Policies_Mc = "{\n  \"data\": {\n    \"id\": \"" + webref + "\",\n    \"type\": \"insurance-policies\",\n    \"attributes\": {\n      \"marketing-consents\":{\n          \"email\":true,\n          \"phone\":true,\n          \"text\":true,            \n          \"post\":true      \n      }\n    }\n  }\n}"
    return Insurance_Policies_Mc


def paymentOrders():
    paymentOrdersPayload = "{\n  \"data\": {\n    \"type\": \"payment-orders\",\n    \"attributes\": {\n      \"amount\": \"" + annualPremium + "\",\n      \"merchant\": \"BGHOMEINSD\",\n      \"intent\":\"insurance\",\n      \"installation\": \"1278476\",\n      \"description\": \"Service Payment\",\n      \"reference\": \"" + webref + "\",\n      \"store-card\": false\n    }\n  } \n}"
    return paymentOrdersPayload


def worldPay():
    worldpayPayload = "<!DOCTYPE paymentService PUBLIC \"-//WorldPay//DTD WorldPay PaymentService v1//EN\"\n\"http://dtd.worldpay.com/paymentService_v1.dtd\">\n<paymentService version=\"1.4\" merchantCode=\"BGHOMEINSD\">\n    <notify>\n        <orderStatusEvent orderCode=\"" + webref + "-BGHOMEINSD-1571650785\">\n            <payment>\n                <paymentMethod>VISA_DEBIT-SSL</paymentMethod>\n                <paymentMethodDetail>\n                    <card number=\"************0106\" type=\"debitcard\">\n                        <expiryDate>\n                            <date month=\"08\" year=\"2021\"/>\n                        </expiryDate>\n                    </card>\n                </paymentMethodDetail>\n                <amount value=\"" + annualPremiumRound() + "\" currencyCode=\"GBP\" exponent=\"2\" debitCreditIndicator=\"credit\"/>\n                <lastEvent>AUTHORISED</lastEvent>\n                <CVCResultCode description=\"C\"/>\n                <cardHolderName>\n                    <![CDATA[Mr H test]]>\n                </cardHolderName>\n                <issuerCountryCode>GB</issuerCountryCode>\n                <balance accountType=\"IN_PROCESS_AUTHORISED\">\n                    <amount value=\"{{annualPremiumPennies}}\" currencyCode=\"GBP\" exponent=\"2\" debitCreditIndicator=\"credit\"/>\n                </balance>\n                <riskScore value=\"0\"/>\n            </payment>\n            <journal journalType=\"AUTHORISED\">\n                <bookingDate>\n                    <date dayOfMonth=\"21\" month=\"05\" year=\"2018\"/>\n                </bookingDate>\n                <accountTx accountType=\"IN_PROCESS_AUTHORISED\" batchId=\"6\">\n                    <amount value=\"" + annualPremiumRound() + "\" currencyCode=\"GBP\" exponent=\"2\" debitCreditIndicator=\"credit\"/>\n                </accountTx>\n            </journal>\n        </orderStatusEvent>\n    </notify>\n</paymentService>"
    return worldpayPayload


def paymentOrderPatch():
    payOrderPatchPayload = "{\n  \"data\": {\n    \"id\": \"" + paymentOrder + "\",\n    \"type\": \"payment-orders\",\n    \"attributes\": {\n      \"status\": \"success\",\n      \"mac\": \"508b96ef0c8ab4baabab37446a20d38bb4c59fc138aa5fd5d15ae700e7466c71\",\n      \"order-key\":\"BRITISHGAS^BGHOMEINSD^" + webref + "-BGHOMEINSD-1552490679\"\n    }\n  }\n}"
    return payOrderPatchPayload


def run_method(method, url, headers, params):
    global response
    if params == "insurance policies payload":
        payload = insurance_policies_post_payloads()
    elif params == "insurance policy matches payload":
        payload = insurance_policies_matches_post_payloads()
    elif params == "marketing preferences":
        payload = marketingConsentUpdate()
    elif params == "payment orders":
        payload = paymentOrders()
    elif params == "worldpay":
        payload = worldPay()
    elif params == "payment orders patch":
        payload = paymentOrderPatch()

    if method == "GET":
        response = requests.request(method, url, headers=headers, params=params)
    else:
        response = requests.request(method, url, data=payload, headers=headers)
        # print(params, url, response.status_code, response)
    try:
        response = json.loads(response.text)
    except SystemExit as msg:
        raise SystemExit(msg)
    except:
        traceback.print_exc(file=open('test.log', 'a'))
    return response


def runFinalMethod(method, url, headers, params):
    global response, policyRef, flag
    for i in range(10):
        response = requests.request(method, url, headers=headers, params=params)
        # print(params, url, response.status_code, response)
        response = json.loads(response.text)
        complete = response['data']['attributes']['complete']
        policyRef = response['data']['attributes']['policy-reference']
        if policyRef is not "null":
            if complete is True:
                flag = True
                return "Success"
                break
            else:
                time.sleep(2)
        else:
            time.sleep(2)

    if not flag:
        return response


def get_address_id():
    global address_id, postcode
    lens = response['data']
    address_number = random.randrange(1, len(lens))
    address_id = response['data'][address_number - 1]['id']
    postcode = response['data'][address_number - 1]['attributes']['postcode']


def get_webref():
    global webref, annualPremium
    webref = response['data']['id']
    annualPremium = response['data']['attributes']['annual-premium']['amount']


def getPaymentOrder():
    global paymentOrder, ordercode
    paymentOrder = response['data']['id']
    ordercode = response['data']['attributes']['order-code']


def get_details():
    return "postcode : " + postcode + " \n dob : 06-05-1989 \n Web reference : " + webref


def get_details1():
    return "postcode : " + postcode + " \n dob : 06-05-1989 \n policy reference : " + policyRef


def get_matchid():
    global match_id
    match_id = response['data']['id']
    return match_id
