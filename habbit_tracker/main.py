import requests
from datetime import datetime
today = datetime.now()
today_date = today.strftime("%Y%m%d")
TOKEN = "xxxxxxxx"
USERNAME = "xxxxxxxxx"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_update = f"{pixel_creation_endpoint}/{today_date}"


user_params= {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
graph_config= {
    "id":GRAPH_ID,
    "name":"Cycling graph",
    "unit":"km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

post_pixel = {
    "date":today_date,
    "quantity":"11",
}

update_pixel = {
    "quantity" : "4",
}
# response = requests.post(url= pixela_endpoint, json = user_params)
# # print(response.text)
# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)
# response = requests.post(url = pixel_creation_endpoint, json = post_pixel, headers = headers)
# print(response.text)
response = requests.delete(url = pixel_update, headers = headers)
print(response.text)
