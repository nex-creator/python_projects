import os
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = "xxxxxxxxxxxxxxxxxx"
stock_parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}
news_parameter ={
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_ENDPOINT,params= stock_parameter)
response.raise_for_status()
print(response.status_code)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
print(data_list)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_data =float(data_list[0]['4. close'])
print(yesterday_data)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = float(data_list[1]['4. close'])
print(day_before_yesterday_data)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

abs_difference = abs(yesterday_data - day_before_yesterday_data)
print(f"{abs_difference:.2f}")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_diff = (abs_difference/yesterday_data)*100
print(f"{percentage_diff:.2f}")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_diff >2:
    response_news = requests.get(url= NEWS_ENDPOINT, params= news_parameter)
    response_news.raise_for_status()
    print(response_news.status_code)
    articles = response_news.json()['articles']
    print(articles)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:4]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    #[news_item for item in list]
    formatted_articles = [f"Headline:{article['title']}. \nBrief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        print(f"{article}")

