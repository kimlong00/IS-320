#the requests package was installed prior to running this app
#using this command at terminal within vs code
# pip install requests==2.18.4
# and since my install went into an earlier miniconda install folder, 
# i also had to switch out the interpreter to the miniconda one (lower left corner)
import requests
import time
from datetime import datetime
BITCOIN_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def get_current_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    #print(response_json)  
    #  the print was done to figure out where the price was, in the response
    # for doing the [ ] indexing below
    print(response_json)
    print(response_json['bpi']['USD']['rate'])
    print(type(response_json['bpi']['USD']['rate']))
    
    return response_json['bpi']['USD']['rate']


price_history = []  #a list of key-value pairs
count = 0    #to allow user to quit the app
while True:
    count += 1
    price = get_current_bitcoin_price()
    date = datetime.now()
    price_history.append({'date': date, 'price': price})
    time.sleep(5)    #wait 20 seconds. once verified, this can be increased
    if count % 2 == 0:    #giving user option to quit every 40 seconds
        quit = int(input('wanna stop? 1/0>>'))
        if quit:
            break
    
print(price_history)   #can send this information to user as notification
#for example, subject to conditions such as price above or below specific values,
#or price change above specific values, alerts could be generated, and sent out
#to the user.  Just as an api was used to retrieve prices, some other api may be
#used to send information out, to show up as an alert on the user's phone, for
#example. Using IFTTT webhooks is one way to do so.