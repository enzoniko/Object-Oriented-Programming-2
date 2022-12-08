from newsapi import NewsApiClient
from datetime import datetime, timedelta

# Init
newsapi = NewsApiClient(api_key='d990b72484cd449188a699f77b9e1372')

#/v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='copa',
#                                           category='sports',
                                          
#                                           language='pt',
#                                           country='br')


# /v2/everything
all_articles = newsapi.get_everything(q='futebol',
                                      from_param=(datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                                      to=datetime.now().strftime("%Y-%m-%d"),
                                      language='pt',
                                      sort_by='popularity',
                                      page=2)




#', '.join([newsapi.get_sources(category='sports')['sources'][i]['id'] for i in range(len(newsapi.get_sources(category='sports')['sources']))])

