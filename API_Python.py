import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == "__main__":
    speak("News for today")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=19ffe3c80cee4e6fb929e945a5dda81f"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arts = news_dict['articles']

    for article in arts:
        speak(article['title'])
        speak("Moving onto next news.listen carefully")

