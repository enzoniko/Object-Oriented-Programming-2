from newsapi import NewsApiClient
from datetime import datetime, timedelta

# Init
newsapi = NewsApiClient(api_key='d990b72484cd449188a699f77b9e1372')

#/v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='copa',
#                                           category='sports',
                                          
#                                           language='pt',
#                                           country='br')

def get_all_articles(q: str, category: str, sort_by: str, from_param: str = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"), to: str = datetime.now().strftime("%Y-%m-%d")):
    
    return newsapi.get_everything(q=q, from_param=from_param, to=to, sources=', '.join([newsapi.get_sources(category=category)['sources'][i]['id'] for i in range(len(newsapi.get_sources(category=category)['sources']))]), sort_by=sort_by, page=1)['articles']



#

