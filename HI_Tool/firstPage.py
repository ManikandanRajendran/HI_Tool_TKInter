import run_page, commonFunction
environment=''


flag = True
headers_get = commonFunction.get_headers
headers_post = commonFunction.post_headers


def fetch_postcode(postcode, envDetails):
    global flag, environment
    environment = envDetails
    if not postcode:
        postcode = "NG9 1LL"
    querystring = {"postcode": postcode}
    env = commonFunction.get_api_environment(environment, "addresses")
    response = run_page.run_method("GET", env, headers_get, querystring)
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']
    else:
        run_page.get_address_id()
        return True


def post_insurance_policy():
    global flag
    env = commonFunction.get_api_environment(environment, "insurance-policies")
    response = run_page.run_method("POST", env, headers_post, "insurance policies payload")
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']
    else:
        run_page.get_webref()
        return True


def post_insurance_policy_matches():
    global flag
    env = commonFunction.get_api_environment(environment, "insurance-policy-matches")
    response = run_page.run_method("POST", env, headers_post, "insurance policy matches payload")
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']
    else:
        match_id = run_page.get_matchid()
        quote_summary = commonFunction.get_UI_environment(environment, match_id)
        return quote_summary


def marketingConsent():
    global flag
    endpoint = "insurance-policies/"+run_page.webref+"?match-id="+run_page.match_id
    env = commonFunction.get_api_environment(environment, endpoint)
    response = run_page.run_method("PATCH", env, headers_post, "marketing preferences")
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']


def paymentOrders():
    global flag
    env = commonFunction.get_api_environment(environment, "payment-orders")
    response = run_page.run_method("POST", env, headers_post, "payment orders")
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']
    else:
        run_page.getPaymentOrder()
        return True


def worldpayPay():
    global flag
    env = commonFunction.get_api_environment(environment, "insurance/notifications/card-payments/worldpay")
    response = run_page.run_method("POST", env, headers_post, "worldpay")
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']


def paymentOrdersPatch():
    global flag
    env = commonFunction.get_api_environment(environment, "payment-orders/"+run_page.paymentOrder)
    response = run_page.run_method("PATCH", env, headers_post, "payment orders patch")
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']


def policyPurchase():
    global flag
    env = commonFunction.get_api_environment(environment, "insurance-policy-purchase-statuses/" + run_page.webref)
    response = run_page.runFinalMethod("GET", env, headers_post, "policy purchase")
    if 'errors' in response:
        flag = False
        return response['errors'][0]['detail']
    else:
        # print("inside else : ", run_page.get_details1())
        return run_page.get_details1()


def getQuoteLink(postcode, envDetails):
    global flag
    flag = True
    result = fetch_postcode(postcode, envDetails)
    if flag:
        result1 = post_insurance_policy()
        if flag:
            quotePage = post_insurance_policy_matches()
            return quotePage
        else:
            return result1
    else:
        return result


def getQuoteDetails(postcode, envDetails):
    global flag
    flag = True
    result = fetch_postcode(postcode, envDetails)
    if flag:
        result1 = post_insurance_policy()
        if flag:
            # quotePage = post_insurance_policy_matches()
            return "success"
        else:
            return result1
    else:
        return result


def getDetailsforRetDocs(postcode, envDetails):
    global flag
    flag = True
    result = fetch_postcode(postcode, envDetails)
    if flag:
        result1 = post_insurance_policy()
        if flag:
            quotePage = post_insurance_policy_matches()
            if flag:
                marketing = marketingConsent()
                if flag:
                    payment1 = paymentOrders()
                    if flag:
                        worldPay = worldpayPay()
                        if flag:
                            payment2 = paymentOrdersPatch()
                            if flag:
                                purchase = policyPurchase()
                                return purchase
                            else:
                                return payment2
                        else:
                            return worldPay
                    else:
                        return payment1
                else:
                    return marketing
            else:
                return quotePage
        else:
            return result1
    else:
        return result


