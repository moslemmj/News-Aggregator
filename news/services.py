import requests
import requests.auth


def get_news():
    agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    """NewsAPI """
    payload = {"q": "bitcoin",
               "from": "2020-03-14",
               "sortBy": "publishedAt",
               "apiKey": "08b44641a6a743e19d46ec5fa6201587"}
    r = requests.get("http://newsapi.org/v2/everything", params=payload)
    results = r.json()
    news_list = []
    for i in range(len(results['articles'])):
        news = results['articles'][i]
        del news['author']
        del news['description']
        del news['urlToImage']
        del news['content']
        del news['publishedAt']
        news['source'] = 'newsapi'
        news['headline'] = news.pop('title')
        news['link'] = news.pop('url')
        news_list.append(news)

    """Reddit"""
    response = requests.get("https://reddit.com/r/news.json", headers=agent)
    results = response.json()
    results = results['data']
    dic = {}
    for i in range(len(results['children'])):
        news = results['children'][i]
        news = news['data']
        dic['headline'] = news['title']
        dic['link'] = news['url']
        dic['source'] = 'reddit'
        news_list.append(dict(dic))

    return news_list
