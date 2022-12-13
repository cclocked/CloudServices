import requests
from azure.cosmos import CosmosClient
import time
i = 1
while True:
    i = i+1

    api_key = "XXXXXXXXXXXXXXXXXX" ## your api-key here
    
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Give city name
    city_name = "Stockholm"
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    
    x = response.json()
    ## YOUR COSMOS INFO
    client = CosmosClient(
        "{your-cosmos-account}",

        "{your-primary-key}"
    )

    x["id"] = "Api_id" + str(i)
    print(x)
    print(type(x))

    database = client.get_database_client("YOUR DATABASE")
    container = database.get_container_client("YOUR CONTAINER")
    #container.create_item(document)
    container.create_item(x)
    # super bad busy-waiting : D
    time.sleep(900)