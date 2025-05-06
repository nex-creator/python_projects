import requests
from datetime import datetime

GENDER= "Female"
AGE = 31
WEIGHT_KG = 56
HEIGHT_CM= 154
APP_ID= "xxxxxxx"
API_KEY="xxxxxxxxxxxxx"
exercise_stat_endpoint ="https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise yor did:")
sheety_endpoint = "https://api.sheety.co/b683551374c04d0bb013761c2ee11db0/<worksheetname>/sheet1"
today_date= datetime.now().strftime("%Y%m%d")
today_time = datetime.now().strftime("%H%M%S")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_params ={
    "query":exercise_text,
    "gender": GENDER,
    "age": AGE,
    "height_cm": HEIGHT_CM,
    "weight_kg": WEIGHT_KG
}
print(today_time)
print(today_date)
response = requests.post(url= exercise_stat_endpoint, json = exercise_params,headers = headers)
result = response.json()
print(result)

for exercises in result["exercises"]:
    new_row={
        "sheet1":{
            "date": today_date,
            "time": today_time,
            "exercise":exercises['name'].title(),
            "duration":exercises['duration_min'],
            "calories":exercises['nf_calories'],
        }
    }

sheety_header= {
    "Content-Type": "application/json",
}

sheety_response = requests.post(url = sheety_endpoint, json = new_row,headers= sheety_header)
print(sheety_response.json())