from newsapi import NewsApiClient, newsapi_exception
from datetime import datetime, timedelta

# Init d990b72484cd449188a699f77b9e1372
newsapi = NewsApiClient(api_key='da8e1c9d66644e9697aab0786c9c9f12')

#/v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='copa',
#                                           category='sports',
                                          
#                                           language='pt',
#                                           country='br')

def get_all_articles(q: str, category: str, sort_by: str, from_param: str = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"), to: str = datetime.now().strftime("%Y-%m-%d")):
    try:
        articles = newsapi.get_everything(q=q, from_param=from_param, to=to, sources=', '.join([newsapi.get_sources(category=category)['sources'][i]['id'] for i in range(len(newsapi.get_sources(category=category)['sources']))]), sort_by=sort_by, page=1)['articles']
    except newsapi_exception.NewsAPIException:
        articles = []
    return articles


# articles = newsapi.get_everything(q='futbol', from_param=(datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"), to=datetime.now().strftime("%Y-%m-%d"), sources=', '.join([newsapi.get_sources(category='sports')['sources'][i]['id'] for i in range(len(newsapi.get_sources(category='sports')['sources']))]), sort_by='publishedAt', page=1)['articles']
# def get_all_articles(q: str, category: str, sort_by: str, from_param: str, to: str):
   
#     return articles


