import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e83795e99fmsha2c3b256945c2c4p153d84jsn5b31cf2aad92"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)