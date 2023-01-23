#!C:\\Users\\dgooch\\AppData\\Local\\Programs\\Python\\Python311

import requests, json
api_url = "https://192.168.74.1:8443/api/v2/monitor/router/ipv4/?access_token=<your token>"

##added these lines to prevent the warning for insecure request
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


##This opens the api request and prints the entire thing
try: 
    response = requests.get(
    api_url,
    verify=False
    )
    jsonresponse = response.json()
    # print("Entire JSON response")
    # print(jsonresponse)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

##This code assigns a variable to the nested dictionary named results
json_results = jsonresponse['results']


##this looks for the ip_mask value.  If it is 
for value in json_results:
    if value['ip_mask'] == '0.0.0.0/0':
        print (value['interface'], "gateway :", value['gateway']) 



####adding this just to verify that there was content in the response
#print(response.json())

##This line prints the entire output of the request results in a nice readable format
# print(json.dumps(jsonresponse, indent=4, sort_keys=True))
