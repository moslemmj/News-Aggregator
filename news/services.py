import requests
import requests.auth


def newsapi_list_and_search(*query):
    """NewsAPI"""
    if query:
        payload = {"q": query,
               "from": "2020-03-14",
               "sortBy": "publishedAt",
               "apiKey": "08b44641a6a743e19d46ec5fa6201587"}
    else:
        payload = {"q": 'bitcoin',
                   "from": "2020-03-14",
                   "sortBy": "publishedAt",
                   "apiKey": "08b44641a6a743e19d46ec5fa6201587"}

    newsapi_response = requests.get("http://newsapi.org/v2/everything", params=payload)
    results = newsapi_response.json()
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
    return news_list


def reddit_list_news(*query):
    """Reddit"""
    dic = {}
    news_list = []
    agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    if query:
        payload = {
            "q": query,
            "restrict_sr": "1",
        }
        agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        reddit_response = requests.get("https://reddit.com/r/news/search.json", params=payload, headers=agent)
    else:
        reddit_response = requests.get("https://reddit.com/r/news.json", headers=agent)
    results = reddit_response.json()
    results = results['data']

    for i in range(len(results['children'])):
        news = results['children'][i]
        news = news['data']
        dic['headline'] = news['title']
        dic['link'] = news['url']
        dic['source'] = 'reddit'
        news_list.append(dict(dic))

    return news_list


def get_news():
    """NewsAPI"""
    main_list = newsapi_list_and_search()
    """reddit"""
    main_list.extend(reddit_list_news())

    return main_list


def search_news(query):
    """NewsAPI"""
    main_list = newsapi_list_and_search(query)
    """reddit"""
    main_list.extend(reddit_list_news(query))

    return main_list
